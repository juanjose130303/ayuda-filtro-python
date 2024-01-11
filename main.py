import json

def mostrar_tareas(tareas):
    """
    Función para mostrar todas las tareas en la lista.
    """
    print("Lista de tareas:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea['titulo']} - {tarea['descripcion']}")

def obtener_titulo_descripcion():
    """
    Función para obtener el título y la descripción de una nueva tarea desde el usuario.
    """
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    return titulo, descripcion

def obtener_numero_tarea():
    """
    Función para obtener el número de tarea desde el usuario.
    """
    try:
        return int(input("Ingrese el número de la tarea: ")) - 1
    except ValueError:
        print("Número inválido.")
        return None

def cargar_datos():
    """
    Función para cargar datos desde el archivo JSON 'tareas.json'.
    """
    try:
        with open('tareas.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(tareas):
    """
    Función para guardar datos en el archivo JSON 'tareas.json'.
    """
    with open('tareas.json', 'w') as archivo:
        json.dump(tareas, archivo, indent=2)

def agregar_tarea(tareas):
    """
    Función para agregar una nueva tarea a la lista.
    """
    titulo, descripcion = obtener_titulo_descripcion()
    tarea = {'titulo': titulo, 'descripcion': descripcion}
    tareas.append(tarea)
    guardar_datos(tareas)
    print("Tarea agregada con éxito.")

def actualizar_tarea(tareas):
    """
    Función para actualizar una tarea existente en la lista.
    """
    mostrar_tareas(tareas)
    indice = obtener_numero_tarea()
    if indice is not None and 0 <= indice < len(tareas):
        tarea = tareas[indice]
        nuevo_titulo, nueva_descripcion = obtener_titulo_descripcion()
        # Actualiza la tarea con la nueva información o mantiene la información existente si no se proporciona nueva información.
        tareas[indice] = {'titulo': nuevo_titulo or tarea['titulo'], 'descripcion': nueva_descripcion or tarea['descripcion']}
        guardar_datos(tareas)
        print("Tarea actualizada con éxito.")

def eliminar_tarea(tareas):
    """
    Función para eliminar una tarea de la lista.
    """
    mostrar_tareas(tareas)
    indice = obtener_numero_tarea()
    if indice is not None and 0 <= indice < len(tareas):
        tarea = tareas.pop(indice)
        guardar_datos(tareas)
        print(f"Tarea '{tarea['titulo']}' eliminada con éxito.")

def main():
    """
    Función principal que coordina la ejecución del programa.
    """
    tareas = cargar_datos()

    while True:
        print("\n1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_tareas(tareas)
        elif opcion == '2':
            agregar_tarea(tareas)
        elif opcion == '3':
            actualizar_tarea(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
