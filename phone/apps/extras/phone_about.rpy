screen phone_info():
    use _phone():
        style_prefix "phone_info"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("About") xalign 0.5 text_align 0.5
            viewport:
                yfill True
                mousewheel True
                draggable True
                frame:
                    vbox:
                        xfill True
                        null height 16
                        text _("[config.name!t]") xalign .5
                        text _("Version [config.version!t]\n") xalign .5

                        ## gui.about is usually set in options.rpy.
                        if gui.about:
                            text "[gui.about!t]\n"

                        text _("Better EMR Phone Framework Copyright © 2022-2023 Elckarow (formerly Elckarow#8399).\n") xalign 0.5
                        text _("Phone+ Addon Copyright © 2023 CalebthePianist.\nCode adapted from the DDLC Mod Template 2.0 and DDLC Music Player by Bronya-Rand, Ren'Py Color Picker by Feniks, and screenshot code by bink on the Ren'Py Forums.\nDDLC emojis are by Team Salvato.\nTwemoji designs are licensed under CC-BY 4.0.\nChibi stickers were created by Team Salvato and edited by Leomonade.") xalign 0.5
                        text _("Special thanks to M3rc, Keita, and Elckarow for assistance and help.\n") xalign 0.5

                        ## Do not touch/remove these unless the © or – symbol isn't available in your font.
                        ## You may add things above or below it.
                        ## If you are not going with a splashscreen option, this first line MUST stay in the mod.
                        text _("Made with Bronya-Rand's DDLC Mod Template 2.0. Copyright © 2019-2023 Azariel Del Carmen (Bronya-Rand). All rights reserved.\n") xalign 0.5
                        text _("Doki Doki Literature Club is Copyright © 2017 Team Salvato. All rights reserved.\n") xalign 0.5
                        text _("Made with Ren'Py [renpy.version_only!t]") xalign 0.5

style phone_info is phone_settings

style phone_info_text is phone_settings_text:
    textalign 0.5

style phone_info_frame is phone_settings_frame:
    padding (5, 5, 5, 5)