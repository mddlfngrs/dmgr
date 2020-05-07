#!/usr/bin/env python
import getopt, sys

class Action():
    def option(self, args):
        print(str(args))
        if args in ("-h", "--help"):
            print("h")
        elif args in ("-v", "--version"):
            #act1.option()
            print("v")
        else:
            print("option " + args + " not recognized\nTry 'dmgr -h' for more information")
            sys.exit()

class Option():
    def main(self):
        act1 = Action()
        try:
            opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
        except getopt.GetoptError as err:
            print(str(err))
            print("Try 'dmgr -h' for more information")
            sys.exit()
        for o, a in opts:
            act1.option(o)

if __name__ == "__main__":
    opt1 = Option()
    opt1.main()
