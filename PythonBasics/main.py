#!/usr/bin/python
## -*- coding: utf-8 -*-

"""
Python Basics. 
Autor: lf
"""

##########################################################################
# Variablen

# Literal / Zeichenkette
PROGRAM_TITLE="Python Basics, Version 20.02"
PROGRAM_TITLE='Python Basics, Version 20.02'

# Liste oder Listenobjekt (Array)
FARBEN=["rot", "grün", "blau"]

# Dictionary (Hash)
PERSON={'VORNAME': 'Lisa', 'ALTER': 22, 'GESCHLECHT': 'w'}

#  List of Dictionary 
PERSONEN=[
    {'VORNAME': 'Lisa', 'ALTER': 22, 'GESCHLECHT': 'w'},
    {'VORNAME': 'Marco', 'ALTER': 17, 'GESCHLECHT': 'm'}
]

##########################################################################
# Funktion lineTest mit Zählerschleife for .. in range(n)
# n => Anzahl der Schleifendurchläufe
# z => Zeichen, die pro Schleifendurchlauf angehängt werden (Optional)

def linieTest(n, z="#"):
    buff="   "
    for i in range(n):
        buff+=z
    print(buff)

def blockTest(m, n, z="B"):
    for i in range(m):
        linieTest(n, z)

def listeHTest(colors):
    buff="   "
    for col in colors:
        buff+=col+"; "
    print(buff)

def listeTest(colors):
    for col in colors:
        print(col)

def dictionaryTest(dict):
    for attr, value in dict.items():
        attr+=":"
        print("   {:15} {}".format(attr, value))

def listOfDictionaryTest(liste):
    for pers in liste:
        dictionaryTest(pers)

##########################################################################
# Ausgaben und Eingaben

def dialogTest():
    print(PROGRAM_TITLE, "\n")          # Ausgabe des Programmtitels + Leerzeile
    buf = Input("  Code: ")             # Tastatureingabe einholen
    print("Eingabe: {:4}".format(buf))  # Eingabeaufforderung und Anzeige
    print("Fertig.")

##########################################################################
# Bedingungen

x = 2

def conditionTest():
    if True:
    if False:
    if x == 2:                  # Gleichheit
    if x != 2:                  # Ungleichheit
    if x <= 2:                  # kleiner gleich
    if x >= 2:                  # größer gleich
    if x >= 1 and x < 3:        # größer gleich 1 und kleiner 3
    if x == 2:                  # Prüfe ob x gleich 2 ist...
        print("Zwei")           #   dann gebe aus...
    elif x == 3:                # sonst prüfe auf x == 3
        print("Drei")           #    dann gebe aus ...
    else:                       # sonst etwas anderes.
        print("Nicht zwei oder drei.")
    return True                 # Rückgabewert
    
    

##########################################################################
# Schleifen

listOfColors = ["red", "green", "yellow", "black", "white"]

def loopTest():
    for i in range(10):
    for i in listOfColors:
        print(i)
    for i in range(10):        # Zählschleife (loops)
        if i == 4:             # Bedingung prüfen und... 
            continue           #  weiter mit nächstem Schritt
        if i == 5:             # Bedingung prüfen und...
            break              #  vorzeitiger Abbruch der Schleife

    i = ""                     # setze Schleifenvariable für Vorbedingung
    while i == 'q':            # wiederhole solange bis 'q' eingegeben wird
        i = input(" In: ")     # hole Eingabe
        if i == 'c':           # Bedingung prüfen und ...
            break              #  vorzeitiger Abbruch der Schleife

##########################################################################
# Math

import math                 # Import module math

x=1.456                     # define a float x
y=2.567                     # define a float y

def mathTest():
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
    # Programmtitel ausgeben
    print("{:s}\n".format(PROGRAM_TITLE))
    # Aufruf der Funktion lineTest() mit n=5
    # blockTest(8, 10, "L")
    # FARBEN.append(input("Farbe eingeben: "))
    # listeTest(FARBEN)
    # dictionaryTest(PERSON)
    # listOfDictionaryTest(PERSONEN)
    # Exit Code setzen
    mathTest();
    exit(0)

if __name__ == "__main__":
    main()
