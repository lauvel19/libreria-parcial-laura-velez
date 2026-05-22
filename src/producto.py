class Producto:
    """Representa un producto de la Librería del Centro con lógica de precios."""

    IVA = 0.19
    DESCUENTO_MAXIMO = 40

    def __init__(self, nombre: str, precio_base: float):
        """
        Crea un producto con nombre y precio base.
        El precio base debe ser mayor que cero.
        """
        self._validar_precio(precio_base)
        self.nombre = nombre
        self.precio_base = precio_base
        self.descuento = 0

    def aplicar_descuento(self, descuento: float):
        """
        Aplica un descuento porcentual al producto.
        El descuento debe estar entre 0% y 40%.
        """
        self._validar_descuento(descuento)
        self.descuento = descuento

    def calcular_precio_final(self) -> float:
        """
        Calcula el precio final aplicando descuento e IVA.
        Fórmula: precio_base * (1 - descuento/100) * (1 + IVA)
        """
        precio_con_descuento = self.precio_base * (1 - self.descuento / 100)
        return precio_con_descuento * (1 + self.IVA)

    def _validar_precio(self, precio: float):
        if precio <= 0:
            raise ValueError("El precio base debe ser mayor que cero")

    def _validar_descuento(self, descuento: float):
        if descuento < 0:
            raise ValueError("El descuento no puede ser negativo")
        if descuento > self.DESCUENTO_MAXIMO:
            raise ValueError("El descuento no puede superar el 40%")