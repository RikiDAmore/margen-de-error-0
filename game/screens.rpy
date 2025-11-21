

screen ingresar_respuesta(tag="menu"):
    modal True
    zorder 200

    add Solid("#0008")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        background "#2a2a2aee"

        vbox:
            spacing 15

            text "Ingresa tus respuestas" size 30 color "#fff"

            text "Respuesta 1:" color "#ddd"
            hbox:
                spacing 10
                text "[player_answer1]" size 20 color "#ffffff" xminimum 200
                textbutton "Editar" action Function(edit_answer1)

            text "Respuesta 2:" color "#ddd"
            hbox:
                spacing 10
                text "[player_answer2]" size 20 color "#ffffff" xminimum 200
                textbutton "Editar" action Function(edit_answer2)
            
            if current_level == "Ecuaciones Lineales":
                text "Respuesta 3:" color "#ddd"
                hbox:
                    spacing 10
                    text "[player_answer3]" size 20 color "#ffffff" xminimum 200
                    textbutton "Editar" action Function(edit_answer3)
                
                text "Respuesta 4:" color "#ddd"
                hbox:
                    spacing 10
                    text "[player_answer4]" size 20 color "#ffffff" xminimum 200
                    textbutton "Editar" action Function(edit_answer4)

            null height 20

            if current_level == "Ecuaciones Lineales":
                if not player_answer1.strip() or not player_answer2.strip() or not player_answer3.strip() or not player_answer4.strip():
                    text "Debes ingresar las 4 respuestas" size 18 color "#ff6666"
            else:
                if not player_answer1.strip() or not player_answer2.strip():
                    text "Debes ingresar ambas respuestas" size 18 color "#ff6666"

            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Enviar":
                    action Function(check_answer)
                textbutton "Cancelar":
                    action [Hide("ingresar_respuesta"), Show("ver_problema")]


init offset = -1

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

screen say(who, what):
    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Opciones") action ShowMenu('preferences')
            textbutton _("Menú") action MainMenu()
    
    key "K_ESCAPE" action MainMenu()

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Comenzar") action Jump("main_menu_start")
        else:
            textbutton _("Menú principal") action Jump("return_to_main_menu")

        textbutton _("Opciones") action ShowMenu("preferences")

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound "audio/hover.mp3"
    activate_sound "audio/select.mp3"

style navigation_button_text:
    properties gui.text_properties("navigation_button")

screen main_menu():
    tag menu

    add Solid("#000000")

    on "replace" action [Stop("music"), Function(renpy.restart_interaction)]
    
    timer 1.0 action If(renpy.music.get_playing(channel='music') != "audio/mmenu.mp3",
                        Play("music", "audio/mmenu.mp3", fadein=1.0))
    
    key "d" action Show("input_debug_code")
    
    if (persistent.modo_debug_desbloqueado or persistent.juego_completado) and comandos_debug_activos:
        key "x" action Show("reset_debug_menu")

    vbox at main_menu_appear:
        align (0.5, 0.22)
        spacing 10

        add "logo"

    vbox at main_menu_appear:
        align (0.5, 0.58)
        spacing 25

        textbutton "Jugar" style "red_button":
            action Jump("main_menu_start")
        textbutton "Opciones" style "red_button":
            action ShowMenu("preferences")
        textbutton "Salir" style "red_button":
            action Quit(confirm=True)

transform main_menu_appear:
    alpha 0.0
    linear 1.0 alpha 1.0

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"
        at main_menu_appear

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        xalign 0.5
                        yalign 0.5

                        side_yfill True

                        vbox:
                            spacing spacing
                            xalign 0.5

                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:
                    transclude

    use navigation

    if main_menu:
        textbutton _("Volver"):
            style "return_button"
            action [Play("music", "audio/mmenu.mp3", fadein=1.0), Return()]
    else:
        textbutton _("Volver"):
            style "return_button"
            action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 60
    top_margin 15
    xalign 0.5

style game_menu_viewport:
    xsize 1380
    xalign 0.5

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

