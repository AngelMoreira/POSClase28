carrito = []
total = 0.0

def mostras_menu():
    print("Bienvenido al POS")
    print("1. Agregar producto al carrito")
    print("2. Ver total del carrito")
    print("3. Pagar")
    print("4. Salir")

def agregar_producto():
    global total
    
    producto = input("Ingrese el nombre del producto: ") 
    precio = float(input("Ingrese el precio del producto: "))
    carrito.append({"producto": producto, "precio": precio })
    total += precio
    print(f"Has agregado {producto} al carrito por {precio}.")

agregar_producto()
print(carrito)

mostras_menu()

def ver_total():
    print(f"El total de tu carrito es: {total}")


def pagar():
    global total, carrito
    if total == 0:
        print("Tu carrito esta vacio, no hay nada que pagar. ")
    else:
        print(f"El total a pagar es: {total}")
        pago = float(input("Ingresa la cantidad con la que vas a pagar: "))
        if pago >= total:
            cambio = pago - total
            print(f"Pago realizado con exito: tu cambio es: {cambio}")
            carrito =[]
            total = 0.0
        else:
            print("No tienes suficiente dinero para pagar.")
            

def ejecutar():
    while True:
        mostras_menu()
        opcion = input("Selecciona una opcion: ")
        if opcion == "2":
            ver_total()
        elif opcion == "3":
            pagar()
        elif opcion == "4":
            print("Gracias por usar el POS , ¡hasta luego!")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo")
ejecutar() 