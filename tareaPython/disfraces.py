def verificar_ingreso():
    edad = int(input("Ingresa tu edad: "))
    
    if edad >= 17 :
        print("Bienvenido a la fiesta de halloweenparty")
    else:
        print("Lo siento, no cumples con los requisitos de ingreso.")
verificar_ingreso()

def verificar_tematica():
    disfras = input("Ingresa de que vas disfrasado: ")
    
    if disfras == "payaso" :
        print("Bienvenido a la fiesta ")
    else:
        print("Lo siento, no cumples con los requisitos de ingreso.")
verificar_tematica()

def gestionar_acompanantes():
    limite_acompanantes = 3

    respuesta = input("¿Llevarás acompañantes? (s/n): ")

    if respuesta.lower() == 's':
        num_acompanantes = int(input("¿Cuántos acompañantes llevarás?: "))

        if num_acompanantes <= limite_acompanantes:
            print(f"¡Bienvenido! Traerás a {num_acompanantes} acompañantes.")
        else:
            print(f"Lo siento, solo puedes traer hasta {limite_acompanantes} acompañantes.")
    else:
        print("¡Bienvenido! No traerás acompañantes.")

gestionar_acompanantes()

def mascota():
    limite_mascota = 2 

    respuesta = input("¿Llevarás mascota? (s/n): ")

    if respuesta.lower() == 's':
        num_mascota = int(input("¿Cuántos acompañantes llevarás?: "))

        if num_mascota <= limite_mascota:
            print(f"¡Bienvenido! Traerás a {num_mascota} mascotas.")
        else:
            print(f"Lo siento, solo puedes traer hasta {limite_mascota} mascotas.")
    else:
        print("¡Bienvenido! No traerás mascotas.")

mascota()

