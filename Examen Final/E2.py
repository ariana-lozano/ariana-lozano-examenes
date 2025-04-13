from datetime import datetime

#Decorador
def conteo(func):
    def wrapper (*args,**kwargs):
        cantidad = len(args) + len(kwargs)
        if cantidad <= 1:
            print("Se necesitan más de un parámetro")
            return
        resultado = func(*args,**kwargs)
        print("La función fue ejecutada")
        return resultado
    return wrapper


#Función para calcular promedio
@conteo
def calcular_promedio(n1, n2, n3, n4):
    promedio = (n1 + n2 + n3 + n4) / 4
    print("El promedio de las 4 notas es:", promedio)


#Función para registro de persona
def registrar_persona(nombre, edad):
    ahora = datetime.now()
    hora = ahora.hour
    minuto = ahora.minute
    print(f"{nombre} de {edad} años ha sido registrado a las {hora} horas con {minuto} minutos.")


#Datos de prueba
calcular_promedio(15, 13, 18, 17)
registrar_persona("Pedro", 30)