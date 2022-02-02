
def add_credit(creditcount, credits, amount):
    credits.append(amount)
    creditcount+=1
    print("¡Monto Ingresado con Exito!\n")
    return creditcount,credits
  

def add_debit(debitcount, debits, amount):
    debits.append(amount)
    debitcount+=1
    print("¡Monto Ingresado con Exito!\n")
    return debitcount,debits

def info_debitsandcredits(creditcount, credits,debitcount, debits):
    sumacredits=sum(credits)
    sumadebits=sum(debits)
    saldo=sumacredits-sumadebits
    avdebits=sumadebits/len(debits)
    avcredits=sumacredits/len(credits)
    mayor_debit=max(debits)
    mayor_credit=max(credits)
    print("INFORMACIÓN ACERCA DE CRÉDITOS\n")
    print('______________________________\n')
    print(f'Cantidad de Créditos realizados: {creditcount}\nCantidad actual de Crédito (Suma de créditos): Q.{sumacredits}\nPromedio de Créditos: Q.{avcredits}\nMayor ingreso a Créditos: Q.{mayor_credit}\n')
    print('______________________________\n\n')
    print("INFORMACIÓN ACERCA DE DÉBITOS\n")
    print('______________________________\n')
    print(f'Cantidad de Debitos realizados: {debitcount}\nCantidad actual de Debito (Suma de debitos): Q.{sumadebits}\nPromedio de Debitos: Q.{avdebits}\nMayor ingreso a Debitos: Q.{mayor_debit}\n')
    print('______________________________\n\n')
    print(f'Saldo Final (Créditos-Debitos):{saldo}')
    print('______________________________\n______________________________\n')


def delete(count, info, posicion):
    count-=1
    info.pop(posicion-1)
    print(info)
    return(count, info)



def main():
    creditcount=0
    debitcount=0
    credits=[]
    debits=[]
    while(1):
        print('DEBITS AND CREDITS S.A.\n')
        menu=int(input('1.Agregar un Crédito\n2.Agregar un Debito\n3.Ver Información de Debitos y Créditos\n4.Eliminar Crédito ó Débito\n5.Salir\n'))
        if menu==1:
            amount=float(input('Ingrese el monto del crédito a ingresar\n'))
            creditcount, credits=add_credit(creditcount,credits, amount)
        if menu==2:
            amount=float(input('Ingrese el monto del débito a ingresar\n'))
            debitcount, debits=add_debit(debitcount, debits, amount)
        if menu==3:
            if creditcount>10 and debitcount>5:
                info_debitsandcredits(creditcount, credits,debitcount, debits)
            else:
                print('Debe ingresar al menos 10 créditos y 5 débitos para poder generar esta información\n')   
        if menu==4:
            if creditcount>10 and debitcount>5:
                opcion=int(input('¿Desea eliminar un crédito ó un debito?\n1.Crédito\n2.Debito\n'))
                if opcion==1:
                    for i in range(len(credits)):
                        print(f'{i+1}. {credits[i]}\n')
                    posicion=int(input('¿Cual de los créditos desea borrar?\n'))
                    creditcount,credits=delete(creditcount,credits,posicion)
                if opcion==2:
                    for i in range(len(debits)):
                        print(f'{i+1}. {debits[i]}\n')
                    posicion=int(input('¿Cual de los debitos desea borrar?\n'))
                    debitcount,debits=delete(debitcount,debits,posicion)
            else:
                print('Debe ingresar al menos 10 créditos y 5 débitos para poder generar esta información\n') 
        if menu==5:
            exit()
