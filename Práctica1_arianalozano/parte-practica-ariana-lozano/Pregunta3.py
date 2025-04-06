from Práctica_01.Pregunta1 import bono_final, nombre, salario, edad_int, compania
from Práctica_01.Pregunta2 import empleado

# Declarar variable lista
lista = [nombre,salario,edad_int,compania,bono_final,empleado]

# Agregar el último valor a mi lista y agregar previamente la variable cant_hijos
cant_hijos = 5
lista.append(cant_hijos)

# La persona tiene o no hijos
si_tiene_hijos = cant_hijos != 0

print("--------------------------------------------------------------")
# Condicional
if si_tiene_hijos:
    bono_familiar = (salario * 8) /100
    lista.append((bono_familiar))
    print("Lista: {}".format(lista))
    print("Obtiene el bono familiar el cuál es de: {} soles ".format(bono_familiar))
else:
    print("No cumple para obtener el bono familiar")