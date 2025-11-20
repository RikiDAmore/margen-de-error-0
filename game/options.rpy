## Este archivo contiene opciones que pueden cambiarse para personalizar el
## juego.
##
## Las líneas que empiezan con doble '#' son comentarios, no deben ser
## descomentadas. Las líneas que empiezan con simple '#' son código comentado,
## puedes descomentarlas si es apropiado.


## Básico ######################################################################

## Nombre del juego en forma legible. Usado en el título de la ventana del
## juego, en la interfaz y en los informes de error.
##
## El _() que rodea la cadena de texto la señala como traducible.

define config.name = _("Margen de Error 0")


## Determina si el título dado más arriba se muestra en el menú principal.
## Ajústalo a 'False' para ocultar el título.

define gui.show_name = True


## Versión del juego.

define config.version = "1.0"


## Texto situado en la pantalla 'Acerca de' del juego. Sitúa el texto entre
## comillas triples y deja una línea en blanco entre párrafos.

define gui.about = _p("""
""")


## Nombre breve del juego para ejecutables y directorios en la distribución.
## Debe contener solo carácteres ASCII, sin espacios, comas o puntos y coma.

define build.name = "MargendeError0"


## Sonidos y música ############################################################

## Estas tres variables controlan, entre otras cosas, qué mezcladores se
## muestran al reproductor de forma predeterminada. Establecer uno de estos en
## False ocultará el mezclador apropiado. 

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Para permitir al usuario probar el volumen de los canales de sonido o voz,
## descomenta la línea más abajo y ajústala a un sonido de ejemplo.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Descomenta la línea siguiente para ajustar un archivo de audio que sonará en
## el menú principal. Este archivo seguirá sonando en el juego hasta que sea
## detenido o se reproduzca otro archivo.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transiciones ################################################################
##
## Estas variables ajustan transiciones usadas ante ciertos eventos. Cada
## variable debe indicar una transición o bien 'None', cuando no se desea usar
## ninguna transición.

## Entrar o salir del manú del juego.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Entre pantallas del menú del juego.

define config.intra_transition = dissolve


## Transición tras la carga de una partida.

define config.after_load_transition = None


## Transición de acceso al menú principal tras finalizar el juego.

define config.end_game_transition = None


## No existe la variable que ajusta la transición cuando el juego comienza. Para
## ello se usa la sentencia 'with' al mostrar la escena inicial.


## Gestión de ventanas #########################################################
##
## Esto controla cuándo se muestra la ventana de diálogo. Si es "show", es
## siempre visible. Si es "hide", solo se muestra cuando hay diálogo presente.
## Si es "auto", la ventana se esconde antes de las sentencias 'scene' y se
## muestra de nuevo cuando hay diálogo que presentar.
##
## Una vez comenzado el juego, esto se puede ajustar con las sentencias "window
## show", "window hide", y "window auto".

define config.window = "auto"


## Transiciones usadas para mostrar o esconder la ventana de diálogo

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferencias por defecto ####################################################

## Controla la velocidad del texto por defecto. El valor por defecto 0 indica
## infinito; cualquier otro número indica el número de caracteres por segundo
## que se mostrarán.

default preferences.text_cps = 30


## El retraso por defecto del auto-avance. Números más grandes indican esperas
## mayores. El rango válido es 0-30.

default preferences.afm_time = 15


## Directorio de guardado ######################################################
##
## Controla el lugar en el que Ren'Py colocará los archivos de guardado,
## dependiendo de la plataforma.
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Normalmente, este valor no debe ser modificado. Si lo es, debe ser siempre
## una cadena literal y no una expresión.

define config.save_directory = "MargendeError0-1763509773"


## Icono #######################################################################
##
## El icono mostrado en la barra de tareas.

define config.window_icon = "gui/window_icon.png"


## Configuración de 'Build' ####################################################
##
## Esta sección contrla cómo Ren'Py convierte el proyecto en archivos para la
## distribución.

init python:
    

    ## Las funciones siguientes toman patrones de archivos. No son relevantes
    ## las mayúsculas o minúsculas. Son relativos al directorio base, con o sin
    ## una / inicial. Si corresponden más de un patrón, se usa el primero.
    ##
    ## En un patrón:
    ##
    ## / es el separador de directorios.
    ##
    ## * corresponde a todos los carácteres, excepto el separador de
    ##   directorios.
    ##
    ## ** corresponde a todos los carácteres, incluynedo el separador de
    ##    directorios.
    ##
    ## Por ejemplo, "*.txt" corresponde a los archivos .txt en el directorio
    ## de base, "game/**.ogg" corresponde a los archivos .ogg del directorio
    ## 'game' y sus subdirectorios y "**.psd" corresponde a los archivos .psd en
    ## cualquier parte del proyecto.

    ## Clasifica archivos como 'None' para excluirlos de la distribución.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Para archivar, se clasifican como 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Los archivos que corresponden a patrones de documentation se duplican en
    ## la distribución de mac; aparecerán en los archivos app y zip.

    build.documentation('*.html')
    build.documentation('*.txt')
