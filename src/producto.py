class Producto:
    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")
        self.nombre = nombre
        self.precio_base = precio_base
        self.descuento = 0

    def aplicar_descuento(self, descuento):
        if descuento < 0:
            raise ValueError("El descuento no puede ser negativo")
        if descuento > 40:
            raise ValueError("El descuento no puede superar el 40%")
        self.descuento = descuento

    def calcular_precio_final(self):
        precio_con_descuento = self.precio_base * (1 - self.descuento / 100)
        precio_final = precio_con_descuento * 1.19
        return precio_final