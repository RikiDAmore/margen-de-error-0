label main_menu_start:

    hide screen main_menu
    $ renpy.music.stop(fadeout=1.0)
    play sound "audio/start.mp3"

    # Flash blanco rápido
    scene expression Solid("#fff")
    with Pause(0.2)

    # Ahora el dissolve y la pausa
    scene black
    with Dissolve(3)
    pause 2.5

label return_to_main_menu:
    stop music fadeout 1.0
    hide screen game_over_screen
    with Dissolve(1.0)
    $ MainMenu(confirm=False)()
    return

label game_over_retry:
    stop music fadeout 1.0
    hide screen game_over_screen
    with Dissolve(1.0)
    jump start