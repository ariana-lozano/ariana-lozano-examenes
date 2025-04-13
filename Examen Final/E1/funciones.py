import random

#Crear función con 10 nums aleatorios
def lista_aleatorios():
    lista = []
    for i in range(10):
        lista.append (random.randint(1,100))
    print(f"\n La lista con 10 nums aleatorios es: {lista}")
    return lista

#Crear función que almacene nums no repetidos
def num_no_repetidos(lista):

    no_repetidos=[]
    for num_lista in lista:
        print(num_lista)
        if num_lista not in no_repetidos:
            no_repetidos.append(num_lista)

    print(f"\nLista de no repetidos es: {no_repetidos}")
    return no_repetidos

#Ordenar de mayor a menor y de menor a mayor
def ordenar_lista(no_repetidos):
    mayor_a_menor=sorted(no_repetidos,reverse=True)
    menor_a_mayor=sorted(no_repetidos)
    print(f"\nMayor a menor: {mayor_a_menor}")
    print(f"Menor a mayor: {menor_a_mayor}")
    return mayor_a_menor,menor_a_mayor

#Mayor num de la lista
def mayor_par_num(no_repetidos):
    lista_par=[]
    for i in no_repetidos:
        if(i%2==0):
            lista_par.append(i)

    if len(lista_par) >0:
        maximo=max(lista_par)
        print(f"El número máximo par es: {maximo}")
        return maximo
    else:
        print("No hay pares en la lista:")
        return None
