#!/usr/bin/python3
## -*- coding: utf-8 -*-

AppData = {
    'TITLE': 'MyProject Python Sample Project',
    'DESC': 'A simple python project template sample.',
    'AUTHOR': 'Sample Project',
    'VERSION': '1.0.1'
}

##########################################################################
# MAIN Procedure

def main():
    print("\n{0}\nVersion: {2}\nAutor: {1}\n".format(AppData['TITLE'], AppData['AUTHOR'], AppData['VERSION']))

##########################################################################
# MAIN Program

if __name__ == "__main__":
    main()