# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define name = ""
# Ya no usamos "n" fijo, lo crearemos dinámicamente
default player_name = ""
default tiempo = 21600  # tiempo total en segundos
default tiempo_restante = 21600  # tiempo que va bajando
default tiempo_activo = False  # si el cronómetro está activo

# ------------------------------
# SISTEMA DE PROBLEMAS ALEATORIOS - 1 PROBLEMA POR NIVEL
# ------------------------------

# Base de datos de problemas - cada nivel tiene múltiples problemas
# Se selecciona UNO aleatorio por nivel
default problems = {
    "Interpolacion": {
        "total_problemas": 5,  # Cuántos problemas hay en la carpeta
        "respuestas": {
            1: {"respuesta1": "4.99", "respuesta2": "4"},
            2: {"respuesta1": "5.0", "respuesta2": "2"},
            3: {"respuesta1": "3.14", "respuesta2": "1"},
            4: {"respuesta1": "2.71", "respuesta2": "3"},
            5: {"respuesta1": "1.41", "respuesta2": "2"},
        }
    },
    "Integracion": {
        "total_problemas": 4,
        "respuestas": {
            1: {"respuesta1": "10", "respuesta2": "5"},
            2: {"respuesta1": "20", "respuesta2": "10"},
            3: {"respuesta1": "15", "respuesta2": "7"},
            4: {"respuesta1": "25", "respuesta2": "12"},
        }
    },
    "EDO": {
        "total_problemas": 3,
        "respuestas": {
            1: {"respuesta1": "100", "respuesta2": "50"},
            2: {"respuesta1": "150", "respuesta2": "75"},
            3: {"respuesta1": "200", "respuesta2": "100"},
        }
    },
    "Minimos Cuadrados": {
        "total_problemas": 3,
        "respuestas": {
            1: {"respuesta1": "100", "respuesta2": "50"},
            2: {"respuesta1": "150", "respuesta2": "75"},
            3: {"respuesta1": "200", "respuesta2": "100"},
        }
    },
    "Ecuaciones No Lineales": {
        "total_problemas": 3,
        "respuestas": {
            1: {"respuesta1": "100", "respuesta2": "50"},
            2: {"respuesta1": "150", "respuesta2": "75"},
            3: {"respuesta1": "200", "respuesta2": "100"},
        }
    },
    "Ecuaciones Lineales": {
        "total_problemas": 3,
        "respuestas": {
            1: {"respuesta1": "100", "respuesta2": "50"},
            2: {"respuesta1": "150", "respuesta2": "75"},
            3: {"respuesta1": "200", "respuesta2": "100"},
        }
    },
    # Agrega más niveles/carpetas aquí con el mismo formato
}

# Variables de control
default niveles_disponibles = []
default niveles_completados = []
default current_level = ""
default current_problem_index = 0
default total_niveles = 0
default player_answer1 = ""
default player_answer2 = ""



# El juego comienza aquí.
label start:

    # Muestra el cuadro de entrada para el nombre
    call screen name_input
    
    # Verificar si el jugador dejó el nombre vacío
    if player_name == "":
        $ player_name = "Jugador"
    
    # Crear el personaje con el nombre del jugador
    $ n = Character("[player_name]")

    # Inicializar niveles aleatorios
    $ inicializar_niveles_aleatorios()
    $ seleccionar_problema_aleatorio()

    # ACTIVAR EL CRONÓMETRO DESDE EL INICIO
    $ tiempo_activo = True
    $ tiempo_restante = tiempo

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
    n "...La puerta tiene tres candados."
    n "No entiendo porqué tendrian tanta seguridad para que no salga..."
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
    
    # Mostrar el problema actual
    $ mostrar_problema_actual()
    
    n ""
    n "A lado del pizarrón hay una especie de teclado con números, supongo que para escribir la respuesta."
    n "Quiero pensar que al resolver este problema podré salir de aquí."
    n "Convenientemente, hay una libreta en una de las mesas."
    n "La usare para poder resolver... {w=0.5}eso."
    
    # Ya no es necesario activar el cronómetro aquí, ya está activo desde el inicio
    
    window hide
    $ _window = False
    hide problem_image
    with Dissolve(0.5)
    show screen ver_problema
    show screen cronometro  # Mostrar el cronómetro
    show screen distorsion_cordura  # Mostrar efectos de distorsión
    with Dissolve(0.5)
    
    # Pausa infinita esperando que el jugador resuelva
    pause
    
label continue_problema1:
    # Ocultar pantallas de problema
    hide screen ver_problema
    hide screen ingresar_respuesta
    hide screen ver_problem
    play sound "audio/click.mp3"
    n "Escuche un click"
    n "Un candado se abrió."
    
    
    # Marcar nivel como completado
    $ niveles_completados.append(current_level)
    # Verificar si quedan niveles por completar
    if len(niveles_completados) < total_niveles:
        n "Aun faltan candados..."
        n "Noto que a lado del problema que resolvi hay otro problema nuevo."
        
        # Seleccionar siguiente nivel aleatorio
        $ seleccionar_siguiente_nivel()
        $ seleccionar_problema_aleatorio()
        $ mostrar_problema_actual()
        
        n "Este es... ¿[current_level]?"
        
        window hide
        $ _window = False
        hide problem_image
        with Dissolve(0.5)
        show screen ver_problema
        show screen cronometro  # Asegurar que el cronómetro se muestre
        show screen distorsion_cordura  # Asegurar efectos de distorsión
        with Dissolve(0.5)
        
        # Pausa infinita esperando que el jugador resuelva
        pause
    else:
        # DESACTIVAR CRONÓMETRO AL GANAR
        $ tiempo_activo = False
        hide screen cronometro
        hide screen distorsion_cordura  # Quitar distorsión al ganar
        
        n "¡Lo has logrado!"
        n "Completaste todos los niveles: [', '.join(niveles_completados)]"
        n "Las puertas se abren... finalmente puedo salir..."
        return

# ------------------------------
# GAME OVER POR TIEMPO
# ------------------------------

label game_over_tiempo:
    # Asegurar que el tiempo esté desactivado
    $ tiempo_activo = False
    
    # Ocultar TODAS las pantallas
    hide screen cronometro
    hide screen distorsion_cordura
    hide screen ver_problema
    hide screen ingresar_respuesta
    hide screen ver_problem
    
    # Detener música actual y reproducir música de game over
    stop music fadeout 1.0
    play music "audio/gameover.mp3" fadein 1.0
    
    # Transición a negro
    scene black with Dissolve(1.0)
    
    # Diálogo de game over
    # Mostrar pantalla de game over
    call screen game_over_screen
    
    # Detener música de game over al salir
    stop music fadeout 1.0
    
    return

# ------------------------------
# RESPUESTAS
# ------------------------------

label respuesta_correcta:
    $ player_answer1 = ""
    $ player_answer2 = ""
    # Saltar al label para continuar con el diálogo
    jump continue_problema1

label respuesta_incorrecta:
    "No sucedió nada..."
    $ player_answer1 = ""
    $ player_answer2 = ""
    return


