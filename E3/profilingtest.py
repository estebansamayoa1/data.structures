import cProfile

from src.receipt import comprar_producto, pagar_productos, main



#Aqui prueba solo la función de agregar un crédito
cProfile.run('comprar_producto([["Cereal","AR01", 25.0], ["Pan","AR02", 12.50],["Leche","AR03", 10.25],["Manzana","AR04", 4.75]],[],0,0)')
#Aqui se prueba solo la función de borrar un valor
cProfile.run('pagar_productos([],25.0,0)')
#Aquí se prueba todo el código con todas sus funciones que se realicen
cProfile.run('main()')