## -*- coding: utf-8 -*-

PI = 3.1415

def kreis_umfang(radius):
    return PI * radius

def learn_math():
    print("Mathetest: {}".format(kreis_umfang(5)))

if __name__ == "__main__":
    print("Modul", __name__, "ist nicht ausführbar!") 