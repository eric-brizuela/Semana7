tipo = ""
cantidad = 0
subtotal = 0
porcentaje_descuento = 0.0
descuento = 0
iva = 0


def calculo_neumaticos(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal


def aplicar_descuento(subtotal, descuento):
    subtotal_con_descuento = subtotal - (subtotal * descuento)
    return subtotal_con_descuento


def aplicar_iva(subtotal, subtotal_con_descuento):
    subtotal = subtotal - subtotal_con_descuento
    iva = subtotal * 0.13
    return iva


def imprimir_factura(tipo, cantidad, subtotal, descuento, iva, total):
    print("\nGracias por su compra. A continuación, su factura:\nTipo..............", tipo, "\nCantidad..........",
          cantidad, "\nSubtotal..........", subtotal, "\nDescuento.........", descuento, "\nIVA...............",
          iva, "\nMonto por Pagar...", total)


while True:
    menu = input(
        "\nGracias por utilizar nuestro programa. A continuación, el menú de opciones: \n\n1. Cálculo neumáticos. "
        "\n2. Aplicar descuento.\n3. Cálculo deL IVA.\n4. Imprimir Factura.\n5. Salir. \n"
        "\nDigite el número de la opción que desea ejecutar: \n")

    if menu == "1":
        tipo = input(
            "\nDe acuerdo. A continuación podrá seleccionar el tipo de neumáticos que desea comprar:\n"
            "\n1. Digite '1' para neumáticos sintéticos.\n2. Digite '2' para neumaticos híbridos."
            "\n3. Digite '3' para neumáticos naturales.\n")

        cantidad = int(input("\nDigite la cantidad de neumáticos que desea comprar: \n"))

        if tipo == "1":
            tipo = "Sintéticos"
            if cantidad > 10:
                porcentaje_descuento = 0.95
                porcentaje = "5%"
            else:
                porcentaje_descuento = 1
                porcentaje = "0%"
            subtotal = calculo_neumaticos(cantidad, 12000)
            print("Subtotal..........", subtotal)
            print("Descuento aplicable...", porcentaje)
            continue

        if tipo == "2":
            tipo = "Híbridos"
            if cantidad > 10:
                porcentaje_descuento = 0.90
                porcentaje = "10%"
            else:
                porcentaje_descuento = 1
                porcentaje = "0%"
            subtotal = calculo_neumaticos(cantidad, 25000)
            print("Subtotal..........", subtotal)
            print("Descuento aplicable...", porcentaje)
            continue

        if tipo == "3":
            tipo = "Naturales"
            if cantidad > 8:
                porcentaje_descuento = 0.93
                porcentaje = "7%"
            else:
                porcentaje_descuento = 1
                porcentaje = "0%"
            subtotal = calculo_neumaticos(cantidad, 45000)
            print("Subtotal..........", subtotal)
            print("Descuento aplicable...", porcentaje)
            continue

    if menu == "2":
        descuento = aplicar_descuento(subtotal, porcentaje_descuento)
        print("Descuento.........", descuento)
        continue

    if menu == "3":
        iva = aplicar_iva(subtotal, descuento)
        print("IVA...............", iva)
        continue

    if menu == "4":
        total = subtotal - descuento + iva
        imprimir_factura(tipo, cantidad, subtotal, descuento, iva, total)
        continue

    else:
        print("Adios!")
        break
