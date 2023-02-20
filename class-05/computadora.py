class Computadora:
    def __init__(self, marca: str, ram: int, tamano_disco: int, precio: float, stock: int, descuento: int = 0):
        self.marca = marca
        self.ram = ram
        self.tamano_disco = tamano_disco
        self.precio = precio
        self.stock = stock
        self.dscto = descuento

    def __str__(self):
        return f"Detalles de la computadora:\n \
                Marca: {self.marca}\n \
                Cantidad de RAM: {self.ram} GB\n \
                Almacenamiento: {self.tamano_disco} GB\n \
                Precio: USD {self.precio}\n \
                Stock: {self.stock} unidades\n \
                Precio (con descuento): USD {self.calcular_precio()}\n"

    #Asigna un nuevo precio (actualiza el precio)
    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    #Asigna un nuevo descuento (actualiza el descuento)
    def set_dscto(self, nuevo_dscto):
        self.dscto = nuevo_dscto

    #Calcula precio con descuento
    def calcular_precio(self):
        return self.precio - ((self.precio * self.dscto) / 100)

    #Actualiza el stock (aumentándolo o disminuyéndolo según sea el parámetro)
    def set_stock(self, variabilidad):
        self.stock += variabilidad

if __name__ == "__main__":
    print("Ejecución del módulo computadora")
