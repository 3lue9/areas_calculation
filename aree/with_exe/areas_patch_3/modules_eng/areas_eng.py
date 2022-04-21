def area_triangolo():
    b=float(input("how much is the base -> "))
    h=float(input("how much does the height measure -> "))
    A=b*h/2
    print(A)

def area_quadrato():
    b=float(input("how much does the side fit -> "))
    B=b*b
    print(B)

def area_rettangolo():
    b=float(input("how much is the base -> "))
    h=float(input("how much does the height measure -> "))
    C=b*h
    print(C) 

def area_cerchio():
    from math import pi
    pi_greco = pi
    raggio = float(input("how much does the radius measure -> "))
    D = (raggio*raggio)*pi_greco
    print(D)

def area_trapezio():
    base_min=float(input("how much is the base minor -> "))
    base_mag=float(input("how much is the base greater -> "))
    h=float(input("how much does the height measure -> "))    

    E=base_min+base_mag
    F = E*h
    G=F/2
    print(G) 