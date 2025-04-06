
# Declaración de variables
nombre = "Ariana"
salario = 1100
edad = "18"
compania = "PUCP"

#Identificar tipos de variables
print("El nombre es: {}".format(type(nombre)))
print("El salario es: {}".format(type(salario)))
print("El edad es: {}".format(type(edad)))
print("El compañía es: {}".format(type(compania)))

# Convertir variable edad a string
edad_int = int(edad)

edad_mayor = edad_int > 30
print("-----------------------------------------------------------")

# Condicional
if edad_mayor:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono_final = pow(salario, 2) + (0.1 * salario)

else:
    print("Usted tiene un bono del 5% en el mes diciembre")
    bono_final = pow(salario, 2) + (0.05 * salario)

# Mostrar bono final

print("El bono final es de {} soles".format(bono_final))
