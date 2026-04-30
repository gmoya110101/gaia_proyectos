"""Main module for the Gaia Proyectos application."""


def insert_persistent_data(nombre: str, edad: int, ocupacion: str):

    usuario = {"nombre": nombre, "edad": edad, "ocupacion": ocupacion}
    usuario["activo"] = True
    return usuario


def input_user_data() -> None:
    print("--- Registro de Atleta Híbrido ---")

    try:

        nombre_usuario = str(input("COLOCA TU NOMBRE"))
        edad_usuario = int(input("COLOCA TU EDAD"))
        ocupacion_usuario = str(input("COLOCA TU OCUPACION"))
        resultado = insert_persistent_data(
            nombre_usuario, edad_usuario, ocupacion_usuario
        )
        print("\nRegistro exitoso:")
        print(resultado)

    except:
        print("Error: La edad debe ser un número.")


def main():
    input_user_data()


if __name__ == "__main__":
    main()
