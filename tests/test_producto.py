import pytest
from src.producto import Producto

# REGLA 1 

def test_crear_producto_con_precio_valido():
    producto = Producto("Libro", 50000)
    assert producto.nombre == "Libro"
    assert producto.precio_base == 50000

def test_crear_producto_con_precio_cero_lanza_error():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Libro", 0)

def test_crear_producto_con_precio_negativo_lanza_error():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Libro", -100)


# REGLA 2

def test_aplicar_descuento_valido():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(20)
    assert producto.descuento == 20

def test_aplicar_descuento_limite_inferior_cero():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(0)
    assert producto.descuento == 0

def test_aplicar_descuento_limite_superior_cuarenta():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(40)
    assert producto.descuento == 40

def test_aplicar_descuento_mayor_cuarenta_lanza_error():
    producto = Producto("Libro", 10000)
    with pytest.raises(ValueError, match="El descuento no puede superar el 40%"):
        producto.aplicar_descuento(41)

def test_aplicar_descuento_negativo_lanza_error():
    producto = Producto("Libro", 10000)
    with pytest.raises(ValueError, match="El descuento no puede ser negativo"):
        producto.aplicar_descuento(-5)

# REGLA 3

def test_calcular_precio_final_con_descuento():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(20)
    assert producto.calcular_precio_final() == pytest.approx(9520.0)

def test_calcular_precio_final_sin_descuento():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(0)
    assert producto.calcular_precio_final() == pytest.approx(11900.0)

def test_precio_final_nunca_es_negativo():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(40)
    assert producto.calcular_precio_final() >= 0