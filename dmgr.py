#!/usr/bin/env python
import getopt, sys

class Action():
    def option(self, args):
        if args in ("-h", "--help"):
             f = open("dat/helpfile.txt", "r")
             print(f.read())
             f.close()
        elif args in ("-v", "--version"):
            print("dmgr v0.1 pre-alpha")
        elif args in ("-i", "--install"):
            print("placeholder for install")
        elif args in ("-s", "--size"):
            print("placeholder for size")
        elif args in ("-f", "--free"):
            print("placeholder for free")
        elif args in ("-p", "--partition"):
            print("placeholder for partition")
        elif args in ("-c", "--copy"):
            print("placeholder for copy")
        elif args in ("-d", "--delete"):
            print("placeholder for delete")
        elif args in ("-x", "--cut"):
            print("placeholder for cut")
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
