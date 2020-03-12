#!/usr/bin/python3
## -*- coding: utf-8 -*-

# Module einbinden
import os       # Filesystem Operationen
import re       # Regular Expressions
import csv      # CSV DictReader

# Anwendungsdaten
AppData = {
    "ID": "2020031123",
    "TYPE": "Application",
    "NAME": "CSV Parser",
    "VERSION": "Version 0.1",
    "INFILE": "../data/people.csv"
}

# Statistikdaten (weitere Felder werden dynamisch erzeugt)
StatisticData = {
    "NAME": "CSV-Statistik-Objekt"
}

##########################################################################
# Application Class (Dialog Application)

class Application:

    def __init__(self, data):
        self.data = data

    def main(self):
        # Anzeigen des Programmnamens
        print("{0:s}, {1:s} ({2:s})".format(self.data["NAME"], self.data["VERSION"], self.data["ID"]))

    def dump(self, filename = ""):
        load_file = self.data["INFILE"]
        if filename != "":
            load_file = filename
        print("Load File: {0}\n".format(load_file))

        # Öffne eine CSV-Datei
        with open(load_file) as csvfile:
            # Erzeuge den CSV-Reader
            reader = csv.DictReader(csvfile)
            count = 0
            # Lade die CSF-Datei zeileweise 
            for record in reader:
                # Zerlege die Zeile in Spaltenname und Wert
                for name,value in record.items():
                    # Hole Schlüsselfeld 
                    if name == "employeenumber":
                        count+=1
                        print("[{}]:".format(value))
                        print("count={0}".format(count))
                    print("{0}={1} ".format(name,value))      # without newline: end = " "
                    try:
                        # hole vorhandenes Statistikfeld oder (Aunnahmeverletzung wenn nicht vorhanden)
                        stdata = StatisticData[name]
                    except KeyError:
                        # erzeuge pro Spalte ein Statistikfeld (initiales anlegen); unterscheide Typ String von Bool
                        if name == 'active':
                            StatisticData[name] = {'EMPTY':0, 'NOTEMPTY':0, 'ACTIVE': 0, 'INACTIVE': 0}     # Bool
                        else:
                            StatisticData[name] = {'EMPTY':0, 'NOTEMPTY':0}     # String (Standardtyp)

                    # Prüfe und zähle hoch (alle Typen)
                    stdata = StatisticData[name]
                    if value == "":
                        stdata['EMPTY'] = stdata['EMPTY'] + 1
                    if value != "":
                        stdata['NOTEMPTY'] = stdata['NOTEMPTY'] + 1
                    
                    # bei bool-Typen: prüfe auf aktiv/inaktiv
                    if name == 'active':
                        if int(value) > 0:
                            stdata['ACTIVE'] = stdata['ACTIVE'] + 1
                        else:
                            stdata['INACTIVE'] = stdata['INACTIVE'] + 1

                # Eine Leerzeile pro Datenobjekt
                print()

        print(StatisticData)

        print("\nCompleted: {} items.".format(count))
        return 0
        
##########################################################################
# MAIN Procedure

if __name__ == "__main__":
    App = Application(AppData)
    App.main()
    App.dump()