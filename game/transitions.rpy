label main_menu_start:

    hide screen main_menu
    $ renpy.music.stop()
    play sound "audio/start.mp3"

    # Flash blanco rápido
    scene expression Solid("#fff")
    with Pause(0.2)

    # Ahora el dissolve y la pausa
    scene black
    with Dissolve(3)
    pause 2.5