import clientes

DATOS_USUARIOS = "usuarios.json"
DATOS_INSTRUCTORES = "instructores.json"

def menu_principal():
    print("---------- BIENVENIDO -----------")
    print("DriveSafe - te ofrecemos cursos prácticos y teóricos de conducción para motocicletas y automóviles")
    print("Selecciona una de las opciones: ")

    while True:
        print("1. Registro de usuario (cliente/instructor)")
        print("2. Registrar vehículo")
        print("3. Gestión de citas")
        print("4. Historial de práctica")
        print("5. Salir")
        try:
            opcion = int(input("Selcciona una opción (1-5): "))
            if opcion ==1:
                crear_usuario()
            elif opcion ==2:
                print("Registrar vehiculos")
            elif opcion ==3:
                print("Gestión de citas")
            elif opcion ==4:
                print("Historial de prácticas")
            elif opcion ==5:
                print("Saliendo...")
                break
            else:
                print("Opción inválida, intenta nuevamente")
        except ValueError:
            print("Ingresa un dato válido")
        except TypeError as e:
            print(f"Error: {e}")


def crear_usuario():
    print("Vamos a crear un usuario.")
    print("Selecciona una de las opciones: ")
    usuarios = {}
    instructor = {}
    while True:
        print("1. Instructor")
        print("2. Alumno")
        opcion = int(input("Selecciona una opción (1-2): "))
        try:
            if opcion ==1:
                print("opcion instructor")
                nombre_completo = input("Ingrese su nombre completo: ")
                edad = int(input("Ingrese su edad: "))
                documento = int(input("Ingrese su numero de documento: "))
                telefono = int(input("Ingrese su numero telefonico: "))
                especialidad = int(input("Ingrese en que es su especialidad (1. Moto, 2. Carro, 3. ambas)"))
                disponibilidad = int(input("Ingrese su jornada de disponilidad (1. Mañana, 2. tarde, 3. noche)"))

                instructor = {
                        "nombre_completo": nombre_completo,
                        "edad": edad,
                        "especialidad": especialidad,
                        "documento": documento,
                        "telefono": telefono,
                        "disponibilidad": disponibilidad
                }

                datos = clientes.cargar_usuarios(DATOS_INSTRUCTORES)
                datos.append(instructor)
                print(datos)

                clientes.guardar_usuarios("instructores.json",datos)

            elif opcion ==2:
                print("opcion alumno")
                nombre_completo = input("Ingrese su nombre completo: ")
                edad = int(input("Ingrese su edad: "))
                documento = int(input("Ingrese su numero de documento: "))
                telefono = int(input("Ingrese su numero telefonico: "))

                
            else:
                print("Ingresa una opción válida")
        except ValueError:
            print("Ingresa un dato válido")       
        except TypeError as e:
            print(f"Error: {e}")
            print("Ingresa un dato válidooooooooooooooooooooooooo")
    





menu_principal()
#clientes.cargar_usuarios() holaa comooooo estasssss brooo FFFFFF
