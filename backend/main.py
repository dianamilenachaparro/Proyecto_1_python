import os
from datetime import date, datetime
import clientes
import vehiculos
import citas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS_DIR = os.path.join(BASE_DIR, "datos")

DATOS_USUARIOS = os.path.join(DATOS_DIR, "usuarios.json")
DATOS_INSTRUCTORES = os.path.join(DATOS_DIR, "instructores.json")
DATOS_VEHICULOS = os.path.join(DATOS_DIR, "vehiculos.json")
DATOS_CITAS = os.path.join(DATOS_DIR, "citas.json")

def menu_principal():
    print("=" * 50)
    print("---------- BIENVENIDO -----------")
    print("DriveSafe - te ofrecemos cursos prácticos y teóricos de conducción para motocicletas y automóviles")
    print("=" * 50)

    while True:
        print()
        print("-" * 50)
        print("1. Registro de usuario (cliente/instructor)")
        print("2. Registrar vehículo")
        print("3. Gestión de citas")
        print("4. Historial de práctica")
        print("5. Salir")
        print("-" * 50)
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            if opcion ==1:
                crear_usuario()
            elif opcion ==2:
                print("\nRegistrar vehiculos")
                crear_vehiculo()
            elif opcion ==3:
                print("\nGestión de citas")
                agendar_cita()
            elif opcion ==4:
                print("\nHistorial de prácticas")
            elif opcion ==5:
                print("\nSaliendo...")
                break
            else:
                print("\n -----> Opción inválida, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")
        except TypeError as e:
            print(f"Error: {e}")


