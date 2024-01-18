screen phone_quick_menu():
    grid 3 2 style_prefix "phone_quick_menu":
        vbox:
            imagebutton:
                idle phone.config.basedir + "quick_menu_history_idle.png"
                hover phone.config.basedir + "quick_menu_history_selected.png"
                selected_idle phone.config.basedir + "quick_menu_history_selected.png"
                action PhoneMenu("phone_dialogue_history")
            text _("History")

        vbox:
            imagebutton:
                idle phone.config.basedir + "quick_menu_afm_idle.png"
                hover phone.config.basedir + "quick_menu_afm_selected.png"
                selected_idle phone.config.basedir + "quick_menu_afm_selected.png"
                action Preference("auto-forward", "toggle")
            text _("Auto")

        vbox:
            imagebutton:
                idle phone.config.basedir + "quick_menu_skip_idle.png"
                hover phone.config.basedir + "quick_menu_skip_selected.png"
                selected_idle phone.config.basedir + "quick_menu_skip_selected.png"
                action Skip()
            text _("Skip")

        vbox:
            imagebutton:
                idle phone.config.basedir + "quick_menu_settings_idle.png"
                hover phone.config.basedir + "quick_menu_settings_selected.png"
                selected_idle phone.config.basedir + "quick_menu_settings_selected.png"
                action PhoneMenu("phone_settings")
            text _("Settings")

        vbox:
            imagebutton:
                idle phone.config.basedir + "quick_menu_save_idle.png"
                hover phone.config.basedir + "quick_menu_save_selected.png"
                selected_idle phone.config.basedir + "quick_menu_save_selected.png"
                action PhoneMenu("phone_savegame")
            text _("Save")

        vbox:
            imagebutton:
                idle phone.config.basedir + "quick_menu_load_idle.png"
                hover phone.config.basedir + "quick_menu_load_selected.png"
                selected_idle phone.config.basedir + "quick_menu_load_selected.png"
                action PhoneMenu("phone_loadgame")
            text _("Load")

style phone_quick_menu_grid is empty:
    xspacing 31 yspacing 22

style phone_quick_menu_vbox is empty
style phone_quick_menu_text is phone_call_time:
    size 14

screen phone_quick_menu_video():
    default qm = False
    default anim_time = 0.35

    showif qm:
        add "#000":
            at transform:
                alpha 0.0
                on show:
                    ease anim_time alpha 0.35
                on hide:
                    ease anim_time alpha 0.0

    vbox style "empty" yalign 1.0 xsize 1.0 xfill True:
        button style "empty" padding (5, 7, 5, 4) xalign 0.5:
            at transform:
                ease anim_time matrixtransform RotateMatrix(0, 0, 180 * qm) matrixcolor OpacityMatrix(0.8 if qm else 0.6)
            
            action ToggleLocalVariable("qm")

            add phone.config.basedir + "arrow_icon.png":
                at transform:
                    subpixel True xysize (70, 18)
                        
        showif qm:
            frame style "empty" top_padding 30 bottom_padding 15 xsize 1.0 modal True:
                at transform:
                    subpixel True crop (0, 0, 1.0, 0.0)
                    on show:
                        ease anim_time crop (0, 0, 1.0, 1.0) alpha 1.0
                    on hide:
                        ease anim_time crop (0, 0, 1.0, 0.0) alpha 0.0

                background "#00000060"

                vbox style "empty" xalign 0.5:
                    use phone_quick_menu()

                    null height 15

                    add phone.config.basedir + "hang_up.png":
                        subpixel True xysize (63, 63) xalign 0.5

screen quick_menu_phone():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            imagebutton:
                xoffset 20
                yoffset 300
                idle "mod_assets/phone/assets/background.png"
                hover "mod_assets/phone/assets/background.png"
                selected "mod_assets/phone/assets/background.png" 
                action [SetVariable("phonepos", 0.15), Function(phone.call_screen, "phone")]
                at phonehover

    if not ost_info.get_current_soundtrack:
        timer 0.01 action NullAction()
    else:
        if persistent.music_continue:
            if persistent.musicstarted == True:
                if not ost_controls.pausedState:
                    timer 0.02 action PauseAudio("music", True)
                    if not renpy.music.is_playing(channel='phone_music'):
                        timer 0.02 action Function(ost_controls.play_music)
            else:
                timer 0.02 action PauseAudio("music", False)
                timer 0.02 action Function(ost_controls.pause_music) 
        else:
            timer 0.02 action Function(ost_controls.pause_music)
            timer 0.02 action PauseAudio("music", False)
    if persistent.phonelocked:
        timer 0.01 action [SetField(persistent, "phonelocked", False), SetVariable("phonelocked1", True)]
    if persistent.phoneunlocked:
        timer 0.01 action [SetField(persistent, "phoneunlocked", False), SetVariable("phoneunlocked1", True)]

default in_splash = False
default phoneunlocked1 = False
default phonelocked1 = False

transform phonehover:
    zoom 0.5
    yoffset 300
    on hover:
        easeout 0.3 yoffset 260
    on idle:
        easeout 0.3 yoffset 300
    on selected:
        easeout 0.3 yoffset 350
