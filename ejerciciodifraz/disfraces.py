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

# Llama a la función para verificar la edad
verificar_ingreso()

# Función para verificar la temática del disfraz del usuario
def verificar_tematica():
    # Lista de disfraces permitidos
    temas_permitidos = ["payaso", "fantasma", "zombie"]

    while True:
        # Solicita al usuario que ingrese su disfraz
        disfraz = input("Ingresa de qué vas disfrazado: ")
        
        # Verifica si el disfraz ingresado está en la lista de disfraces permitidos
        if disfraz.lower() in temas_permitidos:
            print("¡Bienvenido a la fiesta!")
            break
        else:
            print("Lo siento, no cumples con los requisitos de ingreso.")

# Llama a la función para verificar el disfraz
verificar_tematica()

# Función para gestionar el número de acompañantes del usuario
def gestionar_acompanantes():
    # Número máximo de acompañantes permitidos
    limite_acompanantes = 3

    while True:
        # Solicita al usuario si llevará acompañantes
        respuesta = input("¿Llevarás acompañantes? (s/n): ").lower()

        # Si la respuesta es 's', solicita el número de acompañantes
        if respuesta == 's':
            num_acompanantes = int(input("¿Cuántos acompañantes llevarás?: "))

            # Verifica si el número de acompañantes es menor o igual al límite
            if num_acompanantes <= limite_acompanantes:
                print(f"¡Bienvenido! Traerás a {num_acompanantes} acompañantes.")
                break
            else:
                print(f"Lo siento, solo puedes traer hasta {limite_acompanantes} acompañantes.")
        elif respuesta == 'n':
            print("¡Bienvenido! No traerás acompañantes.")
            break
        else:
            print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")

# Llama a la función para gestionar acompañantes
gestionar_acompanantes()

# Función para gestionar si el usuario llevará mascotas y cuántas
def mascota():
    # Número máximo de mascotas permitidas
    limite_mascotas = 2 

    while True:
        # Solicita al usuario si llevará mascotas
        respuesta = input("¿Llevarás mascotas? (s/n): ").lower()

        # Si la respuesta es 's', solicita el número de mascotas
        if respuesta == 's':
            num_mascotas = int(input("¿Cuántas mascotas llevarás?: "))

            # Verifica si el número de mascotas es menor o igual al límite
            if num_mascotas <= limite_mascotas:
                print(f"¡Bienvenido! Traerás a {num_mascotas} mascotas.")
                break
            else:
                print(f"Lo siento, solo puedes traer hasta {limite_mascotas} mascotas.")
        elif respuesta == 'n':
            print("¡Bienvenido! No traerás mascotas.")
            break
        else:
            print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")

# Llama a la función para gestionar mascotas
mascota()
