"""Main module for the Gaia Proyectos application."""
from datetime import datetime
def atleta_hibrido(nombre:str, apellido:str, edad:int, ocupacion:str, ruta:str, calificacion:float, opinion:str ):
    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad, 
        "ocupacion": ocupacion,
        "ruta": ruta,
        "calificacion": calificacion,
        "opinion": opinion,
        "creacion": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    usuario["activo"] = True
    return usuario
def print_result(data:dict):
    for key, value in data.items():
        print(f"el {key} es {value}.")
def main():
    print("--- Registro de Atleta Híbrido ---")

    try:
        # Aquí bajamos la sangría para que sea constante (4 espacios)
        nombre_atleta = str(input("Por favor ingresa tu nombre: "))
        apellido_atleta = str(input("Por favor ingresa tu apellido: "))
        edad_atleta = int(input("Por favor ingresa tu edad: "))
        ocupacion_atleta = str(input("Por favor ingresa tu ocupacion: "))
        ruta_atleta = str(input("Por favor ingresa la ruta: "))
        calificacion_atleta = float(input("Por favor ingresa la calificacion: "))
        opinion_atleta = str(input("Por favor da tu opinion: "))
        
        resultado = atleta_hibrido(
            nombre_atleta, apellido_atleta, edad_atleta, 
            ocupacion_atleta, ruta_atleta, calificacion_atleta, 
            opinion_atleta
        )

        print("Registro exitoso:")
        print_result(resultado)

    except ValueError:
        print("Error: Asegúrate de ingresar números en Edad, Calificación y Año.")

if __name__ == "__main__":
    main()