"Ejercicio feedback Abel fernandez Martinez"

clientes = {}

def añadir_cliente():
    nif = input("Ingrese el NIF del cliente: ")
    if len(nif) != 9 or not nif[:-1].isdigit():
        print("El NIF ingresado no es válido.")
        return

    datos_cliente = {}
    datos_cliente["apellidos y nombre"] = input("Ingrese los apellidos y nombre del cliente: ")
    datos_cliente["dirección"] = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    if len(telefono) != 9 or not telefono.isdigit():
        print("El teléfono ingresado no es válido.")
        return
    datos_cliente["teléfono"] = telefono
    datos_cliente["correo electrónico"] = input("Ingrese el correo electrónico del cliente: ")
    cliente_habitual = input("¿Es cliente habitual? (si/no): ")
    if cliente_habitual.lower() == "si":
        datos_cliente["cliente habitual"] = True
    else:
        datos_cliente["cliente habitual"] = False
    datos_cliente["fecha de la operación"] = input("Ingrese la fecha de la operación ('dd/mm/yyyy'): ")

    clientes[nif] = datos_cliente
    print("Cliente agregado exitosamente.")

def eliminar_cliente():
    nif = input("Ingrese el NIF del cliente que desea eliminar: ")
    if nif in clientes:
        del clientes[nif]
        print("Cliente eliminado exitosamente.")
    else:
        print("No existe un cliente con ese NIF en la base de datos.")

def mostrar_cliente():
    nif = input("Ingrese el NIF del cliente que desea mostrar: ")
    if nif in clientes:
        datos_cliente = clientes[nif]
        print("Datos del cliente:")
        for clave, valor in datos_cliente.items():
            print(clave + ": " + str(valor))
    else:
        print("No existe un cliente con ese NIF en la base de datos.")

def listar_clientes():
    print("Listado de todos los clientes:")
    for nif, datos_cliente in clientes.items():
        print("NIF:", nif)
        print("Nombre:", datos_cliente["apellidos y nombre"])
        print()

def listar_clientes_habituales():
    print("Listado de clientes habituales:")
    for nif, datos_cliente in clientes.items():
        if datos_cliente["cliente habitual"]:
            print("NIF:", nif)
            print("Nombre:", datos_cliente["apellidos y nombre"])
            print()

while True:
    print("Menú:")
    print("1) Añadir cliente")
    print("2) Eliminar cliente")
    print("3) Mostrar cliente")
    print("4) Listar todos los clientes")
    print("5) Listar clientes habituales")
    print("6) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        añadir_cliente()
    elif opcion == "2":
        eliminar_cliente()
    elif opcion == "3":
        mostrar_cliente()
    elif opcion == "4":
        listar_clientes()
    elif opcion == "5":
        listar_clientes_habituales()
    elif opcion == "6":
        break
    else:
        print("¡Opción no válida! Por favor, seleccione una opción del menú nuevamente.")