def crear_usuario():
    print("\nVamos a crear un usuario.")
    usuarios = {}
    instructor = {}
    while True:
        print()
        print("-" * 50)
        print("1. Crear Instructor")
        print("2. Crear Alumno")
        print("3. Ver listado de instructores")
        print("4. Ver listado de alumnos")
        print("5. Editar instructor")
        print("6. Editar alumno")
        print("7. Salir")
        print("-" * 50)
        opcion = int(input("Selecciona una opción (1-7): "))
        try:
            if opcion ==1:
                print("\n--- Crear Instructor ---")
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

                clientes.guardar_usuarios(DATOS_INSTRUCTORES,datos)
                print(f"\n -----> Instructor {nombre_completo} registrado correctamente\n")
                break

            elif opcion ==2:
                print("\n--- Crear Alumno ---")
                nombre_completo = input("Ingrese su nombre completo: ")
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
                while True:
                    try:
                        tipo_vehiculo = int(input("Ingrese el tipo de vehiculo (1. Moto, 2. Carro, 3. Ambas): "))
                        if tipo_vehiculo == 1:
                            tipo_vehiculo = "Moto"
                            break
                        elif tipo_vehiculo == 2:
                            tipo_vehiculo = "Carro"
                            break
                        elif tipo_vehiculo == 3:
                            tipo_vehiculo = "Ambas"
                            break
                        else:
                            print("\n -----> Opción inválida, intenta nuevamente\n")
                    except ValueError:
                        print("\n -----> Ingresa un dato válido\n")

                fecha_registro = date.today().isoformat()

                alumno = {
                        "nombre_completo": nombre_completo,
                        "edad": edad,
                        "sexo": sexo,
                        "tipo_vehiculo": tipo_vehiculo,
                        "documento": documento,
                        "telefono": telefono,
                        "fecha_registro": fecha_registro
                }

                datos = clientes.cargar_usuarios(DATOS_USUARIOS)
                datos.append(alumno)

                clientes.guardar_usuarios(DATOS_USUARIOS,datos)
                print(f"\n -----> Alumno {nombre_completo} registrado correctamente\n")
                break
            elif opcion ==3:
                print("\n -----> Ver listado de instructores\n")
                datos = clientes.cargar_usuarios(DATOS_INSTRUCTORES)
                for instructor in datos:
                    print(f"Nombre: {instructor['nombre_completo']}, Edad: {instructor['edad']}, Sexo: {instructor.get('sexo', 'No especificado')}, Documento: {instructor['documento']}, Teléfono: {instructor['telefono']}, Disponibilidad: {instructor['disponibilidad']}")
                print("\n -----> Fin del listado de instructores\n")
            elif opcion ==4:
                print("\n -----> Ver listado de alumnos\n")
                datos = clientes.cargar_usuarios(DATOS_USUARIOS)
                for alumno in datos:
                    print(f"Nombre: {alumno['nombre_completo']}, Edad: {alumno['edad']}, Sexo: {alumno.get('sexo', 'No especificado')}, Tipo de vehículo: {alumno.get('tipo_vehiculo', 'No especificado')}, Documento: {alumno['documento']}, Teléfono: {alumno['telefono']}, Fecha de registro: {alumno.get('fecha_registro', 'No especificado')}")
                print("\n -----> Fin del listado de alumnos\n")
            elif opcion ==5:
                print("\n -----> Editar instructor\n")
                documento = int(input("Ingrese el documento del instructor a editar: "))
                datos = clientes.cargar_usuarios(DATOS_INSTRUCTORES)
                for i, instructor in enumerate(datos):
                    if instructor["documento"] == documento:
                        print(f"Nombre: {instructor['nombre_completo']}, Edad: {instructor['edad']}, Sexo: {instructor.get('sexo', 'No especificado')}, Especialidad:{instructor['especialidad']}, Documento: {instructor['documento']}, Teléfono: {instructor['telefono']}, Disponibilidad: {instructor['disponibilidad']}")

                        nombre_completo = input("Ingrese el nuevo nombre completo (dejar en blanco para no cambiar): ")
                        edad = input("Ingrese la nueva edad (dejar en blanco para no cambiar): ")
                        sexo = input("Ingrese el nuevo sexo (1. Masculino, 2. Femenino) (dejar en blanco para no cambiar): ")
                        especialidad = input("Ingrese la nueva especialidad (1. Moto, 2. Carro, 3. ambas) (dejar en blanco para no cambiar): ")
                        telefono = input("Ingrese el nuevo teléfono (dejar en blanco para no cambiar): ")
                        disponibilidad = input("Ingrese la nueva disponibilidad (1. Mañana, 2. Tarde, 3. Noche) (dejar en blanco para no cambiar): ")

                        if nombre_completo:
                            instructor["nombre_completo"] = nombre_completo
                            print(f"Nombre actualizado a: {instructor['nombre_completo']}")

                        if edad:
                            instructor["edad"] = int(edad)
                            print(f"Edad actualizada a: {instructor['edad']}")

                        if sexo:
                            if sexo == "1":
                                instructor["sexo"] = "Masculino"
                            elif sexo == "2":
                                instructor["sexo"] = "Femenino"
                            print(f"Sexo actualizado a: {instructor['sexo']}")
                        if especialidad:
                            if especialidad == "1":
                                instructor["especialidad"] = "Moto"
                            elif especialidad == "2":
                                instructor["especialidad"] = "Carro"
                            elif especialidad == "3":
                                instructor["especialidad"] = "Ambas"
                            print(f"Especialidad actualizada a: {instructor['especialidad']}")
                        if telefono:
                            instructor["telefono"] = int(telefono)
                            print(f"Teléfono actualizado a: {instructor['telefono']}")
                        if disponibilidad:
                            if disponibilidad == "1":
                                instructor["disponibilidad"] = "Manana"
                            elif disponibilidad == "2":
                                instructor["disponibilidad"] = "Tarde"
                            elif disponibilidad == "3":
                                instructor["disponibilidad"] = "Noche"
                            print(f"Disponibilidad actualizada a: {instructor['disponibilidad']}")
                        # Guardar los cambios en el archivo JSON
                        clientes.actualizar_usuario(DATOS_INSTRUCTORES, documento, instructor)
            elif opcion ==6:
                print("\n -----> Editar alumno\n")
                documento = int(input("Ingrese el documento del alumno a editar: "))
                datos = clientes.cargar_usuarios(DATOS_USUARIOS)
                for i, alumno in enumerate(datos):
                    if alumno["documento"] == documento:
                        print(f"Nombre: {alumno['nombre_completo']}, Edad: {alumno['edad']}, Sexo: {alumno.get('sexo', 'No especificado')}, Tipo de vehículo: {alumno.get('tipo_vehiculo', 'No especificado')}, Documento: {alumno['documento']}, Teléfono: {alumno['telefono']}, Fecha de registro: {alumno.get('fecha_registro', 'No especificado')}")

                        nombre_completo = input("Ingrese el nuevo nombre completo (dejar en blanco para no cambiar): ")
                        edad = input("Ingrese la nueva edad (dejar en blanco para no cambiar): ")
                        sexo = input("Ingrese el nuevo sexo (1. Masculino, 2. Femenino) (dejar en blanco para no cambiar): ")
                        tipo_vehiculo = input("Ingrese el nuevo tipo de vehiculo (1. Moto, 2. Carro, 3. Ambas) (dejar en blanco para no cambiar): ")
                        telefono = input("Ingrese el nuevo teléfono (dejar en blanco para no cambiar): ")

                        if nombre_completo:
                            alumno["nombre_completo"] = nombre_completo
                            print(f"Nombre actualizado a: {alumno['nombre_completo']}")

                        if edad:
                            alumno["edad"] = int(edad)
                            print(f"Edad actualizada a: {alumno['edad']}")

                        if sexo:
                            if sexo == "1":
                                alumno["sexo"] = "Masculino"
                            elif sexo == "2":
                                alumno["sexo"] = "Femenino"
                            print(f"Sexo actualizado a: {alumno['sexo']}")

                        if tipo_vehiculo:
                            if tipo_vehiculo == "1":
                                alumno["tipo_vehiculo"] = "Moto"
                            elif tipo_vehiculo == "2":
                                alumno["tipo_vehiculo"] = "Carro"
                            elif tipo_vehiculo == "3":
                                alumno["tipo_vehiculo"] = "Ambas"
                            print(f"Tipo de vehículo actualizado a: {alumno['tipo_vehiculo']}")

                        if telefono:
                            alumno["telefono"] = int(telefono)
                            print(f"Teléfono actualizado a: {alumno['telefono']}")

                        # Guardar los cambios en el archivo JSON
                        clientes.actualizar_usuario(DATOS_USUARIOS, documento, alumno)
            elif opcion ==7:
                print("\nSaliendo...")
                break
            else:
                print("\n -----> Ingresa una opción válida\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido")
        except TypeError as e:
            print(f"Error: {e}")
            print("\n -----> Ingresa un dato válido")


