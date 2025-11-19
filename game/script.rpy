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

    n "..."
    n "..."
    n "..."
    n "La atmosfera se siente fria, incomoda incluso."
    n "Me doy cuenta que... dormi... ¿sentado?"

    scene 1ersalon
    with Dissolve(1.0)

    n "*Bostezo*"
    n "...¿Qué...?"
    n "Me doy cuenta que estoy en un salón de clases."
    n "Pero... no es el de siempre."
    n "No estoy en mi escuela... no es esta."
    n "Todo está... diferente."
    n "Yo no recuerdo...{w=0.5}{cps=15} haber entrado aquí.{/cps}"
    n "{cps=30}Me levanto de la silla y me dirijo a la puerta."
    play sound "audio/puertanoabre.mp3"
    n "{w=3}Está cerrada.{w=0.5} No puedo abrirla."
    n "Giro hacia donde estan las sillas, y veo una nota sobre una de las mesas."
    n "Tomo la nota y la leo."
    show expression Solid("#0008") as overlay
    show hoja at truecenter
    play sound "audio/hoja.mp3"
    with Dissolve(0.5)
    ""
    n "¿Los números?"
    hide hoja
    hide overlay
    with Dissolve(0.5)
    n "¿Es una broma? {w=0.5}¿O es un sueño?"
    n "Volteo al pizarrón y veo que hay algo escrito."
    n "Un problema."
    n "No cualquier problema, es..."
    n "¿Métodos? {w=0.5}¿Métodos numéricos?"
    n "Tuve esa materia hace algunos semestres con la Ingeniera Zamora..."
    n "Me acerco al pizarrón para leer el problema"

    return

