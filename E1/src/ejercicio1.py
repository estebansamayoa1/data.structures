
def nota(n):
    if(n>75):
        return "O"
    elif (n<=75 and n>=60):
        return "A"
    elif (n<=59 and n>=50):
        return "B"
    elif (n<=49 and n>=40):
        return "C"
    elif (n<40):
        return "D"



def main():
    n=int(input("Ingrese la nota obtenida:"))
    resultado=nota(n)
    print("Su nota obtenida es:"+resultado)

main()