def crear_vehiculo():
    print("\nVamos a crear un vehiculo.")
    vehiculo = {}
    while True:
        print()
        print("-" * 50)
        print("1. Crear Vehiculo")
        print("2. Ver listado de vehiculos")
        print("3. Salir")
        print("-" * 50)
        opcion = int(input("Selecciona una opción (1-3): "))
        try:
            if opcion ==1:
                print("\n--- Crear Vehiculo ---")
                tipo = input("Ingrese el tipo de vehiculo (1. Moto/2. Carro): ")
                if tipo == "1":
                    tipo = "Moto"
                elif tipo == "2":
                    tipo = "Carro"
                else:
                    print("\n -----> Opción inválida, intenta nuevamente\n")
                    continue
                marca = input("Ingrese la marca del vehiculo: ")
                modelo = input("Ingrese el modelo del vehiculo: ")
                while True:
                    try:
                        placa = input("Ingrese la placa del vehiculo: ")
                        if vehiculos.leer_vehiculo_por_placa(DATOS_VEHICULOS, placa):
                            print("\n -----> Ya existe un vehiculo registrado con esa placa, intenta nuevamente\n")
                        else:
                            break
                    except ValueError:
                        print("\n -----> Ingresa un dato válido")


                vehiculo = {
                        "marca": marca,
                        "modelo": modelo,
                        "placa": placa,
                        "tipo": tipo,
                        "estado": "Disponible",
                }

                datos = vehiculos.cargar_vehiculos(DATOS_VEHICULOS)
                datos.append(vehiculo)

                vehiculos.guardar_vehiculos(DATOS_VEHICULOS,datos)
                print(f"\n -----> Vehículo {marca} {modelo} ({placa}) registrado correctamente\n")
                break
            elif opcion ==2:
                print("\n -----> Ver listado de vehiculos\n")
                datos = vehiculos.cargar_vehiculos(DATOS_VEHICULOS)
                for vehiculo in datos:
                    print(f"Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Placa: {vehiculo['placa']}, Tipo: {vehiculo['tipo']}, Estado: {vehiculo['estado']}")
                print("\n -----> Fin del listado de vehiculos\n")
            elif opcion ==3:
                print("\nSaliendo...")
                break
            else:
                print("\n -----> Ingresa una opción válida\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido")
        except TypeError as e:
            print(f"Error: {e}")
            print("\n -----> Ingresa un dato válido")

