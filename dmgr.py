#!/usr/bin/env python
import getopt, sys, subprocess as sp
from pathlip import Path

class Action():
    def option(self, args):
        if args in ("-h", "--help"):
             f = open("dat/helpfile.txt", "r")
             print(f.read())
             f.close()
        elif args in ("-v", "--version"):
            print("dmgr v0.1 pre-alpha")
        elif args in ("-i", "--install"):
            if == 'deb':
                sp.call(["sudo", "dpkg", "-i", src_file])
            elif == 'rpm':
                print("if this won't work, try\n\nsudo apt install rpm\n\nand try it again then")
                sp.call(["sudo", "rpm", "-i", src_file])
            print("placeholder for install")
        elif args in ("-s", "--size"):
            print("The file size is: " + str(Path(src_file).stat().st_size))
        elif args in ("-f", "--free"):
            print("placeholder for free")
        elif args in ("-p", "--partition"):
            print("placeholder for partition")
        elif args in ("-c", "--copy"):
            sp.call(["sudo", "cp", src_file, dest_file])
            print("Already knew that the default command for that is:\ncp [src_file] [dest_file]")
        elif args in ("-d", "--delete"):
            sp.call(["sudo", "rm", "-rf", src_file])
            print("Already knew that the default command for that is:\nrm -rf [src_file]")
        elif args in ("-x", "--cut"):
            print("placeholder for cut")
            print("Already knew that the default command for that is:\ncp [src_file] [dest_file] && rm [src_file]")
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
