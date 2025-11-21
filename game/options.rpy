define config.name = _("Margen de Error 0")

define gui.show_name = True

define config.version = "1.0"

define gui.about = _p("""
""")

define build.name = "MargendeError0"

define config.has_sound = True
define config.has_music = True

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve

define config.after_load_transition = None

define config.end_game_transition = None

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 30

default preferences.afm_time = 15

define config.save_directory = "MargendeError0-1763509773"

define config.window_icon = "gui/window_icon.png"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

init python:
    import random
    import time
    
    config.keymap['game_menu'] = []
    config.keymap['hide_windows'] = []
    
    config.keymap['screenshot'] = ['s']
    
    def check_window_minimized():
        global tiempo_activo
        
        if tiempo_activo:
            import pygame
            try:
                if pygame.event.peek(pygame.ACTIVEEVENT):
                    for event in pygame.event.get(pygame.ACTIVEEVENT):
                        if event.state & 2 == 0:
                            renpy.quit(relaunch=False, save=False)
            except:
                pass
    
    config.periodic_callbacks = [check_window_minimized]
    
    tiempo_inicio_escritura = 0
    escribiendo_respuesta = False
    
    def actualizar_tiempo():
        global tiempo_restante, tiempo_activo
        
        if tiempo_activo and tiempo_restante > 0:
            tiempo_restante -= 1
            
            if tiempo_restante <= 0:
                tiempo_activo = False
                renpy.hide_screen("cronometro")
                renpy.hide_screen("distorsion_cordura")
                renpy.hide_screen("ver_problema")
                renpy.hide_screen("ingresar_respuesta")
                renpy.jump("game_over_tiempo")
    
    def penalizar_tiempo(segundos=900):
        global tiempo_restante, tiempo_activo
        
        tiempo_restante = max(0, tiempo_restante - segundos)
        
        if tiempo_restante <= 0:
            tiempo_activo = False
            renpy.hide_screen("cronometro")
            renpy.hide_screen("distorsion_cordura")
            renpy.hide_screen("ver_problema")
            renpy.hide_screen("ingresar_respuesta")
            renpy.jump("game_over_tiempo")
            return
        
        if tiempo_restante > 14400:
            mensajes = [
                "Tengo que concentrarme...",
                "Vamos, puedo hacerlo mejor.",
                "No puedo fallar otra vez.",
                "Cálmate... piensa bien.",
            ]
        elif tiempo_restante > 10800:
            mensajes = [
                "Esto se está poniendo difícil...",
                "El tiempo se me escapa...",
                "Necesito enfocarme más.",
                "No... otro error...",
            ]
        elif tiempo_restante > 7200:
            mensajes = [
                "Mi cabeza empieza a doler...",
                "¿Cuánto tiempo llevo aquí?",
                "Los números... se mezclan...",
                "Debo... resistir...",
            ]
        elif tiempo_restante > 3600:
            mensajes = [
                "No... no puedo pensar bien...",
                "¿Por qué sigo fallando?",
                "Mi mente se nubla...",
                "Esto no puede estar pasando...",
                "Las paredes... ¿se están moviendo?",
            ]
        elif tiempo_restante > 1800:
            mensajes = [
                "Ya no sé qué es real...",
                "Los números me persiguen...",
                "¿Cuánto tiempo... queda?",
                "Mis manos tiemblan...",
                "No puedo... respirar bien...",
            ]
        elif tiempo_restante > 600:
            mensajes = [
                "TODO SE DESVANECE...",
                "¿Quién... quién soy?",
                "LOS NÚMEROS NO TIENEN SENTIDO...",
                "Mis ojos... arden...",
                "¿DÓNDE ESTÁ LA SALIDA?",
            ]
        else:
            mensajes = [
                "NO NO NO NO NO...",
                "¡DÉJENME SALIR!",
                "YA NO PUEDO MÁS...",
                "ESTO NO ES REAL...",
                "¿POR QUÉ NO PUEDO SALIR?",
            ]
        
        mensaje = random.choice(mensajes)
        renpy.notify(mensaje)
    
    def inicializar_niveles_aleatorios():
        global niveles_disponibles, total_niveles, current_level
        
        niveles_disponibles = list(problems.keys())
        
        random.shuffle(niveles_disponibles)
        
        total_niveles = len(niveles_disponibles)
        
        if niveles_disponibles:
            current_level = niveles_disponibles[0]
    
    def seleccionar_siguiente_nivel():
        global current_level, niveles_disponibles, niveles_completados
        
        niveles_restantes = [n for n in niveles_disponibles if n not in niveles_completados]
        
        if niveles_restantes:
            current_level = niveles_restantes[0]
    
    def seleccionar_problema_aleatorio():
        global current_problem_index, current_level
        
        total_problemas = problems[current_level]["total_problemas"]
        
        current_problem_index = random.randint(1, total_problemas)
    
    def mostrar_problema_actual():
        carpeta = "problemas/" + current_level + "/"
        imagen = str(current_problem_index) + ".png"
        ruta_completa = carpeta + imagen
        
        renpy.show("problem_image", at_list=[renpy.store.truecenter], what=renpy.displayable(ruta_completa))
    
    def get_current_answers():
        return problems[current_level]["respuestas"][current_problem_index]
    
    def check_answer():
        global player_answer1, player_answer2, player_answer3, player_answer4, current_level
        
        respuestas = get_current_answers()
        
        if current_level == "Ecuaciones Lineales":
            if not player_answer1.strip() or not player_answer2.strip() or not player_answer3.strip() or not player_answer4.strip():
                renpy.notify("Debes ingresar las 4 respuestas")
                return
            
            r1 = respuestas["respuesta1"]
            r2 = respuestas["respuesta2"]
            r3 = respuestas["respuesta3"]
            r4 = respuestas["respuesta4"]
            
            if (player_answer1.strip() == r1 and player_answer2.strip() == r2 and 
                player_answer3.strip() == r3 and player_answer4.strip() == r4):
                renpy.hide_screen("ingresar_respuesta")
                renpy.hide_screen("ver_problema")
                renpy.jump("respuesta_correcta")
            else:
                penalizar_tiempo(900)
        else:
            if not player_answer1.strip() or not player_answer2.strip():
                renpy.notify("Debes ingresar ambas respuestas")
                return
            
            r1 = respuestas["respuesta1"]
            r2 = respuestas["respuesta2"]
            
            if player_answer1.strip() == r1 and player_answer2.strip() == r2:
                renpy.hide_screen("ingresar_respuesta")
                renpy.hide_screen("ver_problema")
                renpy.jump("respuesta_correcta")
            else:
                penalizar_tiempo(900)

    def edit_answer1():
        global player_answer1, tiempo_restante, tiempo_inicio_escritura, escribiendo_respuesta
        
        escribiendo_respuesta = True
        tiempo_inicio_escritura = time.time()
        
        v = renpy.invoke_in_new_context(
            renpy.input, 
            "Respuesta 1:", 
            default=player_answer1, 
            allow="0123456789.-, "
        )
        
        tiempo_fin_escritura = time.time()
        segundos_escribiendo = int(tiempo_fin_escritura - tiempo_inicio_escritura)
        
        tiempo_restante = max(0, tiempo_restante - segundos_escribiendo)
        
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
        global player_answer2, tiempo_restante, tiempo_inicio_escritura, escribiendo_respuesta
        
        escribiendo_respuesta = True
        tiempo_inicio_escritura = time.time()
        
        v = renpy.invoke_in_new_context(
            renpy.input, 
            "Respuesta 2:", 
            default=player_answer2, 
            allow="0123456789.-, "
        )
        
        tiempo_fin_escritura = time.time()
        segundos_escribiendo = int(tiempo_fin_escritura - tiempo_inicio_escritura)
        
        tiempo_restante = max(0, tiempo_restante - segundos_escribiendo)
        
        if tiempo_restante <= 0:
            renpy.hide_screen("ingresar_respuesta")
            renpy.hide_screen("ver_problema")
            renpy.jump("game_over_tiempo")
            return
        
        escribiendo_respuesta = False
        
        if v is not None:
            player_answer2 = v
        renpy.restart_interaction()
    
    def edit_answer3():
        global player_answer3, tiempo_restante, tiempo_inicio_escritura, escribiendo_respuesta
        
        escribiendo_respuesta = True
        tiempo_inicio_escritura = time.time()
        
        v = renpy.invoke_in_new_context(
            renpy.input, 
            "Respuesta 3:", 
            default=player_answer3, 
            allow="0123456789.-, "
        )
        
        tiempo_fin_escritura = time.time()
        segundos_escribiendo = int(tiempo_fin_escritura - tiempo_inicio_escritura)
        
        tiempo_restante = max(0, tiempo_restante - segundos_escribiendo)
        
        if tiempo_restante <= 0:
            renpy.hide_screen("ingresar_respuesta")
            renpy.hide_screen("ver_problema")
            renpy.jump("game_over_tiempo")
            return
        
        escribiendo_respuesta = False
        
        if v is not None:
            player_answer3 = v
        renpy.restart_interaction()
    
    def edit_answer4():
        global player_answer4, tiempo_restante, tiempo_inicio_escritura, escribiendo_respuesta
        
        escribiendo_respuesta = True
        tiempo_inicio_escritura = time.time()
        
        v = renpy.invoke_in_new_context(
            renpy.input, 
            "Respuesta 4:", 
            default=player_answer4, 
            allow="0123456789.-, "
        )
        
        tiempo_fin_escritura = time.time()
        segundos_escribiendo = int(tiempo_fin_escritura - tiempo_inicio_escritura)
        
        tiempo_restante = max(0, tiempo_restante - segundos_escribiendo)
        
        if tiempo_restante <= 0:
            renpy.hide_screen("ingresar_respuesta")
            renpy.hide_screen("ver_problema")
            renpy.jump("game_over_tiempo")
            return
        
        escribiendo_respuesta = False
        
        if v is not None:
            player_answer4 = v
        renpy.restart_interaction()