def _pedir_fecha(mensaje):
    while True:
        texto = input(mensaje)
        try:
            fecha_dt = datetime.strptime(texto, "%Y-%m-%d").date()
            if fecha_dt < date.today():
                print("\n -----> La fecha no puede ser anterior a hoy, intenta nuevamente\n")
                continue
            return fecha_dt.isoformat()
        except ValueError:
            print("\n -----> Formato inválido, usa AAAA-MM-DD\n")


def _pedir_jornada():
    while True:
        try:
            jornada = int(input("Seleccione la jornada (1. Mañana, 2. Tarde, 3. Noche): "))
            if jornada == 1:
                return "Manana"
            elif jornada == 2:
                return "Tarde"
            elif jornada == 3:
                return "Noche"
            else:
                print("\n -----> Opción inválida, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")


def _pedir_tipo_vehiculo():
    while True:
        try:
            tipo = int(input("Seleccione el tipo de vehículo (1. Moto, 2. Carro): "))
            if tipo == 1:
                return "Moto"
            elif tipo == 2:
                return "Carro"
            else:
                print("\n -----> Opción inválida, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")


def _pedir_documento_alumno():
    while True:
        try:
            documento = int(input("Ingrese el documento del alumno: "))
            if clientes.documento_existe(DATOS_USUARIOS, documento):
                return documento
            else:
                print("\n -----> No existe un alumno registrado con ese documento, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")


def programar_cita():
    print("\n--- Programar Cita ---")
    documento_alumno = _pedir_documento_alumno()
    alumno = next(a for a in clientes.cargar_usuarios(DATOS_USUARIOS) if a["documento"] == documento_alumno)

    fecha = _pedir_fecha("Ingrese la fecha de la cita (AAAA-MM-DD): ")

    tipo_vehiculo_alumno = alumno.get("tipo_vehiculo")
    if tipo_vehiculo_alumno in ("Moto", "Carro"):
        tipo_vehiculo = tipo_vehiculo_alumno
        print(f"Tipo de vehículo: {tipo_vehiculo} (preestablecido para este alumno)")
    else:
        tipo_vehiculo = _pedir_tipo_vehiculo()

    jornada = _pedir_jornada()

    instructores = clientes.cargar_usuarios(DATOS_INSTRUCTORES)
    disponibles = [
        instructor for instructor in instructores
        if instructor.get("disponibilidad") == jornada
        and instructor.get("especialidad") in (tipo_vehiculo, "Ambas")
        and not citas.instructor_ocupado(DATOS_CITAS, instructor["documento"], fecha, jornada)
    ]

    if not disponibles:
        print("\n -----> No hay instructores disponibles para esa fecha, jornada y tipo de vehículo\n")
        return

    print(f"\nInstructores disponibles para {fecha} - {jornada} - {tipo_vehiculo}:")
    for indice, instructor in enumerate(disponibles, start=1):
        print(f"  {indice}. {instructor['nombre_completo']} (Documento: {instructor['documento']}, Especialidad: {instructor['especialidad']})")

    while True:
        try:
            seleccion = int(input("Seleccione el instructor (número): "))
            if 1 <= seleccion <= len(disponibles):
                instructor = disponibles[seleccion - 1]
                break
            else:
                print("\n -----> Opción inválida, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")

    vehiculos_todos = vehiculos.cargar_vehiculos(DATOS_VEHICULOS)
    vehiculos_disponibles = [
        v for v in vehiculos_todos
        if v.get("tipo") == tipo_vehiculo
        and v.get("estado") == "Disponible"
        and not citas.vehiculo_ocupado(DATOS_CITAS, v["placa"], fecha, jornada)
    ]

    if not vehiculos_disponibles:
        print("\n -----> No hay vehículos disponibles para ese tipo, fecha y jornada\n")
        return

    print(f"\nVehículos disponibles ({tipo_vehiculo}):")
    for indice, v in enumerate(vehiculos_disponibles, start=1):
        print(f"  {indice}. {v['marca']} {v['modelo']} - Placa: {v['placa']}")

    while True:
        try:
            seleccion = int(input("Seleccione el vehículo (número): "))
            if 1 <= seleccion <= len(vehiculos_disponibles):
                vehiculo = vehiculos_disponibles[seleccion - 1]
                break
            else:
                print("\n -----> Opción inválida, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")

    cita = {
        "id": citas.siguiente_id(DATOS_CITAS),
        "fecha": fecha,
        "jornada": jornada,
        "tipo_vehiculo": tipo_vehiculo,
        "documento_alumno": documento_alumno,
        "nombre_alumno": alumno["nombre_completo"],
        "documento_instructor": instructor["documento"],
        "nombre_instructor": instructor["nombre_completo"],
        "placa_vehiculo": vehiculo["placa"],
        "estado": "Programada",
        "asistencia": None,
        "observaciones": ""
    }

    datos = citas.cargar_citas(DATOS_CITAS)
    datos.append(cita)
    citas.guardar_citas(DATOS_CITAS, datos)
    print(f"\n -----> Cita #{cita['id']} programada con {instructor['nombre_completo']} (vehículo {vehiculo['placa']}) el {fecha} ({jornada})\n")


