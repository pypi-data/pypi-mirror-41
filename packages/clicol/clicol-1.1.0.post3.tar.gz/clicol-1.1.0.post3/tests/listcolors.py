#!/usr/bin/python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clicol import colors_putty

colors_putty.print_colortable()
colors_putty.print_allcolors()
