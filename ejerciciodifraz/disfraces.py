# Función para verificar la edad del usuario
def verificar_ingreso():
    while True:
        # Solicita al usuario que ingrese su edad
        edad = int(input("Ingresa tu edad: "))
        
        # Si la edad es 17 o más, permite el acceso
        if edad >= 17:
            print("¡Bienvenido a la fiesta de halloweenparty!")
            break
        else:
            print("Lo siento, no cumples con los requisitos de ingreso.")

# Llama a la funcion para verificar la edad
verificar_ingreso()

# Función para verificar la tematica del disfraz del usuario
def verificar_tematica():
    # Lista de disfraces permitidos
    temas_permitidos = ["payaso", "fantasma", "zombie"]

    while True:
        # Solicita al usuario que ingrese su disfraz
        disfraz = input("Ingresa de qué vas disfrazado: ")
        
        # Verifica si el disfraz ingresado esta en la lista de disfraces permitidos
        if disfraz.lower() in temas_permitidos:
            print("¡Bienvenido a la fiesta!")
            break
        else:
            print("Lo siento, no cumples con los requisitos de ingreso.")

# Llama a la funcion para verificar el disfraz
verificar_tematica()

# Funcion para gestionar el numero de acompanantes del usuario
def gestionar_acompanantes():
    # Numero maximo de acompanantes permitidos
    limite_acompanantes = 3

    while True:
        # Solicita al usuario si llevará acompanantes
        respuesta = input("¿Llevaras acompanantes? (s/n): ").lower()

        # Si la respuesta es 's', solicita el numero de acompanantes
        if respuesta == 's':
            num_acompanantes = int(input("¿Cuantos acompanantes llevaras?: "))

            # Verifica si el número de acompanantes es menor o igual al limite
            if num_acompanantes <= limite_acompanantes:
                print(f"¡Bienvenido! Traeras a {num_acompanantes} acompanantes.")
                break
            else:
                print(f"Lo siento, solo puedes traer hasta {limite_acompanantes} acompanantes.")
        elif respuesta == 'n':
            print("¡Bienvenido! No traerás acompanantes.")
            break
        else:
            print("Respuesta no valida. Por favor, ingresa 's' o 'n'.")

# Llama a la funcion para gestionar acompanantes
gestionar_acompanantes()

# Funcion para gestionar si el usuario llevará mascotas y cuantas
def mascota():
    # Numero maximo de mascotas permitidas
    limite_mascotas = 2 

    while True:
        # Solicita al usuario si llevara mascotas
        respuesta = input("¿Llevaras mascotas? (s/n): ").lower()

        # Si la respuesta es 's', solicita el numero de mascotas
        if respuesta == 's':
            num_mascotas = int(input("¿Cuantas mascotas llevaras?: "))

            # Verifica si el numero de mascotas es menor o igual al límite
            if num_mascotas <= limite_mascotas:
                print(f"¡Bienvenido! Traeras a {num_mascotas} mascotas.")
                break
            else:
                print(f"Lo siento, solo puedes traer hasta {limite_mascotas} mascotas.")
        elif respuesta == 'n':
            print("¡Bienvenido! No traeras mascotas.")
            break
        else:
            print("Respuesta no valida. Por favor, ingresa 's' o 'n'.")

# Llama a la funcion para gestionar mascotas
mascota()