def _imprimir_cita(cita):
    print(f"  #{cita['id']} | Fecha: {cita['fecha']} | Jornada: {cita['jornada']} | Vehículo: {cita['tipo_vehiculo']} ({cita.get('placa_vehiculo', 'No especificado')}) | "
          f"Alumno: {cita['nombre_alumno']} ({cita['documento_alumno']}) | Instructor: {cita['nombre_instructor']} | "
          f"Estado: {cita['estado']} | Asistencia: {cita.get('asistencia') or 'Pendiente'} | Observaciones: {cita.get('observaciones') or '-'}")


def consultar_citas():
    print("\n--- Consultar Citas ---")
    print("1. Por cliente (documento)")
    print("2. Por fecha")
    try:
        opcion = int(input("Seleccione una opción (1-2): "))
    except ValueError:
        print("\n -----> Ingresa un dato válido\n")
        return

    datos = citas.cargar_citas(DATOS_CITAS)
    if opcion == 1:
        documento = _pedir_documento_alumno()
        resultado = [c for c in datos if c["documento_alumno"] == documento]
    elif opcion == 2:
        fecha = input("Ingrese la fecha a consultar (AAAA-MM-DD): ")
        resultado = [c for c in datos if c["fecha"] == fecha]
    else:
        print("\n -----> Ingresa una opción válida\n")
        return

    if not resultado:
        print("\n -----> No se encontraron citas\n")
        return

    print()
    for cita in resultado:
        _imprimir_cita(cita)
    print()


def registrar_asistencia():
    print("\n--- Registrar Asistencia y Observaciones ---")
    datos = citas.cargar_citas(DATOS_CITAS)
    pendientes = [c for c in datos if c.get("asistencia") is None]

    if not pendientes:
        print("\n -----> No hay citas pendientes de registrar\n")
        return

    print("\nCitas pendientes:")
    for cita in pendientes:
        _imprimir_cita(cita)

    try:
        id_cita = int(input("\nIngrese el número de la cita a registrar: "))
    except ValueError:
        print("\n -----> Ingresa un dato válido\n")
        return

    cita = citas.leer_cita_por_id(DATOS_CITAS, id_cita)
    if cita is None or cita.get("asistencia") is not None:
        print("\n -----> No se encontró una cita pendiente con ese número\n")
        return

    while True:
        try:
            asistio = int(input("¿El alumno asistió? (1. Sí, 2. No): "))
            if asistio == 1:
                cita["asistencia"] = "Asistió"
                break
            elif asistio == 2:
                cita["asistencia"] = "No asistió"
                break
            else:
                print("\n -----> Opción inválida, intenta nuevamente\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido\n")

    cita["observaciones"] = input("Ingrese observaciones (opcional): ")
    cita["estado"] = "Realizada"
    citas.actualizar_cita(DATOS_CITAS, id_cita, cita)
    print(f"\n -----> Asistencia registrada para la cita #{id_cita}\n")


def agendar_cita():
    print("\nVamos a agendar una cita.")
    while True:
        print()
        print("-" * 50)
        print("1. Programar cita")
        print("2. Consultar citas (por cliente / por fecha)")
        print("3. Registrar asistencia y observaciones")
        print("4. Salir")
        print("-" * 50)
        opcion = int(input("Selecciona una opción (1-4): "))
        try:
            if opcion ==1:
                programar_cita()
            elif opcion ==2:
                consultar_citas()
            elif opcion ==3:
                registrar_asistencia()
            elif opcion ==4:
                print("\nSaliendo...")
                break
            else:
                print("\n -----> Ingresa una opción válida\n")
        except ValueError:
            print("\n -----> Ingresa un dato válido")
        except TypeError as e:
            print(f"Error: {e}")
            print("\n -----> Ingresa un dato válido")

menu_principal()
