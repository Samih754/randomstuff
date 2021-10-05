import math

def defz():
    xa = float(input("x =: "))
    ya = float(input("y =: "))
    xb = float(input("x' =: "))
    yb  =float(input("y' =: "))

    g = (xa * yb)-(xb * ya)
    print(g)

def vecteur():
    xa = float(input("x =: "))
    ya = float(input("y =: "))
    xb = float(input("x' =: "))
    yb  =float(input("y' =: "))

    a = xb - xa
    b = yb - ya

    print(a,";",b)

def annoying():
    xAB = float(input("xAB = ?: "))
    YAB = float(input("yAB = ?: "))
    ax = float(input("ax = ?: "))
    ay  = float(input("ay = ?: "))

    bx = xAB + ax
    by = YAB + ay

    print(bx,";", by)

def middle():
    xa = float(input("x =: "))
    ya = float(input("y =: "))
    xb = float(input("x' =: "))
    yb  =float(input("y' =: "))

    x = (xa + xb) / 2
    y = (ya + yb) / 2

    print(x,";",y)

def norme():
    xa = float(input("x =: "))
    ya = float(input("y =: "))
    xb = float(input("x' =: "))
    yb  =float(input("y' =: "))

    a = (xb - xa)
    b = (yb - ya)
    c = a + b
    d = c ** 0.5
    print(d)


a = input("1 for the fonction de def; 2 for calcule d'un vecteur, 3 for AB = A = what is B, 4 for millieu; 5 for norme ")

if a == ("1"):
    defz()
elif a == ("2"):
    vecteur()
elif a == ("3"):
    annoying()
elif a == ("4"):
    middle()
elif a == ("5"):
    norme()
