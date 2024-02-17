class Ave:
    def __init__(self, nombre, edad, especie):
        print(f"Creando ave {nombre}")


        self.nombre = nombre
        self.edad = edad
        self.especie = especie
    

    def volar(self):
        print("Volar, volar, volando...")

    def comer(self):
        print("Comiendo, come, comido...")


mi_ave = Ave("Aquila", "2 años", "Águila")


mi_ave.volar()
mi_ave.comer()
print(f"La edad de la ave {mi_ave.nombre} es {mi_ave.edad} años")
