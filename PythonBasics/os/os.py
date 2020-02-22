#!/usr/bin/python
## -*- coding: utf-8 -*-

DESCRIPTION="""
** Modul os
** 
** Zugriff auf Funktionen (posix-Standard) des Betriebssystems 
** 
"""

import os

##########################################################################
# os

def infoTest():
    print("OS.name:   {}".format( os.name ))
    print("OS.cwd:    {}".format( os.curdir ))
    print("OS.sep:    {}".format( os.sep ))

def unameTest():
    print("\nOS.uname:  {}".format( os.uname() ))       # uname-Abfrage
    print("{0}\n{1}\n{2}\n{3}".format( *os.uname() ))   # *args-Operator

##########################################################################
# help() und usage() 

def help():
    print(DESCRIPTION,END="")      # Trick: ,-Operator unterdrückt Zeilenvorschub

##########################################################################
# MAIN Procedure

def main():
    try:
        str = input("Command: ")    # python2: raw_input()
        cmd = str + "()"
        eval(cmd) 
        exit(1)
    except Exception:
        print("Unknown!")
    finally:
        print("\nOK.")

if __name__ == "__main__":
    main()
