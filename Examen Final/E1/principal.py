#Importaciones
import funciones

# Llamar a las funciones una por una
lista_completa = funciones.lista_aleatorios()
lista_sin_repetidos = funciones.num_no_repetidos(lista_completa)
funciones.ordenar_lista(lista_sin_repetidos)
funciones.mayor_par_num(lista_sin_repetidos)

