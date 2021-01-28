# taken from http://hovnokod.cz/2744

def vporadi(x, y, z):
    if (x < y) and (x < z):
        if (y < z):
            print(x, y, z)
        else:
            print(x, z, y)
    if (y < x) and (y < z):
        if (x < z):
            print(y, x,z)
        else:
            print(y,z,x)
    if (z<y) and (z<x):
        if (y<x):
            print(z,y,x)
        else:
            print(z,x,y)
