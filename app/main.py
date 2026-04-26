"""Main module for the Gaia Proyectos application."""

def saludo(nombre: str):
    print (f"¡Hola, {nombre}!")
def main():
    """Entry point for the Gaia Proyectos application."""
    #TODO: Pon tu código mágico aquí
def atleta_hibrido(nombre:str, edad:int, ocupacion:str):
    
    usuario= {
        "nombre":nombre,
        "edad": edad,
        "ocupacion": ocupacion

    }
    usuario ["activo"]= True
    return usuario

def main():
    print("--- Registro de Atleta Híbrido ---")

    try:

        nombre_usuario= str(input("COLOCA TU NOMBRE"))
        edad_usuario= int(input("COLOCA TU EDAD"))
        ocupacion_usuario= str(input("COLOCA TU OCUPACION"))
        resultado= atleta_hibrido(nombre_usuario, edad_usuario, ocupacion_usuario)
        print("\nRegistro exitoso:")
        print(resultado)

    except:
        print("Error: La edad debe ser un número.")

# ¡No olvides el interruptor de encendido al final!
if __name__ == "__main__":
    main()