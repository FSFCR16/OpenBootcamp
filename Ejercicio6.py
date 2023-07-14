class Vehiculo:

    def __init__(self, color, ruedas, puertas):

        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

    def getinfo_vehiculo(self):

        return(f"El vehiculo tiene las siguientes caracteristicas: \nColor: {self.color} \nRuedas: {self.ruedas} \nPuertas: {self.puertas} " )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindraje):
        Vehiculo.__init__(self, color, ruedas, puertas)
        
        self.velocidad=velocidad

        self.cilidraje=cilindraje

    def getinfo_coche(self):

        print(super().getinfo_vehiculo()+ f"\nVelocidad: {self.velocidad} \nCilindraje: {self.cilidraje}")
    

mercedes=Coche("Negro", "4", "2", "200km\h", "2000")

print(mercedes.getinfo_coche())



    