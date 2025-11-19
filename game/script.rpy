# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define n = Character("")


# El juego comienza aquí.
label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    # Muestra un persaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.


    # Presenta las líneas del diálogo.

    n "..."
    n "..."
    n "..."
    n "La atmosfera se siente fria, incomoda incluso."
    n "Me doy cuenta que... dormi... ¿sentado?"

    scene 1ersalon

    n "*Bostezo*"
    n "...¿Qué...?"
    n "Me doy cuenta que estoy en un salón de clases."
    n "Pero... no es el de siempre."
    n "No estoy en mi escuela... no es esta."
    # Finaliza el juego:

    return
