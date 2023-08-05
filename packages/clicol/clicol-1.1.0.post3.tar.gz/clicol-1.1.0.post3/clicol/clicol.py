#!/usr/bin/python

""" clicol.py - Colorize CLI and more

    Copyright (C) 2017-2019 Viktor Kertesz
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    If you need to contact the author, you can do so by emailing:
    vkertesz2 [~at~] gmail [/dot\] com
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
#import pudb

try:
    #  python2
    import ConfigParser

except ImportError:
    #  python3
    import configparser as ConfigParser

import os
import sys
import re
import string
import pexpect
import timeit
import threading
import time
import signal
from pkg_resources import resource_filename
from . command import getCommand
from . command import getRegex
from . command import getTerminalSize
from . __init__ import __version__

# Global variables
conn = ''         # connection handler
buffer = u''       # input buffer
lastline = u''     # input buffer's last line
is_break = False  # is break key pressed?
effects = set()   # state effects set
ct = dict()       # color table (contains colors)
cmap = list()     # color map (contains coloring rules)
pause = 0         # if true, then coloring is paused
# match for interactive input (prompt,eof)
debug = 0         # global debug (D: hidden command)
timeout = 0       # counts timeout
maxtimeout = 0    # maximum timeout (0 turns off this feature)
prevents = 0      # counts timeout prevention
maxprevents = 0   # maximum number of timeout prevention (0 turns this off)
RUNNING = True    # signal to timeoutcheck
WORKING = True    # signal to timeoutcheck
bufferlock = threading.Lock()
# Interactive regex matches for
# - prompt (asd# ) (all)
# - question ([yes]) (cisco)
# - more (-more-) (cisco,juniper)
# - restore coloring (\x1b[m) (linux)
# possible chars: "\):>#$/- "
INTERACT = re.compile(r"(?i)^("  # START of whole line matches
                    "[^* ]+([\]\>\#\$][: ]?)(.*)"  # prompt
                    "| ?<?-+ ?\(?more(?: [0-9]{1,2}%)?\)? ?-+>? ?([\b ]+)?"  # more (\b can be at the end when excessive enters are pressed
                    "|\x1b\[m"                     # color escape sequence
                    "|username: ?"
                    "|password: ?"
                    ")$"                           # END of whole line match
                    "|\]:? ?$"                     # probably question (reload? [yes])
                    , flags=re.S)


def timeoutcheck(maxwait=1.0):
    global bufferlock, debug, timeout, maxtimeout, buffer
    global RUNNING, WORKING

    timeout = time.time()
    while RUNNING:
        time.sleep(0.33)  # time clicks we run checks
        if WORKING:  # ifilter is working, do not send anything
            continue
        now = time.time()
        # Check if there was user input in the specified time range
        if maxtimeout > 0 and (now - timeout) >= maxtimeout:
            preventtimeout()       # send something to prevent timeout on device
            timeout = time.time()    # reset timeout
        # Check if there is some output stuck at buffer we should print out
        # (to mitigate unresponsiveness)
        if (now - timeout) > maxwait:
            try:
                bufferlock.acquire()
                if len(buffer) > 0:  # send out buffer
                    if debug >= 1: print("\r\n\033[38;5;208mTOB-", repr(buffer), "\033[0m\r\n")  # DEBUG
                    sys.stdout.write(colorize(buffer))
                    sys.stdout.flush()
                    buffer = ""
                    timeout = time.time()
                bufferlock.release()
            except threading.ThreadError as e:
                if debug>=1: print("\r\n\033[38;5;208mTERR-%s\033[0m\r\n" % e)  # DEBUG
                pass



def sigwinch_passthrough(sig, data):
    global conn

    rows, cols = getTerminalSize()
    conn.setwinsize(rows, cols)


def preventtimeout():
    global conn, prevents, maxprevents

    prevents += 1
    if maxprevents <= 0 or prevents <= maxprevents:
        conn.send("\x0C")


def printhelp(shortcuts):
    print(
"""q: quit program
p: pause coloring")
T: highlight regex (empty turns off)")

