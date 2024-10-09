from funciones import *


def mostrar_menu():
    activo = True
    while activo:
        print("\n--- Menú del Sistema de Gestión de Pacientes ---")
        print("1. Cargar pacientes")
        print("2. Mostrar lista de pacientes")
        print("3. Buscar paciente por Historia Clínica")
        print("4. Ordenar pacientes por número de Historia Clínica")
        print("5. Determinar paciente con más días de internación")
        print("6. Determinar paciente con menos días de internación")
        print("7. Pacientes con más de 5 días de internación")
        print("8. Promedio de días de internación")
        print("9. Salir del sistema")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_pacientes(pacientes)
        elif opcion == "2":
            mostrar_pacientes(pacientes)
        elif opcion == "3":
            buscar_paciente(pacientes)
        elif opcion == "4":
            ordenar_pacientes(pacientes)
        elif opcion == "5":
            paciente_mas_dias(pacientes)
        elif opcion == "6":
            paciente_menos_dias(pacientes)
        elif opcion == "7":
            contar_pacientes_mas_de_5_dias(pacientes)
        elif opcion == "8":
            promedio_dias_internacion(pacientes)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

mostrar_menu()