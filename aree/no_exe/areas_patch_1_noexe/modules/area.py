def area_triangolo():
    b=float(input("quanto misura la base -> "))
    h=float(input("quanto misura l'altezza -> "))
    A=b*h/2
    print(A)

def area_quadrato():
    b=float(input("quanto misura il lato -> "))
    B=b*b
    print(B)

def area_rettangolo():
    b=float(input("quanto misura la base -> "))
    h=float(input("quanto misura l'altezza -> "))
    C=b*h
    print(C) 

def area_cerchio():
    from math import pi
    pi_greco = pi
    raggio = float(input("quanto misura il raggio -> "))
    D = (raggio*raggio)*pi_greco
    print(D)

def area_trapezio():
    base_min=float(input("quanto misura la base minore -> "))
    base_mag=float(input("quanto misura la base maggiore -> "))
    h=float(input("quanto misura l'altezza -> "))    

    E=base_min+base_mag
    F = E*h
    G=F/2
    print(G) 