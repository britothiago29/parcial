pacientes = [
    [1234, "Jorge Gomez", 54, "Fiebre", 2],
    [1235, "Ana Perez", 25, "Hipotiroidismo", 5],
    [1236, "Carlos Lopez", 30, "Neumonía", 5],
    [1237, "Ludmila Gonzalez", 22, "Celulitis orbitaria", 10],
]

def verificar_si_hay_pacientes(pacientes):
    """
    Verifica si hay pacientes registrados.

    Si la lista de pacientes está vacia, imprime un mensaje indicando
    que no hay pacientes registrados.

    Args:
        pacientes (list): Lista de pacientes registrados.
    """
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return

def cargar_pacientes(pacientes):
    """
    Carga pacientes en la lista.

    Permite al usuario ingresar los datos de los pacientes y los
    almacena en la lista proporcionada.

    Args:
        pacientes (list): Lista en la que se agregarán los pacientes.
    """
    cantidad = int(input("¿Cuantos pacientes desea ingresar? "))
    for i in range(cantidad):
        numero_historia = int(input("Número de Historia Clínica: "))
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnóstico del paciente: ")
        dias_internacion = int(input("Días de internación: "))
        pacientes.append([numero_historia, nombre, edad, diagnostico, dias_internacion])

def mostrar_paciente(paciente):
    """
    Muestra los detalles de un solo paciente.

    Args:
        paciente (list): Lista con la información de un paciente,
        en el orden de [Numero de Historia Clinica, Nombre, Edad, Diagnostico, Dias de internación].
    """
    print(f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, "
        f"Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")

def mostrar_pacientes(pacientes):
    """
    Muestra todos los pacientes registrados.

    Verifica primero si hay pacientes en la lista, y si los hay,
    imprime los detalles de cada paciente.

    Args:
        pacientes (list): Lista de pacientes registrados.
    """
    verificar_si_hay_pacientes(pacientes)

    for paciente in pacientes:
        mostrar_paciente(paciente)

def buscar_paciente(pacientes):
    """
    Busca un paciente por su numero de historia clinica.

    Permite al usuario ingresar el numero de historia clinica y
    busca en la lista de pacientes, mostrando la información
    del paciente si se encuentra.

    Args:
        pacientes (list): Lista de pacientes registrados.
    """
    verificar_si_hay_pacientes(pacientes)

    encontrado = False
    historia_clinica = int(input("Ingrese el numero de Historia Clínica del paciente que desea buscar: "))
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            mostrar_paciente(paciente)
            encontrado = True
            break

def ordenar_pacientes(pacientes):
    """
    Ordena la lista de pacientes por el numero de historia clinica.

    Utiliza el algoritmo de burbuja para ordenar los pacientes
    en la lista de forma ascendente.

    Args:
        pacientes (list): Lista de pacientes registrados.

    Returns:
        list: Lista de pacientes ordenada por número de historia clinica.
    """
    verificar_si_hay_pacientes(pacientes)

    n = len(pacientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]

    print("Pacientes ordenados por numero de Historia Clinica.")
    for paciente in pacientes:
        mostrar_paciente(paciente)
    return pacientes

def paciente_mas_dias(pacientes):
    """
    Muestra el paciente con la mayor cantidad de días de internación.

    Verifica si hay pacientes registrados y busca el paciente
    con el mayor número de días de internación, mostrando su información.

    Args:
        pacientes (list): Lista de pacientes registrados.
    """
    verificar_si_hay_pacientes(pacientes)

    paciente_con_mas_dias = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > paciente_con_mas_dias[4]:
            paciente_con_mas_dias = paciente
    print(f"paciente con mas dias: {paciente_con_mas_dias}")

def paciente_menos_dias(pacientes):
    """
    Muestra el paciente con la menor cantidad de días de internación.

    Verifica si hay pacientes registrados y busca el paciente
    con el menor número de días de internación, mostrando su información.

    Args:
        pacientes (list): Lista de pacientes registrados.
    """
    verificar_si_hay_pacientes(pacientes)

    paciente_con_menos_dias = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < paciente_con_menos_dias[4]:
            paciente_con_menos_dias = paciente
    print(f"Paciente con menos dias: {paciente_con_menos_dias}")

def contar_pacientes_mas_de_5_dias(pacientes):
    """
    Cuenta la cantidad de pacientes con más de 5 días de internación.

    Verifica si hay pacientes registrados y cuenta cuántos
    pacientes tienen más de 5 días de internación, imprimiendo el resultado.

    Args:
        pacientes (list): Lista de pacientes registrados.
    """
    verificar_si_hay_pacientes(pacientes)

    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1
    print(f"Cantidad de pacientes con más de 5 días de internación: {contador}")

def promedio_dias_internacion(pacientes):
    """
    Calcula y muestra el promedio de días de internación de todos los pacientes.

    Verifica si hay pacientes registrados y calcula el promedio
    de días de internación, imprimiendo el resultado.

    Args:
        pacientes (list): Lista de pacientes registrados.
    """
    verificar_si_hay_pacientes(pacientes)

    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]
    promedio = total_dias / len(pacientes)
    print(f"Promedio de días de internación de los pacientes: {promedio}")
