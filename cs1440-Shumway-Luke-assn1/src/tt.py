#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage

import sys


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    if sys.argv[1] == "cat":
        if not len(sys.argv) > 2:
            usage("Too few arguments", "cat")
            sys.exit(1)
        else:
            cat(sys.argv[2:])
    elif sys.argv[1] == "tac":
        if not len(sys.argv) > 2:
            usage("Too few arguments", "tac")
            sys.exit(1)
        else:
            tac(sys.argv[2:])
    elif sys.argv[1] == "cut":
        if sys.argv[2] == "-f" and sys.argv[3].isdigit():
            fields = sys.argv[3].split(",")
            cut(fields=fields, files=sys.argv[4:])
        elif sys.argv[2] == "-f" and (not len(sys.argv) > 3 or not sys.argv[3].isdigit()):
            usage("A comma-separated field specification is required", "cut")
            sys.exit(1)
        elif len(sys.argv) > 2:
            cut(files=sys.argv[2:])
        else:
            usage("Too few arguments", "cut")
            sys.exit(1)
    elif sys.argv[1] == "paste":
        if not len(sys.argv) > 2:
            usage("Too few arguments", "paste")
            sys.exit(1)
        else:
            paste(sys.argv[2:])
    elif sys.argv[1] == "grep":
        if sys.argv[2] == "-v" and len(sys.argv) > 4:
            grep(match=False, pattern=sys.argv[3], files=sys.argv[4:])
        elif len(sys.argv) > 3:
            grep(match=True, pattern=sys.argv[2], files=sys.argv[3:])
        else:
            usage("Please provide a pattern and at least one filename", "grep")
            sys.exit(1)
    elif sys.argv[1] == "head":
        if sys.argv[2] == "-n" and sys.argv[3].isdigit() and len(sys.argv) > 4:
            head(lines=sys.argv[3], files=sys.argv[4:])
        elif sys.argv[2] == "-n" and (not sys.argv[3].isdigit() or not len(sys.argv) > 2):
            usage("Number of lines is required", "head")
            sys.exit(1)
        elif len(sys.argv) > 2:
            head(files=sys.argv[2:])
        else:
            usage("Too few arguments", "head")
            sys.exit(1)
    elif sys.argv[1] == "tail":
        if sys.argv[2] == "-n" and sys.argv[3].isdigit() and len(sys.argv) > 4:
            tail(lines=sys.argv[3], files=sys.argv[4:])
        elif sys.argv[2] == "-n" and (not sys.argv[3].isdigit() or not len(sys.argv) > 2):
            usage("Number of lines is required", "tail")
            sys.exit(1)
        elif len(sys.argv) > 2:
            tail(files=sys.argv[2:])
        else:
            usage("Too few arguments", "tail")
            sys.exit(1)
    elif sys.argv[1] == "sort":
        if not len(sys.argv) > 2:
            usage("Too few arguments", "sort")
            sys.exit(1)
        else:
            sort(sys.argv[2:])
    elif sys.argv[1] == "wc":
        if not len(sys.argv) > 2:
            usage("Too few arguments", "wc")
            sys.exit(1)
        else:
            wc(sys.argv[2:])


