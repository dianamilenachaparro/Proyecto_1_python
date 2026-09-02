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
                print("\n -----> Opción inválida, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")
        except TypeError as e:
            print(f"Error: {e}")


def crear_usuario():
    print("Vamos a crear un usuario.")
    print("Selecciona una de las opciones: ")
    usuarios = {}
    instructor = {}
    while True:
        print("1. Crear Instructor")
        print("2. Crear Alumno")
        print("3. Ver listado de instructores")
        print("4. Ver listado de alumnos")
        opcion = int(input("\nSelecciona una opción (1-4): \n"))
        try:
            if opcion ==1:
                print("opcion instructor")
                nombre_completo = input("Ingrese su nombre completo: ")
                while True:
                    try:
                        edad = int(input("Ingrese su edad: "))
                        if 18 <= edad <= 100:
                            break
                        else:
                            print("\n -----> La edad debe estar entre 18 y 100 años, intenta nuevamente\n")
                    except ValueError:
                        print("\n -----> Ingresa un dato válido")
                while True:
                    try:
                        documento = int(input("Ingrese su numero de documento: "))
                        if clientes.documento_existe(DATOS_INSTRUCTORES, documento):
                            print("\n -----> Ya existe un instructor registrado con ese documento, intenta nuevamente\n")
                        else:
                            break
                    except ValueError:
                        print("\n -----> Ingresa un dato válido")
                telefono = int(input("Ingrese su numero telefonico: "))
                while True:
                    try:
                        sexo = int(input("Ingrese su sexo (1. Masculino, 2. Femenino): "))
                        if sexo == 1:
                            sexo = "Masculino"
                            break
                        elif sexo == 2:
                            sexo = "Femenino"
                            break
                        else:
                            print("\n -----> Opción inválida, intenta nuevamente\n")
                    except ValueError:
                        print("\n -----> Ingresa un dato válido\n")
                while True:
                    try:
                        especialidad = int(input("Ingrese en que es su especialidad (1. Moto, 2. Carro, 3. ambas): "))
                        if especialidad == 1:
                            especialidad = "Moto"
                            break
                        elif especialidad == 2:
                            especialidad = "Carro"
                            break
                        elif especialidad == 3:
                            especialidad = "Ambas"
                            break
                        else:
                            print("\n -----> Opción inválida, intenta nuevamente\n")
                    except ValueError:
                        print("\n -----> Ingresa un dato válido\n")

                while True:
                    try:
                        disponibilidad = int(input("Ingrese su jornada de disponilidad (1. Mañana, 2. tarde, 3. noche) "))
                        if disponibilidad == 1:
                            disponibilidad = "Manana"
                            break
                        elif disponibilidad == 2:
                            disponibilidad = "Tarde"
                            break
                        elif disponibilidad == 3:
                            disponibilidad = "Noche"
                            break
                        else:
                            print("\n -----> Opción inválida, intenta nuevamente\n")
                    except ValueError:
                        print("\n -----> Ingresa un dato válido\n")

                instructor = {
                        "nombre_completo": nombre_completo,
                        "edad": edad,
                        "sexo": sexo,
                        "especialidad": especialidad,
                        "documento": documento,
                        "telefono": telefono,
                        "disponibilidad": disponibilidad
                }

                datos = clientes.cargar_usuarios(DATOS_INSTRUCTORES)
                datos.append(instructor)
                print(datos)

                clientes.guardar_usuarios(DATOS_INSTRUCTORES,datos)
                break

            elif opcion ==2:
                print("opcion alumno")
                nombre_completo = input("\nIngrese su nombre completo: ")
                while True:
                    try:
                        edad = int(input("Ingrese su edad: "))
                        if 16 <= edad <= 100:
                            break
                        else:
                            print("\n -----> La edad debe estar entre 16 y 100 años, intenta nuevamente\n")
                    except ValueError:
                        print("\n -----> Ingresa un dato válido\n")
                while True:
                    try:
                        documento = int(input("Ingrese su numero de documento: "))
                        if clientes.documento_existe(DATOS_USUARIOS, documento):
                            print("\n -----> Ya existe un alumno registrado con ese documento, intenta nuevamente\n")
                        else:
                            break
                    except ValueError:
                        print("\n -----> Ingresa un dato válido")
                telefono = int(input("Ingrese su numero telefonico: "))
                while True:
                    try:
                        sexo = int(input("Ingrese su sexo (1. Masculino, 2. Femenino): "))
                        if sexo == 1:
                            sexo = "Masculino"
                            break
                        elif sexo == 2:
                            sexo = "Femenino"
                            break
                        else:
                            print("\n -----> Opción inválida, intenta nuevamente\n")
                    except ValueError:
                        print("\n -----> Ingresa un dato válido\n")

                alumno = {
                        "nombre_completo": nombre_completo,
                        "edad": edad,
                        "sexo": sexo,
                        "documento": documento,
                        "telefono": telefono
                }

                datos = clientes.cargar_usuarios(DATOS_USUARIOS)
                datos.append(alumno)
                print(datos)

                clientes.guardar_usuarios(DATOS_USUARIOS,datos)
                break
            elif opcion ==3:
                print("\n -----> Ver listado de instructores\n")
                datos = clientes.cargar_usuarios(DATOS_INSTRUCTORES)
                for instructor in datos:
                    print(f"Nombre: {instructor['nombre_completo']}, Edad: {instructor['edad']}, Sexo: {instructor['sexo']}, Documento: {instructor['documento']}, Teléfono: {instructor['telefono']}, Disponibilidad: {instructor['disponibilidad']}")
                print("\n -----> Fin del listado de instructores\n")
            elif opcion ==4:
                print("\n -----> Ver listado de alumnos\n")
                datos = clientes.cargar_usuarios(DATOS_USUARIOS)
                for alumno in datos:
                    print(f"Nombre: {alumno['nombre_completo']}, Edad: {alumno['edad']}, Sexo: {alumno['sexo']}, Documento: {alumno['documento']}, Teléfono: {alumno['telefono']}")
                print("\n -----> Fin del listado de alumnos\n")
            else:
                print("\n -----> Ingresa una opción válida\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido")
        except TypeError as e:
            print(f"Error: {e}")
            print("\n -----> Ingresa un dato válidooooooooooooooooooooooooo")
    





menu_principal()
#clientes.cargar_usuarios() holaa comooooo estasssss brooo FFFFFF
