#!/usr/bin/env python
import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        print("Try 'dmgr -h' for more information")
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            help()
            sys.exit()
        else:
            assert False, "unhandled option"
            sys.exit()

def help():
    print("placeholder")

if _name_ == "_main_":
    main()
