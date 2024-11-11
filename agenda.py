# Agenda de contactos
def agenda():
    myAgenda = {}

    def addNewContact(name):
        phone = input("Ingresar número de teléfono: ")
        if len(phone) > 0 and len(phone) <= 11:
            myAgenda[name] = phone
        else:
            print("El número no debe ser mayor a 11 caracteres.")

    def searchContactByName(name):
        if name in myAgenda:
            print(f"{name}: {myAgenda[name]}")
        else:
            print(f"No existe un contacto con el nombre {name}")

    def listAllContacts():
        for name, phone in myAgenda.items():
            print(f"{name} -> {phone}")

    def deleteContact(name):
        if name in myAgenda:
            del myAgenda[name]
            print(f"Contacto {name} eliminado.")
        else:
            print(f"No existe un contacto con el nombre {name}")

    while True:
        print(
            """
            AGENDA:
            1. Agregar contacto
            2. Buscar contacto
            3. Actualizar contacto
            4. Eliminar contacto
            5. Lista de contactos
            6. Salir
            """
        )
        option = input("Escoger una opción del menú: ")

        match option:
            case "1":
                name = input("Introduzca el nombre del contacto: ")
                addNewContact(name)
            case "2":
                name = input("Introduzca el nombre del contacto a buscar: ")
                searchContactByName(name)
            case "3":
                name = input("Introduzca el nombre del contacto a actualizar: ")
                if name in myAgenda:
                    addNewContact(name)  # Actualiza el número
                else:
                    print(f"No existe un contacto con el nombre {name}")
            case "4":
                name = input("Introduzca el nombre del contacto a eliminar: ")
                deleteContact(name)
            case "5":
                listAllContacts()
            case "6":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

agenda()