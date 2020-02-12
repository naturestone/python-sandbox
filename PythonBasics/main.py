#!/usr/bin/python
## -*- coding: utf-8 -*-

"""
Python Basics. 
Autor: lf
"""

# Programmtitel für Anzeige
PROGRAM_TITLE='Python Basics, Version 20.02'

##########################################################################
# Ausgaben und Eingaben -  print/input

def dialogTest():
    print(PROGRAM_TITLE, "\n")          # Ausgabe des Programmtitels + Leerzeile
    buf = input("  Code: ")             # Tastatureingabe einlesen
    print("  In: {:4}".format(buf))     # Eingabeaufforderung und Anzeige
    print("\nFertig.")

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
        print(i)
    for i in listOfColors:
        print(i)
    for i in range(10):        # Zählschleife (loops)
        if i == 4:             # Bedingung prüfen und... 
            continue           #  weiter mit nächstem Schritt
        if i == 5:             # Bedingung prüfen und...
            break              #  vorzeitiger Abbruch der Schleife
    for p in dictOfPeople:     # Datensätze aus Liste holen
        for n,a in p.items():  # Datensatz holen und aufschlüsseln
            print(n,a);        # Datensatz ausgeben
    i = ""                     # setze Schleifenvariable für Vorbedingung
    while i == 'q':            # wiederhole solange bis 'q' eingegeben wird
        i = input(" In: ")     # hole Eingabe
        if i == 'c':           # Bedingung prüfen und ...
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

##########################################################################
# MAIN Procedure

def main():
    dialogTest()
    exit(0)

if __name__ == "__main__":
    main()
