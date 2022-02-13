from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    c: int=0

def cuadrante(xpoint,ypoint):
    if (xpoint>0 and ypoint>0):
        c=1
        return c
    elif (xpoint<0 and ypoint>0):
        c=2
        return c
    elif (xpoint<0 and ypoint<0):
        c=3
        return c
    elif (xpoint>0 and ypoint<0):
        c=4
        return c
    else:
        c=0
        return c


def main():
    xpoint=float(input('Ingrese la coordenada en x del punto\n'))
    ypoint=float(input('Ingrese la coordenada en y del punto\n'))
    c=cuadrante(xpoint, ypoint)
    point1=Point(xpoint,ypoint,c)
    print(f'Coordenada en X:{point1.x}\nCoordenada en Y:{point1.y}\nCuadrante:{point1.c}\n')

main()