Shortcuts""")
    for (key, value) in shortcuts:
        print("%s: \"%s\"" % (key.upper(), value.strip(r'"')))



def colorize(text, only_effect=[]):
    # text       : input string to colorize
    # only_effect: select specific regex group(with specified effect) to work with
    global effects, cmap, conn, timeoutact, debug
    colortext = ""
    if debug >= 2: start = timeit.default_timer()
    for line in text.splitlines(True):
        cmap_counter = 0
        if debug >= 2: print("\r\n\033[38;5;208mC-", repr(line), "\033[0m\r\n")  # DEBUG
        if debug >= 3: print("\r\n\033[38;5;208mCCM-", repr(cmap), "\033[0m\r\n")  # DEBUG
        for i in cmap:
            cmap_counter += 1
            matcher = False
            # try:
            matcher = i[0]  # is matcher?
            prio = i[1]     # priority
            effect = i[2]   # invokes other rules
            dep = i[3]      # dependency on effect
            reg = i[4]      # regexp match string
            rep = i[5]      # replacement string
            option = i[6]   # match options (continue,break,clear)
            cdebug = i[7]   # debug
            name = i[8]     # regex name

            if only_effect != [] and effect not in only_effect:  # check if only specified regexes should be used
                continue  # move on to the next regex
            if len(dep) > 0 and dep not in effects:  # we don't meet our dependency
                continue  # move on to the next regex
            if cdebug > 0:
                print("\r\n\033[38;5;208mD-", name, repr(origline), repr(line), repr(effects), "\033[0m\r\n")  # debug
            if matcher:
                if reg.search(line):
                    if debug >= 2: print("\r\n\033[38;5;208mCM-", name, "\033[0m\r\n")  # debug
                    effects.add(effect)
                if 'timeoutwarn' in effects and timeoutact:
                    effects.remove('timeoutwarn')
                    preventtimeout()
                continue

            origline = line
            if option == 2:  # need to cleanup existing coloring (CLEAR)
                backupline = line
                origline = re.sub('\x1b[^m]*m', '', line)
                if debug >= 3: print("\r\n\033[38;5;208mCCL-", origline, "\033[0m\r\n")  # debug
            line = reg.sub(rep, origline)
            if line != origline:  # we have a match
                if debug >= 2: print("\r\n\033[38;5;208mCM-", name, "\033[0m\r\n")  # debug
                if len(effect) > 0:  # we have an effect
                    effects.add(effect)
                if 'prompt' in effects:  # prompt eliminates all effects
                    effects = set()
                if option > 0:  # non-zero means non-final match
                    break
            elif option == 2:  # need to restore existing coloring as there was no match (by CLEAR)
                line = backupline
        if debug >= 2: print("\033[38;5;208mCC-%d\033[0m" % cmap_counter)  # DEBUG
        colortext += line
    if debug >= 2: print("\r\n\033[38;5;208mCT-%f\033[0m\r\n" % (timeit.default_timer() - start))  # DEBUG
    return colortext


def ifilter(input):
    global is_break, timeout, prevents

    is_break = input == b'\x1c'
    if not is_break: timeout = time.time(); prevents = 0
    return input


def ofilter(input):
    global buffer
    global pause  # coloring must be paused
    global lastline
    global debug
    global bufferlock
    global WORKING

    # Coloring is paused by escape character
    if pause:
        return input

    input = input.decode()
    bufferlock.acquire()  # we got input, have to access buffer exclusively
    WORKING = True
    try:
        # If not ending with linefeed we are interacting or buffering
        if not (input[-1] == "\r" or input[-1] == "\n"):
            # collect the input into buffer
            buffer += input
            if debug: print("\r\n\033[38;5;208mI-", repr(input), "\033[0m\r\n")  # DEBUG
            lastline = buffer.splitlines(True)[-1]
            if debug: print("\r\n\033[38;5;208mL-", repr(lastline), "\033[0m\r\n")  # DEBUG
            if debug: print("\r\n\033[38;5;208mB-", repr(buffer), "\033[0m\r\n")  # DEBUG
            # special characters. e.g. moving cursor
            # if input not starts with \b then it's sg like more or anything device wants to hide.
            # regular text can follow which we want to colorize
            if ("\a" in lastline or "\b" in lastline) and (lastline[0] != "\a" and lastline[0] != "\b") and input == lastline:
                bufout = buffer
                buffer = ""
                return colorize(bufout, ["prompt"]).encode()
            if INTERACT.search(lastline):  # prompt or question at the end
                bufout = buffer
                buffer = ""
                return colorize(bufout).encode()

            if len(buffer) < 100:  # interactive or end of large chunk
                bufout = buffer
                if "\r" in input or "\n" in input:  # multiline input, not interactive
                    bufout = "".join(buffer.splitlines(True)[:-1])  # all buffer except last line
                    buffer = lastline  # delete printed text. last line remains in buffer
                    return colorize(bufout).encode()
                elif buffer == input:  # interactive
                    buffer = ""
                    return colorize(bufout, ["prompt", "ping"]).encode() # colorize only short stuff (up key,ping)
                else:             # need to collect more output
                    return b""
            else:  # large data. we need to print until last line which goes into buffer
                bufout = "".join(buffer.splitlines(True)[:-1])  # all buffer except last line
                if bufout == "":  # only one line was in buffer
                    return b""
                else:
                    buffer = lastline  # delete printed text. last line remains in buffer
                    return colorize(bufout).encode()
        else:
            if debug: print("\r\n\033[38;5;208mNI-", repr(input), "\033[0m\r\n")  # DEBUG
            # Got linefeed, dump buffer
            bufout = buffer + input
            buffer = ""
            return colorize(bufout).encode()
    finally:
        bufferlock.release()
        WORKING = False


def merge_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def main():
    global conn, ct, cmap, pause, timeoutact, terminal, buffer, lastline, debug
    global is_break
    global maxtimeout, maxprevents
    global RUNNING
    highlight = ""

    default_config = {
                    'colortable': r'dbg_net',
                    'terminal': r'securecrt',
                    'regex': r'all',
                    'timeoutact': r'true',
                    'debug': r'0',
                    'maxtimeout': r'0',
                    'maxprevents': r'0',
                    'maxwait': r'1.0',
                    'update_caption': r'false',
                    'default_caption': os.environ['HOSTNAME'],
                    'F1': r'show ip interface brief | e unassign\r',
                    'F2': r'show ip bgp sum\r',
                    'F3': r'show ip bgp vpnv4 all sum\r',
                    'F4': r'"ping "',  # space requires quoting
                    'F5': r'',
                    'F6': r'',
                    'F7': r'',
                    'F8': r'',
                    'F9': r'',
                    'F10': r'',
                    'F11': r'',
                    'F12': r'',
                    'SF1': r'show interface terse | match inet\r',
                    'SF2': r'show bgp summary\r',
                    'SF3': r'',
                    'SF4': r'',
                    'SF5': r'',
                    'SF6': r'',
                    'SF7': r'',
                    'SF8': r'', }
    try:
        config = ConfigParser.SafeConfigParser(default_config, allow_no_value=True)
    except TypeError:
        config = ConfigParser.SafeConfigParser(default_config)  # keep compatibility with pre2.7
    starttime = time.time()
    config.add_section('clicol')
    config.read(['/etc/clicol.cfg', 'clicol.cfg', os.path.expanduser('~/clicol.cfg')])
    terminal = config.get('clicol', 'terminal')

    shortcuts = [o_v for o_v in config.items('clicol') if re.match(r'[fF][0-9][0-9]?', o_v[0]) and o_v[1]]  # read existing shortcuts
    shortcuts_shift = [o_v1 for o_v1 in config.items('clicol') if re.match(r'[sS][fF][0-9][0-9]?', o_v1[0]) and o_v1[1]]  # read existing shortcuts+shift
    shortcuts.sort(key=lambda o_v2: int(o_v2[0].lstrip("SFsf")))  # sort by function key
    shortcuts_shift.sort(key=lambda o_v3: int(o_v3[0].lstrip("SFsf")))  # sort by function key
    shortcuts.extend(shortcuts_shift)

    cct = config.get('clicol', 'colortable')
    timeoutact = config.getboolean('clicol', 'timeoutact')
    update_caption = config.getboolean('clicol', 'update_caption')
    default_caption = config.get('clicol', 'default_caption')
    maxtimeout = config.getint('clicol', 'maxtimeout')
    maxprevents = config.getint('clicol', 'maxprevents')
    debug = config.getint('clicol', 'debug')

    colors = ConfigParser.SafeConfigParser()
    colors.add_section('colors')
    colors.read([resource_filename(__name__, 'ini/colors_' + terminal + '.ini'), os.path.expanduser('~/clicol_customcolors.ini')])

    ctfile = ConfigParser.SafeConfigParser(dict(colors.items('colors')))
    del colors
    ctfile.add_section('colortable')
    if cct == "dbg_net" or cct == "lbg_net":
        ctfile.read([resource_filename(__name__, 'ini/ct_' + cct + '.ini'), os.path.expanduser('~/clicol_customct.ini')])
    else:
        print("No such colortable: " + cct)
        exit(1)

    default_cmap = {
             'matcher': '0',
             'priority': '100',
             'effect': '',
             'dependency': '',
             'regex': '',
             'replacement': '',
             'options': '1',  # CONTINUE=0,BREAK=1,CLEAR=2 as below
             'debug': '0',
             'disabled': '0',
             'BOL': '(^(?: ?<?-+ ?\(?[mM][oO][rR][eE](?: [0-9]{1,2}%%)?\)? ?-+>? ?)?(?:[\b ]+)|^)',
             'BOS': ("(?:" + dict(ctfile.items('colortable'))['default'] + r'|\b)').replace(r'[', '\['),
             'CONTINUE': '0',
             'BREAK': '1',
             'CLEAR': '2',
             }
    cmaps = ConfigParser.SafeConfigParser(merge_dicts(dict(ctfile.items('colortable')), default_cmap))
    regex = config.get('clicol', 'regex')
    if regex == "all":
        regex = '.*'
    try:
        if len(sys.argv) > 1 and sys.argv[1] == '--c':  # called with specified colormap regex
            regex = sys.argv[2]
            del sys.argv[1]  # remove --c from args
            del sys.argv[1]  # remove colormap regex string from args
    except:  # index error, wrong call
        cmd = 'error'
    for cm in ["common", "cisco", "juniper"]:
        cmaps.read(resource_filename(__name__, 'ini/cm_' + cm + '.ini'))
    cmaps.read([os.path.expanduser('~/clicol_customcmap.ini')])
    for cmap_i in cmaps.sections():
        c = dict(cmaps.items(cmap_i))
        if re.match(regex, cmap_i):  # configured rules only
            if debug >= 3: print(repr([c['matcher'], c['priority'], c['effect'], c['dependency'], c['regex'], c['replacement'], c['options'], c['debug']]))
            if bool(int(c['disabled']) < 1):
                cmap.append([bool(int(c['matcher']) > 0), int(c['priority']), c['effect'], c['dependency'], re.compile(c['regex']), c['replacement'], int(c['options']), int(c['debug']), cmap_i])
    cmap.sort(key=lambda match: match[1])  # sort colormap based on priority

    # Check how we were called
    # valid options: clicol-telnet, clicol-ssh, clicol-test
    cmd = str(os.path.basename(sys.argv[0])).replace('clicol-', '');

    if cmd == 'test' and len(sys.argv) > 1:
        # Print starttime:
        print("Starttime: %s s" % (round(time.time() - starttime, 3)))
        # Sanity check on colormaps
        cmbuf = list()
        for cm in cmap:
            # search for duplicate patterns
            if cm[4] in cmbuf:
                print("Duplicate pattern:" + repr(cm))
            else:
                cmbuf.append(cm[4])

        if len(sys.argv) > 1:
            for test in filter(lambda x: re.match(sys.argv[1], x) and re.match(regex, x), cmaps.sections()):
                test_d = dict(cmaps.items(test))
                try:
                    # search for dirty patterns
                    match_in_regex = re.findall(r'(?<!\\)\((?!\?)', test_d['regex'].replace(r'%(BOS)s', ''))
                    match_in_replace = re.findall(r'(?<!\\)\\[0-9](?![0-9])', test_d['replacement'])

                    print("%s:%s" % (test, ofilter(('%s\n' % test_d['example'].replace('\'', '')).encode()).decode()))
                    if len(match_in_regex) != len(match_in_replace):
                        print("Warning: match group numbers are not equal! (%s/%s)" % (match_in_regex, match_in_replace))
                        test_d['debug'] = "1"
                    if test_d['debug'] == "1":
                        print(repr(test_d['regex']))
                        print(repr(test_d['replacement']))

                except:
                    pass
    elif cmd == 'file' and len(sys.argv) > 1:
        try:
            f = open(sys.argv[1], 'r')
        except:
            print("Error opening " + sys.argv[1])
            raise
        for line in f:
            print(ofilter(line.replace("\n", "\r\n").decode('string_escape')), end='')  # convert to CRLF to support files created in linux
        f.close()
    elif cmd == 'telnet' or cmd == 'ssh' or (cmd == 'cmd' and len(sys.argv) > 1):
        try:
            args = sys.argv[1:]
            if cmd == 'cmd':
                cmd = sys.argv[1]
                args = sys.argv[2:]
            skip = False
            if update_caption and (cmd == 'telnet' or cmd == 'ssh'):  # only update on telnet/ssh
                for arg in args:
                    if skip:
                        skip = False
                        continue
                    if re.match("-[46AaCfGgKkMNnqsTtVvXxYy]", arg):
                        continue
                    if re.match("-\w+", arg):
                        skip = True
                        continue
                    m = re.match("(?:\w+@)?([0-9a-zA-Z_.-]+)", arg)
                    # Print caption update code:
                    print("\033]2;%s\007" % m.group(1), end = '')
                    break
            conn = pexpect.spawn(cmd, args, timeout=1)
            # Set signal handler for window resizing
            signal.signal(signal.SIGWINCH, sigwinch_passthrough)
            # Set initial terminal size
            rows, cols = getTerminalSize()
            conn.setwinsize(rows, cols)
        except Exception as e:
            if cmd != 'telnet' and cmd != 'ssh':
                print("Error starting %s" % cmd)
                return
            else:
                print("Unknown error %s" % e)
                # Restore caption
                if update_caption:
                    # Print caption update code:
                    print("\033]2;%s\007" % default_caption, end = '')
                return
        try:
            # Start timeoutcheck to check timeout or string stuck in buffer
            tc = threading.Thread(target=timeoutcheck, args=(config.getfloat("clicol", "maxwait"),))
            tc.daemon = True
            tc.start()
            while conn.isalive():
                # esc code table: http://jkorpela.fi/chars/c0.html
                #\x1c = CTRL-\
                conn.interact(escape_character='\x1c', output_filter=ofilter, input_filter=ifilter)
                if is_break:
                    is_break = False
                    print("\r" + " " * 100 + "\rCLICOL: q:quit,p:pause,T:highlight,F1-12,SF1-8:shortcuts,h-help", end = '')
                    command = getCommand()
                    if command == "D":
                        debug += 1
                        if debug > 2:
                            debug = 0
                    if command == "p":
                        pause = 1 - pause
                    if command == "q":
                        print()
                        conn.close()
                        break
                    if command == "T":
                        highlight = getRegex()
                        cmap_highlight = [False, 0, "", "", highlight, dict(ctfile.items('colortable'))['highlight'] + r"\1" + dict(ctfile.items('colortable'))['default'], 0, 0, 'user_highlight']
                        if highlight == "":
                            if cmap[0][8] == 'user_highlight':  # If we have highlight regex, we remove it on user request
                                del cmap[0]
                        elif cmap[0][8] == 'user_highlight':
                            cmap[0] = cmap_highlight
                        else:
                            cmap.insert(0, cmap_highlight)
                    if command == "h":
                        printhelp(shortcuts)

                    print("\r" + " " * 100 + "\r" + colorize(lastline, "prompt"), end = '')  # restore last line/prompt

                    if command is not None:
                        for (key, value) in shortcuts:
                            if command.upper() == key.upper():
                                conn.send(value.encode().decode('unicode_escape').strip(r'"'))  # decode to have CRLF as it is and remove ""
                                break
        except OSError:
            conn.close()
        except Exception as e:
            if debug:
                import traceback
                print(traceback.format_exc())  # DEBUG
            print(e)
            print("Error while running " + cmd + " " + " ".join(args))

        # Restore caption
        if update_caption and (cmd == 'telnet' or cmd == 'ssh'):
            # Print caption update code:
            print("\033]2;%s\007" % default_caption, end = '')
        # Stop timeoutcheck thread and exit
        RUNNING = False
        tc.join()
        if len(buffer) > 0: print(colorize(buffer), end = '')  # print remaining buffer
    else:
        print("CLICOL - CLI colorizer and more... Version %s" % __version__)
        print("""
Usage: clicol-{telnet|ssh} [--c {colormap}] [args]
Usage: clicol-file         [--c {colormap}] {inputfile}
Usage: clicol-cmd          [--c {colormap}] {command} [args]
Usage: clicol-test         {colormap regex name (e.g.: '.*' or 'cisco_if|juniper_if')}

Usage while in session
Press break key CTRL-\\
""")
        printhelp(shortcuts)
        print(r"""
Copyright (C) 2019 Viktor Kertesz
This program comes with ABSOLUTELY NO WARRANTY
This is free software, and you are welcome to redistribute it""")


# END OF PROGRAM
if __name__ == "__main__":
    main()
