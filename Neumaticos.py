def neumaticos(tipo, cantidad, precio, descuento):
    subtotal = (cantidad * precio) * descuento
    iva = subtotal * 0.13
    monto_final = subtotal + iva

    print("\nGracias por su compra. A continuación, su factura:\nTipo..............", tipo, "\nCantidad..........",
          cantidad, "\nSubtotal..........", subtotal, "\nDescuento.........", descuento, "\nIVA...............",
          iva, "\nMonto por Pagar...", monto_final)


while True:
    menu = input(
        "\nGracias por utilizar nuestro programa. A continuación, el menú de opciones: \n\n1. Comprar neumáticos. "
        "\n2. Salir. \n\nDigite el número de la opción que desea ejecutar: \n")

    if menu == "1":

        tipo = input(
            "\nDe acuerdo. A continuación podrá seleccionar el tipo de neumáticos que desea comprar:\n"
            "\n1. Digite '1' para neumáticos sintéticos.\n2. Digite '2' para neumaticos híbridos."
            "\n3. Digite '3' para neumáticos naturales.\n")

        cantidad = int(input("\nDigite la cantidad de neumáticos que desea comprar: \n"))

        if tipo == "1":
            if cantidad > 10:
                descuento = 0.95
            else:
                descuento = 1
            neumaticos("Sintéticos", cantidad, 12000, descuento)
            print()

        elif tipo == "2":
            if cantidad > 10:
                descuento = 0.90
            else:
                descuento = 1
            neumaticos("Híbridos", cantidad, 25000, descuento)

        elif tipo == "3":
            if cantidad > 8:
                descuento = 0.93
            else:
                descuento = 1
            neumaticos("Naturales", cantidad, 45000, descuento)

    else:
        break