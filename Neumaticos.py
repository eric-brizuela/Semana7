#declaracion de variables

sinteticos = ""
hibridos = ""
naturales = ""
precio = 0
cantidad = 0
descuento = 0
subtotal = 0
iva = 0
monto_final = 0

#definicion de funciones

def sinteticos():
  precio = 12000
  if cantidad < 10:
    descuento = 0
    subtotal = cantidad * precio
    iva = subtotal * 0.13
    monto_final = subtotal + iva
  elif cantidad > 10:
    descuento = 0.95
    subtotal = (cantidad * precio) * descuento
    iva = subtotal * 0.13
    monto_final = subtotal + iva

#factura
  print("\nGracias por su compra. A continuación, su factura:\nTipo.............. Sintéticos\nCantidad..........",cantidad,"\nSubtotal..........",subtotal,"\nDescuento.........",descuento,"\nIVA...............",iva,"\nMonto por Pagar...",monto_final)
    
def hibridos():
  precio = 25000
  if cantidad < 10:
    descuento = 0
    subtotal = cantidad * precio
    iva = subtotal * 0.13
    monto_final = subtotal + iva
  elif cantidad > 10:
    descuento = 0.90
    subtotal = (cantidad * precio) * descuento
    iva = subtotal * 0.13
    monto_final = subtotal + iva

#factura
  print("\nGracias por su compra. A continuación, su factura:\nTipo.............. Híbridos\nCantidad..........",cantidad,"\nSubtotal..........",subtotal,"\nDescuento.........",descuento,"\nIVA...............",iva,"\nMonto por Pagar...",monto_final)

def naturales():
  precio = 45000
  if cantidad < 8:
    descuento = 0
    subtotal = cantidad * precio
    iva = subtotal * 0.13
    monto_final = subtotal + iva
  elif cantidad > 8:
    descuento = 0.93
    subtotal = (cantidad * precio) * descuento
    iva = subtotal * 0.13
    monto_final = subtotal + iva

#factura
  print("\nGracias por su compra. A continuación, su factura:\nTipo.............. Naturales\nCantidad..........",cantidad,"\nSubtotal..........",subtotal,"\nDescuento.........",descuento,"\nIVA...............",iva,"\nMonto por Pagar...",monto_final)

#programa

while True:
  menu = input("\nGracias por utilizar nuestro programa. A continuación, el menú de opciones: \n\n1. Comprar neumáticos. \n2. Salir. \n\nDigite el número de la opción que desea ejecutar: \n")

  if menu == "1":

    tipo = input("\nDe acuerdo. A continuación podrá seleccionar el tipo de neumáticos que desea comprar:\n\n1. Digite '1' para neumáticos sintéticos.\n2. Digite '2' para neumaticos híbridos.\n3. Digite '3' para neumáticos naturales.\n")
    
    cantidad = int(input("\nDigite la cantidad de neumáticos que desea comprar: \n"))

    if tipo == "1":
      sinteticos()

    elif tipo == "2":
      hibridos()

    elif tipo == "3":
      naturales()  

  else:
    break
  



  


  
