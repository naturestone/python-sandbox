#!/usr/bin/python3
## -*- coding: utf-8 -*-

DESCRIPTION = """
***
** Python Basics. 
** Autor: lf
**
** Darstellung der wichtigsten Datentypen und Funktionen für den Einstieg in Python. 
** Die Beispiele hier sind nur zur Demonstration. Durch Eingabe von help oder printTest
** können die Funktionen aufgerufen werden.
**
**    python3 main.py
** 
"""

# Programmtitel für Anzeige
PROGRAM_TITLE="Python Basics, Version 20.02"
PYTHON_BOOK='https://py-tutorial-de.readthedocs.io/de/python-3.3/'

##########################################################################
# Ausgaben formatieren print,String.format()

text = "Name {0} Age {1} Gender {2}\n"      # String template
data = ["Smith", "35", "male"]              # List 
table = {"ID": 123, "ROLE": "Master"}       # Dictionary

def printTest():
    print('Prints the values to a stream, or to sys.stdout by default')
    print("Return a formatted version of formtext, using substitutions ")
    print(text.format(*data))                        # expands data array
    print("|{ID:10d}|{ROLE:>10s}|".format(**table))  # Schlüsselwortargumente
    print("|{0:10.3f}|{0:5.0f}|".format(3.1415))     # formatiere Zahlen
    

##########################################################################
# Bedingungen - if/elif/else

def conditionTest(x = 2):
    c = x == 2                  # Gleichheit
    c = x != 2                  # Ungleichheit
    c = x <= 2                  # kleiner gleich
    c = x >= 2                  # größer gleich
    c = x >= 1 and x < 3        # größer gleich 1 und kleiner 3
    if x == 2:                  # Prüfe ob x gleich 2 ist...
        print("Zwei")           #   dann gebe aus...
    elif x == 3:                # sonst prüfe auf x == 3
        print("Drei")           #    dann gebe aus ...
    else:                       # sonst etwas anderes.
        print("Nicht zwei oder drei.")
    return True                 # Rückgabewert

##########################################################################
# Schleifen - for und while

listOfColors = ["red", "green", "yellow", "black", "white"]
dictOfPeople = [{"NAME":"Max", "AGE": 22}, {"NAME":"Lea", "AGE": 20}]

def loopTest():
    for i in range(10):
        print(i, end=" ")      # Trick: Zeilenvorschub unterdrücken mit end=
    for i in listOfColors:
        print(i,end=" ")
    for i in range(10):        # Zählschleife (loops)
        if i == 4:             # Bedingung prüfen und... 
            continue           #  weiter mit nächstem Schritt
        if i == 5:             # Bedingung prüfen und...
            break              #  vorzeitiger Abbruch der Schleife
    print()                    # nur Zeilenvorschub ausgeben
    for p in dictOfPeople:     # Datensätze aus Liste holen
        for n,a in p.items():  # Datensatz holen und aufschlüsseln
            print(n,a)         # Datensatz ausgeben
    i = 0                      # setze Schleifenvariable für Vorbedingung 
    while i < 10:              # wiederhole solange bis 'q' eingegeben wird
        i+=1                   # erhöhe um 1
        if i == 5:             # Bedingung prüfen und ...
            print(i)           #  und raus...
            break              #  vorzeitiger Abbruch der Schleife

##########################################################################
# Math

import math                 # Import module math

def mathTest(x=1.456, y=2.567):
    r = math.pi             # die Zahl PI
    r = math.sqrt(x)        # Return the square root of x. 
    r = math.floor(x)       # Return the largest integer <= x.
    r = math.ceil(x)        # Return the smallest integer >= x.
    r = math.pow(x,y)       # Return x**y (x to the power of y).
    r = math.log(x)         # Return the logarithm of x to the given base.
    r = math.log10(x)       # Return the logarithm of x to base 10.
    r = math.exp(x)         # Return e raised to the power of x.
    r = math.cos(x)         # Return the cosine of x (measured in radians).
    r = math.sin(x)         # Return the sine of x (measured in radians).
    r = math.radians(x)     # Convert angle x from degrees to radians.
    r = abs(x)              # Return the absolute value of the argument.
    # Demo-Ausgabe von Gleitkommazahlen (Floatingpoint Types: float, double)
    print ("PI={}".format(math.pi))
    print ("COS(x)={:.4f}".format(math.cos(x)))

##########################################################################
# Ausgaben und Eingaben -  print/input

def help():
    print (DESCRIPTION)                    # Ausgabe von DESCRIPTION

def dialogTest():
    print(PROGRAM_TITLE + "\n")           # Ausgabe des Programmtitels + Leerzeile
    buf = input("Name der Funktion: ")    # Tastatureingabe einlesen (py2: raw_input)
    cmd = buf + "()"                      # Funktionsaufruf für eval() bauen
    eval(cmd)                             # eval() führt Python Code aus
    print("OK.")

##########################################################################
# MAIN Procedure

def main():
    dialogTest()
    # printTest()
    exit(0)

if __name__ == "__main__":
    main()
