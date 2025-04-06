#Copiado de la pregunta 1
class Empleado:
    def __init__(self):
        #Atributos
        self.nombre = ""
        self.edad = 0
        self.saldo = 0
        self.nacionalidad ="Peruana"

    #Solicitar nombre (input())
    def pedir_nombre(self):
        self.nombre=input("Ingrese el nombre del empleado: ")

    #Solicitar la edad
    def pedir_edad(self):
        self.edad=int(input("Ingrese la edad del empleado: "))

    #Definir saldo
    def definir_saldo(self, saldo_inicial):
        self.saldo = saldo_inicial

    #Método cumpleaños
    def cumpleaños(self):
        #Agregar 1 año cada vez que ingrese
        self.edad +=1

    #Método aumentoSaldo
    def aumento_saldo(self):
        self.saldo = self.saldo*1.30
        return self.saldo

    #Ingresar edad del año
    def edad_en_anio(self,anio_futuro):
        edad_futura = self.edad + (anio_futuro - 2024)
        # Retornar el mensaje “En el año 2025 tendrá XX años”
        resultado = "En el año " + str(anio_futuro) + " tendrá " + str(edad_futura) + " años."
        return resultado

empleados = []

#Ingresar hasta 2 personas
for i in range(2):
    print(f"\n Empleado {i+1}")

    #'emp' va ser una instancia (un objeto) de la clase 'Empleado'
    emp=Empleado()
    #LLama al método 'pedir_nombre' (donde está el input()) y lo guarda en 'emp'
    emp.pedir_nombre()
    emp.pedir_edad()

    #Pedir el saldo inicial
    saldo_inicial = float(input("Ingrese el saldo inicial del empeado: "))
    #Guarda este saldo en 'emp'
    emp.definir_saldo(saldo_inicial)
    emp.cumpleaños()

    nuevo_saldo = emp.aumento_saldo()
    print(f"Sueldo con aumento del 30%:  {nuevo_saldo}")
    print(emp.edad_en_anio(2025))
    empleados.append(emp)

#Pregunta 2
class Persona:
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self.__saldo = saldo #Ocultar el saldo

    #Mostrar saldo
    def mostrar_saldo(self):
        print(f"Saldo de {self.nombre} : {self.__saldo}")

    #Obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    #Métodos para modificar el saldo
    def actualizar_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

# Clase Empleado que hereda de Persona
class Empleado(Persona):
    # Método para transferir dinero a otro empleado
    def transferencia(self, receptor, monto):
        if self.obtener_saldo() >= monto:
            self.actualizar_saldo(self.obtener_saldo() - monto)
            receptor.actualizar_saldo(receptor.obtener_saldo() + monto)
            print(self.nombre, "transferió", monto, "a", receptor.nombre)
        else:
            print("Saldo insuficiente para transferir", monto)

# Crear 2 empleados
empleado1 = Empleado("Valeria", 1000)
empleado2 = Empleado("George", 700)

# Mostrar saldos antes de la transferencia
empleado1.mostrar_saldo()
empleado2.mostrar_saldo()

# Hacer la transferencia
empleado1.transferencia(empleado2, 300)

# Mostrar saldos después de la transferencia
empleado1.mostrar_saldo()
empleado2.mostrar_saldo()