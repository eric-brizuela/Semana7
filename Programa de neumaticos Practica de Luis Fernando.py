# Datos utilizados
costoSintetico = 12000
costoNaturales = 25000
costoHibridos = 45000
x = ""
y = 0
nombre = ""
iva = 0.13
calculoIVA = 0

# comercio de neumaticos
def saludo():
    print("\t\t\t Bienvenidos al programa de venta de neumaticos\t\t\t")


def descripción():
    print("Este es el programa que le permite a las personas en comprar los neumaticos de su gusto, cantidad y ",
          end="")
    print("aprobechar los diferentes descuentos que ofrece nuestro programa virtual")


def menu():
    print("Seleccione uno de las opciones")
    print("1-Neumaticos Sinteticos")
    print("2- Neumaticos Naturales")
    print("3- Neumaticos Hibridos")
    print("4-Salir")

# noinspection PyUnreachableCode
def calculodeneumatico():
    nombre = input("Digite su nombre completo")
    while True:
        menu()
        x = int(input("Elige uno de los numeros de nuestro menu"))
        y = int(input("\t Digite la cantidad de neumaticos que desea comprar\t"))
        continue
        if x == "1":
            # noinspection PyTypeChecker
            if y <= 10:
                x=costoSintetico
                costoSintetico *= y
                costoSintetico= costo_sin_porcentaje_sintetico
                print("El costo de los neumaticos sinteticos fue menor o igual de 10 por lo tanto el precio es", end="")
                print(costo_sin_porcentaje_sintetico)
            if y > 10:
                costo_con_descuento_sintetico = costo_sin_porcentaje_sintetico * 0.05
                print("El monto de descuento que se le aplicaria es", costo_con_descuento_sintetico)
        if x == "2":
            if y <= 10:
                costo_sin_porcentaje_naturales = costoNaturales * y
            print("El costo de los neumaticos naturales fue menor o igual de 10 por lo tanto el precio es", end="")
            print(costo_sin_porcentaje_naturales)
            if y > 10:
                    costo_con_descuento_naturales = costo_sin_porcentaje_naturales * 0.10
            print("El monto de descuento que se le aplicaria es", costo_con_descuento_naturales)
        if x == "3":
            if y <= 10:
                costo_sin_porcentaje_hibridos = costoHibridos * y
            print("El costo de los neumaticos hibridos fue menor o igual de 10 por lo tanto el precio es", end="")
            print(costo_sin_porcentaje_hibridos)
            if y > 10:
                costo_con_descuento_hibridos = costo_sin_porcentaje_hibridos * 0.07
            print("El monto de descuento que se le aplicaria es", costo_con_descuento_hibridos)
        else:
            print("Hasta pronto y gracias por visitarnos")
            break








saludo()
descripción()
calculodeneumatico()
