
#Item 1
#Mostrar los minutos que el decorador está siendo utilizado

from datetime import datetime

#decorador
def decorador_hora(func):
    def wrapper(**kwargs):
        #Mostrar hoy y minuto
        ahora = datetime.now()
        print(f"\nEl decorador está siendo ejecutado a las {ahora.hour} con {ahora.minute} minutos")


        #Item 2
        #Sumar los elementos de la función
        suma=sum(kwargs.values())
        print(f"La suma de los valores es: {suma}")

        #LLamar a la función original
        return func(**kwargs)
    return wrapper

#Item 3 y 4
#Función que recibe N parámetros y muestra el mayor
@decorador_hora
def encontrar_mayor(**kwargs):
    mayor = max(kwargs.values())
    print("El número mayor es:", mayor)



# Función usando 6 números y decorando
encontrar_mayor(a=5, b=9, c=3, d=7, e=10, f=2)

#Más de 6 números
encontrar_mayor(x=15, y=3, z=25)
encontrar_mayor(n1=20, n2=15, n3=18, n4=25, n5=30, n6=10, n7=45)