screen preferences():
    tag menu
    
    on "show" action Play("music", "audio/options.mp3", fadein=1.0)
    on "replace" action Play("music", "audio/options.mp3", fadein=1.0)

    add Solid("#000000")
    
    frame:
        xalign 0.5
        yalign 0.5
        background "#00000000"
        
        vbox:
            spacing 40
            xalign 0.5

            text "Opciones" size 50 color "#ffffff" xalign 0.5 bold True
            
            null height 20

            vbox:
                spacing 25
                xalign 0.5

                if config.has_music:
                    vbox:
                        spacing 10
                        xalign 0.5
                        label _("Volumen Música"):
                            xalign 0.5
                        bar value Preference("music volume"):
                            xalign 0.5
                            xsize 400

                if config.has_sound:
                    vbox:
                        spacing 10
                        xalign 0.5
                        label _("Volumen Sonido"):
                            xalign 0.5
                        bar value Preference("sound volume"):
                            xalign 0.5
                            xsize 400

                if config.has_music or config.has_sound:
                    null height 20
                    
                    textbutton _("Silenciar Todo"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"
                        xalign 0.5
                
                null height 30
                
                if persistent.juego_completado or persistent.modo_debug_desbloqueado:
                    hbox:
                        spacing 40
                        xalign 0.5
                        
                        vbox:
                            spacing 20
                            
                            vbox:
                                spacing 10
                                
                                text "Detección de Cambio de Ventana" size 22 color "#ffffff"
                                
                                textbutton _("Activada" if deteccion_ventana_activa else "Desactivada"):
                                    action [ToggleVariable("deteccion_ventana_activa"), Function(resetear_deteccion_ventana)]
                                    style "check_button"
                            
                            vbox:
                                spacing 10
                                
                                text "Comandos Debug" size 22 color "#ffffff"
                                
                                textbutton _("Activados" if comandos_debug_activos else "Desactivados"):
                                    action ToggleVariable("comandos_debug_activos")
                                    style "check_button"
                        
                        vbox:
                            spacing 10
                            yalign 0.5
                            
                            text "Ojo Observador" size 22 color "#ffffff"
                            
                            textbutton "Ver Demostración":
                                action Show("demo_ojo_observador")
                                style "check_button"
            
            null height 40
            
            textbutton "Volver" style "red_button":
                action [Play("music", "audio/mmenu.mp3", fadein=1.0), Return()]
                xalign 0.5

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    hover_sound "audio/hover.mp3"
    activate_sound "audio/select.mp3"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
    hover_sound "audio/hover.mp3"
    activate_sound "audio/select.mp3"

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

screen confirm(message, yes_action, no_action):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Sí") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"

screen notify(message):
    zorder 300
    style_prefix "notify"

    frame at notify_appear:
        xalign 0.5
        yalign 0.5
        background "#000000dd"
        padding (40, 20)
        
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        yoffset -20
        linear .25 alpha 1.0 yoffset 0
    on hide:
        linear .5 alpha 0.0 yoffset 20

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    background None

style notify_text:
    size 28
    color "#ffffff"
    text_align 0.5
    xalign 0.5

style red_button is default:
    size 35
    xalign 0.5
    color "#cccccc"
    hover_color "#ff2020"
    idle_color "#cccccc"
    background None
    hover_background None
    hover_sound "audio/hover.mp3"
    activate_sound "audio/select.mp3"

style red_button_text is red_button

screen name_input():
    frame:
        align (0.5, 0.5)

        vbox:
            spacing 20
            xalign 0.5

            text "Escribe tu nombre:"

            input:
                value VariableInputValue("player_name")
                xalign 0.5

            textbutton "Aceptar":
                action Return()
                xalign 0.5

screen ver_problema():
    modal True
    zorder 100
    
    if comandos_debug_activos:
        key "r" action Jump("respuesta_correcta")
        key "t" action Function(debug_agregar_tiempo)
        key "y" action Function(debug_reducir_tiempo)
        key "h" action Function(debug_pausar_cronometro)
        key "g" action Jump("game_over_tiempo")
        key "c" action Jump("corredor_completado")
        key "m" action Function(debug_mostrar_respuestas)
        key "f" action Function(debug_toggle_latidos)
        key "v" action Jump("corredor_completado")

    frame:
        xalign 0.5
        yalign 0.5
        background "#2a2a2aee"
        xpadding 40
        ypadding 30

        vbox:
            spacing 25

            text "Nivel: [current_level]" size 25 color "#aaa"
            text "Niveles completados: [len(niveles_completados)]/[total_niveles]" size 20 color "#888"

            textbutton "Ver el problema":
                action Show("ver_problem")
                xalign 0.5

            textbutton "Resolver el problema":
                action [Hide("ver_problema"), Show("ingresar_respuesta")]
                xalign 0.5

screen ver_problem():
    modal True
    zorder 500

    add Solid("#0009")

    $ carpeta = "problemas/" + current_level + "/"
    $ imagen = str(current_problem_index) + ".png"
    $ ruta_completa = carpeta + imagen
    
    add ruta_completa at truecenter

    textbutton "Cerrar":
        xalign 0.5
        yalign 0.95
        action Hide("ver_problem")

screen cronometro():
    if ventana_cambiada:
        timer 0.1 action Jump("ventana_cambiada")
    
    if tiempo_activo:
        timer 1.0 repeat True action Function(actualizar_tiempo)
        
        $ horas = int(tiempo_restante // 3600)
        $ minutos = int((tiempo_restante % 3600) // 60)
        $ segundos = int(tiempo_restante % 60)
        
        $ color_tiempo = "#ffffff"
        if tiempo_restante <= 3600:
            $ color_tiempo = "#ffaa00"
        if tiempo_restante <= 600:
            $ color_tiempo = "#ff0000"
        
        frame:
            xalign 0.98
            yalign 0.02
            background "#00000088"
            padding (15, 10)
            
            vbox:
                spacing 5
                
                text "TIEMPO" size 18 color "#aaaaaa" xalign 0.5
                text "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos):
                    size 32
                    color color_tiempo
                    xalign 0.5
                    bold True

screen distorsion_cordura():
    if tiempo_activo:
        if tiempo_restante <= 7200:
            if tiempo_restante > 3600:
                $ alpha_vineta = 0.3
            elif tiempo_restante > 1800:
                $ alpha_vineta = 0.5
            else:
                $ alpha_vineta = 0.7
                
            add Solid("#000000"):
                xalign 0.5
                yalign 0.5
                xysize (config.screen_width, config.screen_height)
                at vineta_efecto
                alpha alpha_vineta
        
        if tiempo_restante <= 3600:
            if tiempo_restante > 1800:
                $ alpha_ruido = 0.05
            elif tiempo_restante > 600:
                $ alpha_ruido = 0.1
            else:
                $ alpha_ruido = 0.15
                
            add Solid("#808080"):
                xalign 0.5
                yalign 0.5
                xysize (config.screen_width, config.screen_height)
                at ruido_estatico
                alpha alpha_ruido
        
        if tiempo_restante <= 1800:
            if tiempo_restante > 600:
                $ alpha_aberracion = 0.05
            else:
                $ alpha_aberracion = 0.1
                
            add Solid("#ff0000"):
                xalign 0.5
                yalign 0.5
                xysize (config.screen_width, config.screen_height)
                at aberracion_roja
                alpha alpha_aberracion
        
        if tiempo_restante <= 600:
            add Solid("#000000"):
                xalign 0.5
                yalign 0.5
                xysize (config.screen_width, config.screen_height)
                at distorsion_critica
                alpha 0.2
            
            if tiempo_restante <= 300:
                add Solid("#ff0000"):
                    xalign 0.5
                    yalign 0.5
                    xysize (config.screen_width, config.screen_height)
                    at parpadeo_rojo
                    alpha 0.15

transform vineta_efecto:
    blur 50

transform ruido_estatico:
    xoffset 0
    yoffset 0
    block:
        linear 0.1 xoffset 5 yoffset 3
        linear 0.1 xoffset -3 yoffset -5
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -4 yoffset 4
        repeat

transform aberracion_roja:
    xoffset 0
    block:
        linear 2.0 xoffset 3
        linear 2.0 xoffset -3
        repeat

transform distorsion_critica:
    zoom 1.0
    blur 0
    block:
        linear 0.5 zoom 1.02 blur 5
        linear 0.5 zoom 1.0 blur 0
        linear 0.5 zoom 0.98 blur 5
        linear 0.5 zoom 1.0 blur 0
        repeat

transform parpadeo_rojo:
    alpha 0.0
    block:
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0.0
        pause 2.0
        repeat

screen game_over_screen():
    modal True
    zorder 999
    
    on "show" action Play("music", "audio/gameover.mp3", fadein=1.0)
    
    add Solid("#000000")
    
    frame:
        xalign 0.5
        yalign 0.5
        background "#1a1a1aee"
        xpadding 60
        ypadding 40
        
        vbox:
            spacing 30
            xalign 0.5
            
            text "SE ACABÓ EL TIEMPO" size 50 color "#ff0000" xalign 0.5 bold True
            text "No lograste escapar a tiempo..." size 25 color "#ffffff" xalign 0.5
            
            null height 20
            
            hbox:
                spacing 30
                xalign 0.5
                
                textbutton "Reintentar" style "red_button":
                    action [Return(), Jump("game_over_retry")]
                    
                textbutton "Menú Principal" style "red_button":
                    action [Return(), Jump("return_to_main_menu")]

style pref_vbox:
    variant "medium"
    xsize 675

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:
        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Atrás") action Rollback()
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menú") action ShowMenu()

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize gui.slider_size

screen mostrar_ojo_gif():
    zorder 1000
    modal True
    
    on "show" action Play("sound", "audio/paraelojo.mp3", loop=True)
    
    timer 0.1 repeat True action Function(renpy.invoke_in_thread, hacer_parpadear_ventana)
    
    timer 5.0 action Function(renpy.quit, relaunch=False, save=False)
    
    frame:
        background None
        xalign 0.5
        yalign 0.5
        
        add "ojo_animado"
    
    for i in range(15):
        timer (0.1 + i * 0.3):
            action Show("mensaje_glitch_{}".format(i))

screen demo_ojo_observador():
    zorder 1000
    modal True
    
    on "show" action Play("sound", "audio/paraelojo.mp3", loop=True)
    on "hide" action Stop("sound")
    
    timer 5.0 action Hide("demo_ojo_observador")
    
    frame:
        background None
        xalign 0.5
        yalign 0.5
        
        add "ojo_animado"
    
    for i in range(15):
        timer (0.1 + i * 0.3):
            action Show("mensaje_glitch_{}".format(i))
    
    timer 5.0 action Function(hide_all_glitch_messages)
    
screen mensaje_glitch_0():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_1():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_2():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_3():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_4():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_5():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_6():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_7():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_8():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_9():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_10():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_11():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_12():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_13():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen mensaje_glitch_14():
    zorder 1001
    $ mensajes = ["¿QUÉ ESTÁS HACIENDO?", "NO DEBERÍAS ESTAR AQUÍ", "VUELVE", "TE ESTOY OBSERVANDO", "NO PUEDES ESCAPAR", "CONCÉNTRATE", "ESTO NO ES UN JUEGO", "¿CREÍAS QUE PODÍAS HACER TRAMPA?", "SIEMPRE TE VEO", "NO HAY SALIDA"]
    $ import random
    $ msg = random.choice(mensajes)
    $ pos_x = random.uniform(0.1, 0.9)
    $ pos_y = random.uniform(0.1, 0.9)
    $ tamano = random.randint(20, 50)
    text msg xalign pos_x yalign pos_y size tamano color "#ff0000" bold True at transform:
        alpha 0.0
        linear 0.1 alpha 1.0

screen input_debug_code():
    zorder 200
    modal True
    
    default codigo_ingresado = ""
    
    frame:
        xalign 0.5
        yalign 0.5
        background "#000000dd"
        padding (40, 30)
        
        vbox:
            spacing 20
            
            text "Ingresa el código:" size 25 color "#ffffff"
            
            input:
                value ScreenVariableInputValue("codigo_ingresado")
                length 10
                color "#ffffff"
                size 30
                xalign 0.5
            
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Confirmar":
                    action Function(verificar_codigo_debug, codigo_ingresado)
                    
                textbutton "Cancelar":
                    action Hide("input_debug_code")
