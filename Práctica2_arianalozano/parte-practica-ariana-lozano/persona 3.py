class Billetera:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.soles = saldo_soles
        self.dolares = saldo_dolares
        self.tipo_cambio = 3.7  # 1 dólar = 3.7 soles

    def mostrar_saldos(self):
        print(f"\nSaldos de {self.nombre} {self.apellido}:")
        print(f"Soles: S/{self.soles}")
        print(f"Dólares: ${self.dolares:.2f}")

    def transferir(self, desde, monto):
        if desde == "soles":
            if self.soles >= monto:
                dolares = monto / self.tipo_cambio
                self.soles = self.soles - monto
                self.dolares = self.dolares + dolares
                print("Transferencia hecha de soles a dólares")
            else:
                print("No tienes suficientes soles")
        if desde == "dolares":
            if self.dolares >= monto:
                soles = monto * self.tipo_cambio
                self.dolares = self.dolares - monto
                self.soles = self.soles + soles
                print("Transferencia hecha de dólares a soles")
            else:
                print("No tienes suficientes dólares")

    def retirar(self, moneda, monto):
        if moneda == "soles":
            if self.soles >= monto:
                self.soles -= monto
                print(f"Retiro exitoso: S/{monto}")
            else:
                print("No hay suficientes soles.")
        if moneda == "dolares":
            if self.dolares >= monto:
                self.dolares -= monto
                print(f"Retiro exitoso: ${monto}")
            else:
                print("No hay suficientes dólares.")

# Crear cuenta
usuario = Billetera("Camila", "Chávez", 1000, 200)

# Mostrar saldos iniciales
usuario.mostrar_saldos()

# 3 transferencias
usuario.transferir("soles", 470)   # convierte S/470 a $
usuario.transferir("dolares", 60)  # convierte $60 a S/
usuario.transferir("soles", 200)   # otra transferencia

# Retiro
usuario.retirar("soles", 100)

# Mostrar saldos finales
usuario.mostrar_saldos()