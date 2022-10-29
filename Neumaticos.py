tipo = ""
cantidad = 0
subtotal = 0
porcentaje_descuento = 0.0
descuento = 0
iva = 0
monto_final = 0


def calculo_neumaticos(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal


def aplicar_descuento(subtotal, descuento):
    subtotal_descuento = subtotal * descuento
    return subtotal_descuento


def aplicar_iva(subtotal_descuento):
    iva = subtotal_descuento * 0.13
    monto_final = subtotal_descuento + iva
    return monto_final


def imprimir_factura(tipo, cantidad, subtotal, descuento, iva, monto_final):
    print("\nGracias por su compra. A continuación, su factura:\nTipo..............", tipo, "\nCantidad..........",
          cantidad, "\nSubtotal..........", subtotal, "\nDescuento.........", descuento, "\nIVA...............",
          iva, "\nMonto por Pagar...", monto_final)


while True:
    menu = input(
        "\nGracias por utilizar nuestro programa. A continuación, el menú de opciones: \n\n1. Cálculo neumáticos. "
        "\n2. Aplicar descuento.\n3. Cálculo deL IVA.\n4. Imprimir Factura. \n"
        "\nDigite el número de la opción que desea ejecutar: \n")

    if menu == "1":
        tipo = input(
            "\nDe acuerdo. A continuación podrá seleccionar el tipo de neumáticos que desea comprar:\n"
            "\n1. Digite '1' para neumáticos sintéticos.\n2. Digite '2' para neumaticos híbridos."
            "\n3. Digite '3' para neumáticos naturales.\n")

        cantidad = int(input("\nDigite la cantidad de neumáticos que desea comprar: \n"))

        if tipo == "1":
            if cantidad > 10:
                porcentaje_descuento = 0.95
            else:
                porcentaje_descuento = 1
            subtotal = calculo_neumaticos(cantidad, 12000)
            print("Subtotal..........", subtotal)
            continue

        if tipo == "2":
            if cantidad > 10:
                porcentaje_descuento = 0.90
            else:
                porcentaje_descuento = 1
            subtotal = calculo_neumaticos(cantidad, 25000)
            print("Subtotal..........", subtotal)
            continue

        if tipo == "3":
            if cantidad > 8:
                porcentaje_descuento = 0.93
            else:
                porcentaje_descuento = 1
            subtotal = calculo_neumaticos(cantidad, 45000)
            print("Subtotal..........", subtotal)
            continue

    if menu == "2":
        descuento = aplicar_descuento(subtotal, porcentaje_descuento)
        print(descuento)
        continue

    if menu == "3":
        iva = aplicar_iva(subtotal)
        print(iva)
        continue

    if menu == "4":
        imprimir_factura(tipo, cantidad, subtotal, iva, monto_final)
        continue

    else:
        print("Adios!")
        break