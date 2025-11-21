define name = ""
default player_name = ""
default tiempo = 21600
default tiempo_restante = 21600
default tiempo_activo = False

default problems = {
    "Interpolacion": {
        "total_problemas": 10,
        "respuestas": {
            1: {"respuesta1": "4.99", "respuesta2": "4"},
            2: {"respuesta1": "7.84", "respuesta2": "2.5"},
            3: {"respuesta1": "4.24", "respuesta2": "1"},
            4: {"respuesta1": "8.08", "respuesta2": "5"},
            5: {"respuesta1": "6.845", "respuesta2": "4"},
            6: {"respuesta1": "4.25", "respuesta2": "4"},
            7: {"respuesta1": "12.50", "respuesta2": "3, 4"},
            8: {"respuesta1": "7.25", "respuesta2": "2, 2.5"},
            9: {"respuesta1": "4.99", "respuesta2": "-0.03652"},
            10: {"respuesta1": "4.83", "respuesta2": "0.02614"},
        }
    },
    "Integracion": {
        "total_problemas": 3,
        "respuestas": {
            1: {"respuesta1": "1.7572", "respuesta2": "0.40"},
            2: {"respuesta1": "1.4936", "respuesta2": "1"},
            3: {"respuesta1": "1.2647", "respuesta2": "0.01195"},
        }
    },
    "Ecuaciones No Lineales": {
        "total_problemas": 8,
        "respuestas": {
            1: {"respuesta1": "3.55", "respuesta2": "5"},
            2: {"respuesta1": "0.40236", "respuesta2": "5"},
            3: {"respuesta1": "2.094", "respuesta2": "10"},
            4: {"respuesta1": "1.512", "respuesta2": "1.4817"},
            5: {"respuesta1": "2", "respuesta2": "1.7"},
            6: {"respuesta1": "-1.5", "respuesta2": "-1.2"},
            7: {"respuesta1": "2", "respuesta2": "4"},
            8: {"respuesta1": "3", "respuesta2": "4"},        
        }
    },
    "Ecuaciones Lineales": {
        "total_problemas": 10,
        "respuestas": {
            1: {"respuesta1": "1.700855", "respuesta2": "0.726496", "respuesta3": "1.256410", "respuesta4": "6"},
            2: {"respuesta1": "1.275510", "respuesta2": "0.153061", "respuesta3": "2.1632650", "respuesta4": "7"},
            3: {"respuesta1": "1", "respuesta2": "-0.285714", "respuesta3": "2.428571", "respuesta4": "4"},
            4: {"respuesta1": "0.333333", "respuesta2": "2.095238", "respuesta3": "0.761904", "respuesta4": "3"},
            5: {"respuesta1": "0.774410", "respuesta2": "1.925925", "respuesta3": "2.178451", "respuesta4": "5"},
            6: {"respuesta1": "1.492307", "respuesta2": "0.353846", "respuesta3": "1.569230", "respuesta4": "-16"},
            7: {"respuesta1": "2.137931", "respuesta2": "0.793103", "respuesta3": "1.551724", "respuesta4": "3"},
            8: {"respuesta1": "2.278350", "respuesta2": "-0.876288", "respuesta3": "2.216494", "respuesta4": "3"},
            9: {"respuesta1": "2.698795", "respuesta2": "1.457831", "respuesta3": "-0.710843", "respuesta4": "3"},
            10: {"respuesta1": "2.771428", "respuesta2": "1.514285", "respuesta3": "3.628571", "respuesta4": "3"},

        }
    },
}

default niveles_disponibles = []
default niveles_completados = []
default current_level = ""
default current_problem_index = 0
default total_niveles = 0
default player_answer1 = ""
default player_answer2 = ""
default player_answer3 = ""
default player_answer4 = ""



label start:

    call screen name_input
    
    if player_name == "":
        $ player_name = "Jugador"
    
    $ n = Character("[player_name]")

    $ inicializar_niveles_aleatorios()
    $ seleccionar_problema_aleatorio()

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
    
    $ mostrar_problema_actual()
    
    n ""
    n "A lado del pizarrón hay una especie de teclado con números, supongo que para escribir la respuesta."
    n "Quiero pensar que al resolver este problema podré salir de aquí."
    n "Convenientemente, hay una libreta en una de las mesas."
    n "La usare para poder resolver... {w=0.5}eso."
    
    window hide
    $ _window = False
    hide problem_image
    with Dissolve(0.5)
    show screen ver_problema
    show screen cronometro
    show screen distorsion_cordura
    with Dissolve(0.5)
    
    pause
    
label continue_problema1:
    hide screen ver_problema
    hide screen ingresar_respuesta
    hide screen ver_problem
    play sound "audio/click.mp3"
    n "Escuche un click"
    n "Un candado se abrió."
    
    
    $ niveles_completados.append(current_level)
    if len(niveles_completados) < total_niveles:
        n "Aun faltan candados..."
        n "Noto que a lado del problema que resolvi hay otro problema nuevo."
        
        $ seleccionar_siguiente_nivel()
        $ seleccionar_problema_aleatorio()
        $ mostrar_problema_actual()
        
        n "Este es... ¿[current_level]?"

        window hide
        $ _window = False
        hide problem_image
        with Dissolve(0.5)
        show screen ver_problema
        show screen cronometro
        show screen distorsion_cordura
        with Dissolve(0.5)
        
        pause
    else:
        $ tiempo_activo = False
        hide screen cronometro
        hide screen distorsion_cordura
        
        n "Se ha abierto la puerta..."
        n "Salgo del salon, y me dirijo a la salida para no volver nunca mas..."
        return

label game_over_tiempo:
    $ tiempo_activo = False
    
    hide screen cronometro
    hide screen distorsion_cordura
    hide screen ver_problema
    hide screen ingresar_respuesta
    hide screen ver_problem
    
    stop music fadeout 1.0
    play music "audio/gameover.mp3" fadein 1.0
    
    scene black with Dissolve(1.0)
    
    call screen game_over_screen
    
    stop music fadeout 1.0
    
    return

label respuesta_correcta:
    $ player_answer1 = ""
    $ player_answer2 = ""
    $ player_answer3 = ""
    $ player_answer4 = ""
    jump continue_problema1

label respuesta_incorrecta:
    "No sucedió nada..."
    $ player_answer1 = ""
    $ player_answer2 = ""
    $ player_answer3 = ""
    $ player_answer4 = ""
    return


