from behave import given, when, then
from src.producto import Producto


@given('un producto llamado "{nombre}" con precio base de {precio:d}')
def step_crear_producto(context, nombre, precio):
    context.producto = Producto(nombre, precio)
    context.error = None


@when('aplico un descuento del {descuento:d}%')
def step_aplicar_descuento(context, descuento):
    context.producto.aplicar_descuento(descuento)


@when('intento aplicar un descuento del {descuento:d}%')
def step_intentar_descuento_invalido(context, descuento):
    try:
        context.producto.aplicar_descuento(descuento)
    except ValueError as e:
        context.error = str(e)


@when('calculo el precio final')
def step_calcular_precio(context):
    context.precio_final = context.producto.calcular_precio_final()


@then('el descuento debe quedar registrado como {descuento:d}%')
def step_verificar_descuento(context, descuento):
    assert context.producto.descuento == descuento


@then('el sistema debe rechazarlo con el mensaje "{mensaje}"')
def step_verificar_error(context, mensaje):
    assert context.error == mensaje, f"Error esperado: '{mensaje}', obtenido: '{context.error}'"


@then('el precio final debe ser {precio_final:f}')
def step_verificar_precio_final(context, precio_final):
    assert abs(context.precio_final - precio_final) < 0.01, \
        f"Esperado: {precio_final}, obtenido: {context.precio_final}"