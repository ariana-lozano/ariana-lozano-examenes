from Práctica_01.Pregunta1 import nombre, salario, edad_int, compania, bono_final

# Crear una lista vacía
datos =[]

# Añadir datos de la pregunta1 a la lista
datos.append(nombre)
datos.append(salario)
datos.append(edad_int)
datos.append(compania)
datos.append(bono_final)

# Añadir "true" o "false" si está trabajando en esa empresa
empleado = True
datos.append(empleado)

# Mostrar en consola
print("Lista de datos: {}".format(datos))

# Agregar variable "apellido"
apellido = "Lozano"

print("--------------------------------------------------------------------------")
# Condicional
if empleado:
    # Mostrar tamaño de la lista
    print("El tamaño de mi lista es: {}".format(len(datos)))
    print("El trabajador {} {} se encuentra trabajando en la compañía".format(nombre,apellido))
else:
    print("El trabajador {} {} ya no se encuentra trabajando actualmente en la empresa".format(nombre,apellido))