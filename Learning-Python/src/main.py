#!/usr/bin/python3
## -*- coding: utf-8 -*-

import learn_math

AppData = {
    'TITLE': 'Learning-Python, Python Samples and Templates',
    'DESC': 'A simple python project template sample.',
    'AUTHOR': 'naturestone',
    'VERSION': '1.0.1'
}

##########################################################################
# TEST Procedure

def test():
    print("Modul ist running.")

##########################################################################
# MAIN Procedure

def main():
    # Standardausgabe
    print("\n{0}\nVersion: {2}\nAutor: {1}\n".format(AppData['TITLE'], AppData['AUTHOR'], AppData['VERSION']))
    # Eingabe der Funktion / des Bausteins, der ausgeführt werden soll
    load_func = input("Running module: ")
    try:
        type_modul = type(load_func)
        print('Loading: {} is from type {}\n'.format(load_func, type_modul))
        # Prüfe, ob eingegebener Name vom Typ 'function' ist type(test())
        if (type_modul == type(test())):
            # Ausführen der Funktion und zurück
            return load_func()
    except:
        # Fehlerhandling
        print('Module not found.')
        exit(2)
    finally:
        print('Complete.')
    

##########################################################################
# MAIN Program

if __name__ == "__main__":
    main()