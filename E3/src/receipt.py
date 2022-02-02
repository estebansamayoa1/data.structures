


def comprar_producto(articulos, comprados,total,countcomprados):
    print('SOLO PUEDE COMPRAR UN ARTÍCULO A LA VEZ\n')
    x=0
    countcomprados+=1
    for i in articulos:
        x+=1
        print('__________________\n')
        print(f'{x}. {i[0]}\n  -Precio: Q.{i[2]}\n')
    compra=int(input('Ingrese el número del producto que desea comprar\n'))
    comprados.append(articulos[compra-1])
    total+=articulos[compra-1][2]
    print('¡Articulo ingresado exitosamente!')
    return(comprados,total,countcomprados)
    

def pagar_productos(pagos, total,countpagos):
    pago=float(input(f'Ingrese el monto que desea agregar a sus pagos\n\nTotal a pagar:{total}\n\nMonto: Q.'))
    pagos.append(pago)
    countpagos+=1
    return pagos,countpagos

def generar_recibo(comprados,total,pagos):
    precios=[]
    print('RECIBO DE COMPRA:\n')
    print('_______________________\n')
    print('Artículos comprados:\n')
    for i in comprados:
        print(f'{i[1]}------{i[0]}\n')
        precios.append(i[2])
    print('_______________________\n')
    print(f'TOTAL A PAGAR Q.{total}\n\n')
    print(f'Total de pagos realizados: Q.{sum(pagos)}\n\n')
    print('_______________________\n')
    print(f'SALDO RESTANTE: Q.{total-sum(pagos)}\n')
    print('_______________________\n')
    print(f'El promedio por producto fue de: Q.{sum(precios)/len(precios)}\n')
    print(f'El precio del producto más caro fue: Q.{max(precios)}\n')
    print('_______________________\n')


def main():
    countpagos=0
    countcomprados=0
    comprados=[]
    pagos=[]
    total=0
    articulos=[
        ["Cereal","AR01", 25.0],
        ["Pan","AR02", 12.50],
        ["Leche","AR03", 10.25],
        ["Manzana","AR04", 4.75],
        ["Jugo de Naranja","AR05", 17.50],
        ["Cafe","AR06", 45.0],
        ["Tortillas de Harina","AR07", 20.0],
        ["Gelatina","AR08", 4.50],
        ["Galletas","AR09", 11.50],
        ["Naranja","AR10", 2.25]
    ]
    while(1):
        print('BIENVENIDO A PUNTO DE VENTA\n')
        opcion=int(input('1.Comprar Productos\n2.Pagar productos\n3.Ver recibo de compra\n4.Salir\n'))
        if opcion==1:
            comprados,total,countcomprados=comprar_producto(articulos, comprados,total,countcomprados)
        if opcion==2:
            pagos,countpagos=pagar_productos(pagos,total,countpagos)
        if opcion==3:
            if countpagos>5:
                generar_recibo(comprados,total,pagos)
            else:
                print('Debe realizar al menos 5 pagos para que pueda generar una factura\n')
        if opcion==4:
            exit()


