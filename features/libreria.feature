Feature: Gestion de precios de productos en la Libreria del Centro
  Como administrador de la libreria
  Quiero aplicar descuentos y calcular el precio final con IVA
  Para ofrecer precios justos y transparentes a los clientes

  Background:
    Given un producto llamado "Libro de Calculo" con precio base de 10000

  @descuento_valido
  Scenario: Aplicar un descuento valido dentro del rango permitido
    When aplico un descuento del 20%
    Then el descuento debe quedar registrado como 20%

  @descuento_limite
  Scenario: Aplicar descuento en el limite superior permitido
    When aplico un descuento del 40%
    Then el descuento debe quedar registrado como 40%

  @descuento_invalido
  Scenario: Rechazar un descuento mayor al 40%
    When intento aplicar un descuento del 41%
    Then el sistema debe rechazarlo con el mensaje "El descuento no puede superar el 40%"

  @precio_final
  Scenario: Calcular precio final con descuento e IVA
    When aplico un descuento del 20%
    And calculo el precio final
    Then el precio final debe ser 9520.0

  @precio_final
  Scenario Outline: Calcular precio final con distintos descuentos
    When aplico un descuento del <descuento>%
    And calculo el precio final
    Then el precio final debe ser <precio_final>

    Examples:
      | descuento | precio_final |
      | 0         | 11900.0      |
      | 10        | 10710.0      |
      | 40        | 7140.0       |