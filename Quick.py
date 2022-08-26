import time
import random as rd
def Particion(lista, inicio, fin):
    pivot = lista[inicio]
    min = inicio + 1
    maxim = fin
#hola jacobo
    while True:
        

        while min <= maxim and lista[maxim] >= pivot:
            maxim = maxim - 1

        while min <= maxim and lista[min] <= pivot:
            min = min + 1

        if min <= maxim:
            lista[min], lista[maxim] = lista[maxim], lista[min]
            
        else:
          
            break

    lista[inicio], lista[maxim] = lista[maxim], lista[inicio]

    return maxim

def quickSort (lista, inicio, fin):
    if inicio >= fin:
        return

    p = Particion(lista, inicio, fin)
    quickSort(lista, inicio, p-1)
    quickSort(lista, p+1, fin)




def crearRandom(a:list,n:int):
    for i in range(n):
        b=rd.randint(0,15000000)
        a.append(b)

def crearDescendente(a:list,n:int):
    for i in range(n):
        a.append(15000000-(i*(15000000/n)))     

def imprimir(lista:list):
    for i in range(len(lista)):
        print(lista[i])        

k=500000
while k<15000001:
    listaRan=[]
    listaDesc=[]
    num=k
    #num=int(input("Cuantos numeros va a contener el arreglo: "))

    crearRandom(listaRan,num)
    #crearDescendente(listaDesc,num)

    #imprimir(listaRan)
    #imprimir(listaDesc)

    inicioR = time.time()
    quickSort(listaRan, 0, len(listaRan) - 1) 
    finR = time.time()

    '''inicioD = time.time()
    quickSort(listaDesc, 0, len(listaDesc) - 1) 
    finD = time.time()'''

    #imprimir(listaRan)
    #imprimir(listaDesc)

    print(str(k)+"Tiempo en segundos ordenando ascendentemente el Random: "+str(finR-inicioR))
    #print("Tiempo en segundos ordenando ascendentemente el Descen: "+str(finD-iniciod))
    k+=500000