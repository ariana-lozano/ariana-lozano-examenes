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