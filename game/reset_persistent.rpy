init python:
    def reset_debug_flags():
        persistent.juego_completado = False
        persistent.modo_debug_desbloqueado = False
        renpy.save_persistent()
        renpy.notify("Flags reseteadas: juego=False, modo=False")

screen reset_debug_menu():
    zorder 300
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        background "#000000dd"
        padding (40, 30)
        
        vbox:
            spacing 20
            
            text "Reset Debug Flags" size 30 color "#ffffff"
            text "juego_completado: [persistent.juego_completado]" size 20 color "#aaaaaa"
            text "modo_debug: [persistent.modo_debug_desbloqueado]" size 20 color "#aaaaaa"
            
            null height 20
            
            textbutton "Reset a False":
                action Function(reset_debug_flags)
                
            textbutton "Cerrar":
                action Hide("reset_debug_menu")
