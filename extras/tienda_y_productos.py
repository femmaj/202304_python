class Tienda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        return self

    def vender_producto(self, id):
        self.productos.pop(id)
        return self

    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)
        return self

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, False)
        return self


class Producto:

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje
        else:
            self.precio -= self.precio * cambio_porcentaje
        return self
    
    def imprimir_info(self):
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}")
        return self
    

alfajor = Producto(nombre="Alfajor", precio=500, categoria="Confites")
empolvado = Producto(nombre="Empolvado", precio=600, categoria="Confites")
palmeritas = Producto(nombre="Palmeritas", precio=200, categoria="Confites")

dulces_chilenos = Tienda(nombre="Dulces Chilenos")

dulces_chilenos.agregar_producto(alfajor)
dulces_chilenos.agregar_producto(empolvado)
dulces_chilenos.agregar_producto(palmeritas)

print("Stock de la tienda:")
for producto in dulces_chilenos.productos:
    producto.imprimir_info()

dulces_chilenos.vender_producto(1)

print("Stock de la tienda después de vender un producto:")
for producto in dulces_chilenos.productos:
    producto.imprimir_info()

dulces_chilenos.inflacion(0.1)

print("Stock de la tienda después de inflación:")
for producto in dulces_chilenos.productos:
    producto.imprimir_info()

dulces_chilenos.hacer_liquidacion("Confites", 0.5)

print("Stock de la tienda después de liquidación:")
for producto in dulces_chilenos.productos:
    producto.imprimir_info()