init python:
    import random
    import time
    
    # ==========================================================================
    # CONFIGURACIÓN DE TECLAS
    # ==========================================================================
    
    # Redefinir la tecla ESC para ir al menú principal en lugar de opciones
    config.keymap['game_menu'] = []  # Quitar el comportamiento por defecto de ESC
    config.keymap['hide_windows'] = []  # Opcional: quitar hide windows si quieres
    
    # Agregar ESC para ir directamente al menú principal
    config.keymap['screenshot'] = ['s']  # Dejar screenshot en 's'
    
    # ==========================================================================
    # SISTEMA DE DETECCIÓN DE MINIMIZACIÓN DE VENTANA
    # ==========================================================================
    
    def check_window_minimized():
        """
        Verifica si la ventana está minimizada.
        Si se minimiza durante una partida activa, cierra el juego inmediatamente.
        """
        global tiempo_activo
        
        # Solo verificar si hay una partida activa
        if tiempo_activo:
            import pygame
            try:
                # Verificar si la ventana está minimizada o perdió el foco
                # pygame.APPACTIVE detecta si la aplicación está activa
                if pygame.event.peek(pygame.ACTIVEEVENT):
                    for event in pygame.event.get(pygame.ACTIVEEVENT):
                        # Si el evento indica que se minimizó o perdió foco
                        if event.state & 2 == 0:  # Bit 2 = ventana activa
                            # Ventana minimizada o inactiva - cerrar inmediatamente
                            renpy.quit(relaunch=False, save=False)
            except:
                pass
    
    # Configurar callback periódico para verificar constantemente
    config.periodic_callbacks = [check_window_minimized]
    
    # ==========================================================================
    # SISTEMA DE TIEMPO
    # ==========================================================================
    
    # Variable para rastrear tiempo de escritura
    tiempo_inicio_escritura = 0
    escribiendo_respuesta = False
    
    def actualizar_tiempo():
        """
        Reduce el tiempo restante en 1 segundo.
        Si llega a 0, salta a game over.
        """
        global tiempo_restante, tiempo_activo
        
        if tiempo_activo and tiempo_restante > 0:
            tiempo_restante -= 1
            
            # Verificar si se acabó el tiempo
            if tiempo_restante <= 0:
                tiempo_activo = False
                # Ocultar todas las pantallas antes del jump
                renpy.hide_screen("cronometro")
                renpy.hide_screen("distorsion_cordura")
                renpy.hide_screen("ver_problema")
                renpy.hide_screen("ingresar_respuesta")
                renpy.jump("game_over_tiempo")
    
    def penalizar_tiempo(segundos=900):
        """
        Reduce el tiempo restante por respuesta incorrecta.
        Muestra un mensaje según el nivel de cordura (tiempo restante).
        Por defecto quita 15 minutos (900 segundos).
        Si el tiempo llega a 0 o menos, game over inmediato.
        """
        global tiempo_restante, tiempo_activo
        
        # Reducir tiempo
        tiempo_restante = max(0, tiempo_restante - segundos)
        
        # SI EL TIEMPO LLEGÓ A 0 O MENOS, GAME OVER INMEDIATO
        if tiempo_restante <= 0:
            tiempo_activo = False
            # Ocultar todas las pantallas antes del jump
            renpy.hide_screen("cronometro")
            renpy.hide_screen("distorsion_cordura")
            renpy.hide_screen("ver_problema")
            renpy.hide_screen("ingresar_respuesta")
            renpy.jump("game_over_tiempo")
            return  # Salir de la función para evitar mostrar mensaje
        
        # Mensajes según el tiempo restante (cordura)
        if tiempo_restante > 14400:  # Más de 4 horas
            mensajes = [
                "Tengo que concentrarme...",
                "Vamos, puedo hacerlo mejor.",
                "No puedo fallar otra vez.",
                "Cálmate... piensa bien.",
            ]
        elif tiempo_restante > 10800:  # Entre 3-4 horas
            mensajes = [
                "Esto se está poniendo difícil...",
                "El tiempo se me escapa...",
                "Necesito enfocarme más.",
                "No... otro error...",
            ]
        elif tiempo_restante > 7200:  # Entre 2-3 horas
            mensajes = [
                "Mi cabeza empieza a doler...",
                "¿Cuánto tiempo llevo aquí?",
                "Los números... se mezclan...",
                "Debo... resistir...",
            ]
        elif tiempo_restante > 3600:  # Entre 1-2 horas
            mensajes = [
                "No... no puedo pensar bien...",
                "¿Por qué sigo fallando?",
                "Mi mente se nubla...",
                "Esto no puede estar pasando...",
                "Las paredes... ¿se están moviendo?",
            ]
        elif tiempo_restante > 1800:  # Entre 30min-1 hora
            mensajes = [
                "Ya no sé qué es real...",
                "Los números me persiguen...",
                "¿Cuánto tiempo... queda?",
                "Mis manos tiemblan...",
                "No puedo... respirar bien...",
            ]
        elif tiempo_restante > 600:  # Entre 10-30 minutos
            mensajes = [
                "TODO SE DESVANECE...",
                "¿Quién... quién soy?",
                "LOS NÚMEROS NO TIENEN SENTIDO...",
                "Mis ojos... arden...",
                "¿DÓNDE ESTÁ LA SALIDA?",
            ]
        else:  # Menos de 10 minutos - CRÍTICO
            mensajes = [
                "NO NO NO NO NO...",
                "¡DÉJENME SALIR!",
                "YA NO PUEDO MÁS...",
                "ESTO NO ES REAL...",
                "¿POR QUÉ NO PUEDO SALIR?",
            ]
        
        # Seleccionar mensaje aleatorio
        mensaje = random.choice(mensajes)
        renpy.notify(mensaje)
    
    # ==========================================================================
    # SISTEMA DE PROBLEMAS ALEATORIOS
    # ==========================================================================
    
    # --------------------------------------------------------------------------
    # Inicialización de niveles
    # --------------------------------------------------------------------------
    
    def inicializar_niveles_aleatorios():
        """
        Inicializa el sistema de niveles aleatorios.
        - Obtiene todos los niveles disponibles del diccionario 'problems'
        - Los mezcla aleatoriamente
        - Selecciona el primer nivel
        """
        global niveles_disponibles, total_niveles, current_level
        
        # Obtener todos los nombres de niveles (carpetas)
        niveles_disponibles = list(problems.keys())
        
        # Mezclar aleatoriamente para orden diferente en cada partida
        random.shuffle(niveles_disponibles)
        
        total_niveles = len(niveles_disponibles)
        
        # Seleccionar el primer nivel
        if niveles_disponibles:
            current_level = niveles_disponibles[0]
    
    # --------------------------------------------------------------------------
    # Selección de niveles y problemas
    # --------------------------------------------------------------------------
    
    def seleccionar_siguiente_nivel():
        """
        Selecciona el siguiente nivel no completado de la lista aleatoria.
        """
        global current_level, niveles_disponibles, niveles_completados
        
        # Encontrar niveles no completados
        niveles_restantes = [n for n in niveles_disponibles if n not in niveles_completados]
        
        if niveles_restantes:
            current_level = niveles_restantes[0]
    
    def seleccionar_problema_aleatorio():
        """
        Selecciona UN problema aleatorio del nivel actual.
        El problema se elige entre 1 y total_problemas del nivel.
        """
        global current_problem_index, current_level
        
        # Obtener total de problemas del nivel actual
        total_problemas = problems[current_level]["total_problemas"]
        
        # Seleccionar UN índice aleatorio (del 1 al total)
        current_problem_index = random.randint(1, total_problemas)
    
    # --------------------------------------------------------------------------
    # Visualización de problemas
    # --------------------------------------------------------------------------
    
    def mostrar_problema_actual():
        """
        Muestra la imagen del problema actual en pantalla.
        Construye la ruta: problemas/[carpeta]/[numero].png
        """
        # Construir la ruta de la imagen
        carpeta = "problemas/" + current_level + "/"
        imagen = str(current_problem_index) + ".png"
        ruta_completa = carpeta + imagen
        
        # Mostrar la imagen del problema
        renpy.show("problem_image", at_list=[renpy.store.truecenter], what=renpy.displayable(ruta_completa))
    
    # --------------------------------------------------------------------------
    # Gestión de respuestas
    # --------------------------------------------------------------------------
    
    def get_current_answers():
        """
        Obtiene las respuestas correctas del problema actual.
        Returns: dict con {"respuesta1": valor, "respuesta2": valor}
        """
        return problems[current_level]["respuestas"][current_problem_index]
    
    def check_answer():
        """
        Valida las respuestas del jugador contra las respuestas correctas.
        - Verifica que ambas respuestas estén ingresadas
        - Compara con las respuestas correctas
        - Salta a la etiqueta correspondiente (correcta/incorrecta)
        """
        global player_answer1, player_answer2
        
        # Verificar que ambas respuestas tengan contenido
        if not player_answer1.strip() or not player_answer2.strip():
            renpy.notify("Debes ingresar ambas respuestas")
            return

        # Obtener respuestas correctas
        respuestas = get_current_answers()
        r1 = respuestas["respuesta1"]
        r2 = respuestas["respuesta2"]

        # Validar respuestas
        if player_answer1.strip() == r1 and player_answer2.strip() == r2:
            # Respuesta correcta
            renpy.hide_screen("ingresar_respuesta")
            renpy.hide_screen("ver_problema")
            renpy.jump("respuesta_correcta")
        else:
            # Respuesta incorrecta - APLICAR PENALIZACIÓN
            penalizar_tiempo(900)  # Quitar 15 minutos

    # --------------------------------------------------------------------------
    # Edición de respuestas
    # --------------------------------------------------------------------------
    
    def edit_answer1():
        """
        Permite editar la respuesta 1 usando un input modal.
        Solo acepta números, puntos y guiones.
        REGISTRA EL TIEMPO QUE TOMAS ESCRIBIENDO Y LO RESTA DEL CRONÓMETRO.
        """
        global player_answer1, tiempo_restante, tiempo_inicio_escritura, escribiendo_respuesta
        
        # Marcar que empezó a escribir
        escribiendo_respuesta = True
        tiempo_inicio_escritura = time.time()
        
        v = renpy.invoke_in_new_context(
            renpy.input, 
            "Respuesta 1:", 
            default=player_answer1, 
            allow="0123456789.-"
        )
        
        # Calcular tiempo que pasó escribiendo
        tiempo_fin_escritura = time.time()
        segundos_escribiendo = int(tiempo_fin_escritura - tiempo_inicio_escritura)
        
        # RESTAR el tiempo de escritura del cronómetro
        tiempo_restante = max(0, tiempo_restante - segundos_escribiendo)
        
        # Verificar si se acabó el tiempo mientras escribía
        if tiempo_restante <= 0:
            renpy.hide_screen("ingresar_respuesta")
            renpy.hide_screen("ver_problema")
            renpy.jump("game_over_tiempo")
            return
        
        escribiendo_respuesta = False
        
        if v is not None:
            player_answer1 = v
        renpy.restart_interaction()

    def edit_answer2():
        """
        Permite editar la respuesta 2 usando un input modal.
        Solo acepta números, puntos y guiones.
        REGISTRA EL TIEMPO QUE TOMAS ESCRIBIENDO Y LO RESTA DEL CRONÓMETRO.
        """
        global player_answer2, tiempo_restante, tiempo_inicio_escritura, escribiendo_respuesta
        
        # Marcar que empezó a escribir
        escribiendo_respuesta = True
        tiempo_inicio_escritura = time.time()
        
        v = renpy.invoke_in_new_context(
            renpy.input, 
            "Respuesta 2:", 
            default=player_answer2, 
            allow="0123456789.-"
        )
        
        # Calcular tiempo que pasó escribiendo
        tiempo_fin_escritura = time.time()
        segundos_escribiendo = int(tiempo_fin_escritura - tiempo_inicio_escritura)
        
        # RESTAR el tiempo de escritura del cronómetro
        tiempo_restante = max(0, tiempo_restante - segundos_escribiendo)
        
        # Verificar si se acabó el tiempo mientras escribía
        if tiempo_restante <= 0:
            renpy.hide_screen("ingresar_respuesta")
            renpy.hide_screen("ver_problema")
            renpy.jump("game_over_tiempo")
            return
        
        escribiendo_respuesta = False
        
        if v is not None:
            player_answer2 = v
        renpy.restart_interaction()


## Se necesita una clave de licencia de Google Play para realizar compras dentro
## de la aplicación. Se puede encontrar en la consola de desarrollador de Google
## Play, en "Monetizar" > "Configuración de la monetización" > "Licencias".

# define build.google_play_key = "..."


## Los nombres de usuario y de proyecto asociados con un proyecto itch.io,
## separados por una barra.

# define build.itch_project = "renpytom/test-project"