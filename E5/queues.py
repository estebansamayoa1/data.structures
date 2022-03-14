import random

class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class Queue:  
  
    def __init__(self):  
        self.queue = list()  

    def add_element(self,val):   
        if val not in self.queue:  
            self.queue.insert(0,val)  
            return True  
        return False  

    def remove_element(self):  
        if len(self.queue)>0:  
            return self.queue.pop(0)  
        return ("Queue is Empty")  




def sort_elements(que):
    return que['social security'] 


def main():
    size=5
    j=0
    random_workers=[]
    que = Queue() 
    t1=Node({"social security":1234,"name of worker":"rodrigo reyes","days worked":13})
    t2=Node({"social security":3312,"name of worker":"alejandro gutierrez","days worked":13})
    t3=Node({"social security":1457,"name of worker":"alex lopez","days worked":13})
    t4=Node({"social security":2347,"name of worker":"matias estrada","days worked":13})
    t5=Node({"social security":7980,"name of worker":"juan fernandez","days worked":13})
    t6=Node({"social security":5689,"name of worker":"nicko nolte","days worked":13})
    t7=Node({"social security":5678,"name of worker":"esteban samayoa","days worked":13})
    t8=Node({"social security":9876,"name of worker":"daniel behar","days worked":13})
    t9=Node({"social security":1209,"name of worker":"jose reyes","days worked":13})
    t10=Node({"social security":2398,"name of worker":"luis figueroa","days worked":13})
    llenar=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
    while j<size:
        n = random.randint(0,10)
        if n not in random_workers:
            random_workers.append(n)
            j+=1
    i=0
    for i in random_workers:
        que.add_element(llenar[i].dataval)
    while(1):
        opcion=int(input("1.Agregar un trabajador al Queue\n2.Ver lista de trabajadores\n3.Vaciar lista\n4.Salir\n"))

        if opcion==1:
            social_security=int(input("Ingrese el número de seguridad social\n"))
            name=input("Ingrese el nombre del trabajador\n")
            days=int(input("Ingrese el número de días trabajados\n"))
            que.add_element({"social security":social_security,"name of worker":name,"days worked":days})

        if opcion==2: 
            a=que.queue
            a.sort(key=sort_elements)  
            for i in que.queue:
                print(f"SOCIAL SECURITY ID: {i['social security']}")
                print(f"NAME OF WORKER: {i['name of worker']}")
                print(f"DAYS WORKED:{i['days worked']}")
                print("_______________________________\n")
        
        if opcion==3:
            while len(que.queue)>0:
                print("TRABAJADOR A BORRAR DEL QUEUE:\n")
                print(f"SOCIAL SECURITY ID:{que.queue[0]['social security']}")
                print(f"NAME OF WORKER:{que.queue[0]['name of worker']}")
                print("_______________________________\n")
                que.remove_element() 
                print("TRABAJADOR BORRADO\n")

        if opcion==4:
            exit()




    


main()
    


    
