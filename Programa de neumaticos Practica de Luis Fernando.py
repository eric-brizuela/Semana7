# datos
precio_a = 12000
precio_b = 25000
precio_c = 45000
descuento_a=0.05
descuento_b=0.10
descuento_c=0.07
nombre = ""
cantidad = 0
x = ""

print("Bienvenidos a nuestro programa de neumaticos")
nombreUsuario = input("Digite el nombre de usuario")
print("\t\tmenu\t\t")
print("1- Neumaticos sinteticos ")
print("Neumaticos naturales ")
print("3- Neumaticos hibridos")
print("4-salir")


def calculo_neumatico(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal


def aplicar_descuento(subtotal, descuento):
    subtotal_descuento = subtotal * descuento
    return subtotal_descuento


def aplicar_iva(subtotal_descuento):
    aplicar_iva = subtotal_descuento * 0.13
    monto_final = subtotal_descuento + iva
    return monto_final


def imprimir(tipo, cantidad, subtotal, descuento, iva, monto_final):
    print("\t\t\t\n gracias por su compra. A conticuaciónsu factura: \n Tipo........", tipo, "")


while True:
    print("\t\tmenu\t\t")
    print("1- Neumaticos sinteticos ")
    print("Neumaticos naturales ")
    print("3- Neumaticos hibridos")
    print("4-salir")
    x = int(input("seleccione el producto que decea comprar"))
    cantidad = int(input("Digite la cantidad que desea comprar"))
    if x == "1":
        if cantidad > 10:
            descuento_sintetico=aplicar_descuento(subtotal,descuento_a)
            print("El descuento de los neumaticos sinteticos es", descuento_sintetico)
        elif cantidad <= 10:
            sin_descuento_sintetico = subtotal(cantidad*precio_a)
            print("El  precio del neumatico es", sin_descuento_sintetico)

    if x == "2":
        if cantidad > 10:
            descuento_naturales = aplicar_descuento(subtotal,descuento_b)
            print("El descuento de los neumaticos naturales es", descuento_naturales)
        elif cantidad <= 10:
            sin_descuento_naturales = calculo_neumatico(cantidad*precio_b)
            print("El precio del neumatico naturales sin descuento es de",sin_descuento_naturales)

    if x == "3":
        if cantidad > 10:
            descuento_hibridos =  aplicar_descuento(subtotal,descuento_c)
        print("El descuento de los neumaticos hibridos es", descuento_hibridos)

    elif cantidad <= 10:
        sin_descuento_hibrido = calculo_neumatico(cantidad,precio_c)
        print("El neumatico hibrido sin descuento es de",sin_descuento_hibrido)

    else:
        print("hasta pronto")
