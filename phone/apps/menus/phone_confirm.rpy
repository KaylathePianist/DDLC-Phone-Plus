screen confirm(message, yes_action, no_action):
    if renpy.get_screen("phone_discussionex"):
        use confirm_phone(message, yes_action, no_action, center=True)
    elif renpy.get_screen("_phone_image"):
        use confirm_orig(message, yes_action, no_action)
    elif renpy.get_screen("phone_settings") or renpy.get_screen("_phone") or renpy.get_screen("phone_contacts") or renpy.get_screen("phone") or renpy.get_screen("phone_savegame") or renpy.get_screen("phone_loadgame") or renpy.get_screen("phone_call") or renpy.get_screen("phone_video_call") or renpy.get_screen("phone_calendar") or renpy.get_screen("phone_dialogue_history") or renpy.get_screen("phone_info") or renpy.get_screen("phone_advanced") or renpy.get_screen("color_picker") or renpy.get_screen("color_picker2") or renpy.get_screen("phone_call_history") or renpy.get_screen("phone_discussion") or renpy.get_screen("photos_gallery") or renpy.get_screen("photos_gallery2") or renpy.get_screen("photos_gallery3") or renpy.get_screen("phone_music") or renpy.get_screen("phone_music_list") or renpy.get_screen("phone_achievements") or renpy.get_screen("phone_music_list_type") or renpy.get_screen("phone_music_settings") or renpy.get_screen("phone_music_info")or renpy.get_screen("phone_calculator"):
        use confirm_phone(message, yes_action, no_action, center=False)
    else:
        use confirm_orig(message, yes_action, no_action)


screen confirm_phone(message, yes_action, no_action, center=False):
    modal True
    zorder 200
    fixed:
        if center:
            at [Flatten, phone_confirm_transform_center]
        else:
            at [Flatten, phone_confirm_transform]
        xsize 300
        vbox spacing 2:
            style_prefix "phone_confirm"
            null height 300
            frame:
                if persistent.darkmode:
                    background RoundedFrame("#525252", radius=(0, 10, 0, 10)) # some color i pulled out of my ass
                else:
                    background RoundedFrame("#cdcdcd", radius=(0, 10, 0, 10)) # some color i pulled out of my ass
                ysize 100
                xsize 242
                vbox:
                    ysize 90
                    xfill True
                    yalign 0.0
                    yanchor 0.0
                    xalign 0.0
                    xanchor 0.0
                    text message xalign 0.5 yalign 0.6
            
            hbox spacing 2:
                button:
                    xsize 120
                    ysize 36
                    label "Yes" align (0.5, 0.5)
                    if persistent.darkmode:
                        idle_background RoundedFrame("#525252", radius=(0, 0, 10, 0))
                        hover_background RoundedFrame("#7e7e7e", radius=(0, 0, 10, 0))
                    else:
                        idle_background RoundedFrame("#cdcdcd", radius=(0, 0, 10, 0))
                        hover_background RoundedFrame("#9e9e9e", radius=(0, 0, 10, 0))
                    action yes_action
                button:
                    xsize 120
                    ysize 36
                    label "No" align (0.5, 0.5)
                    if persistent.darkmode:
                        idle_background RoundedFrame("#525252", radius=(10, 0, 0, 0))
                        hover_background RoundedFrame("#7e7e7e", radius=(10, 0, 0, 0))
                    else:
                        background RoundedFrame("#cdcdcd", radius=(10, 0, 0, 0))
                        hover_background RoundedFrame("#9e9e9e", radius=(10, 0, 0, 0))
                    action no_action

screen phone_dialogue(message, ok_action, center=False):
    modal True
    zorder 200
    fixed:
        if center:
            at [Flatten, phone_confirm_transform_center]
        else:
            at [Flatten, phone_confirm_transform]
        xsize 300
        vbox spacing 2:
            style_prefix "phone_confirm"
            null height 300
            frame:
                if persistent.darkmode:
                    background RoundedFrame("#525252", radius=(0, 10, 0, 10)) # some color i pulled out of my ass
                else:
                    background RoundedFrame("#cdcdcd", radius=(0, 10, 0, 10)) # some color i pulled out of my ass
                ysize 100
                xsize 242
                vbox:
                    ysize 90
                    xsize 238
                    yalign 0.0
                    yanchor 0.0
                    xalign 0.0
                    xanchor 0.0
                    text message xalign 0.5 yalign 0.5
            
            hbox:
                button:
                    xsize 242
                    ysize 36
                    label "Okay" align (0.5, 0.5)
                    if persistent.darkmode:
                        idle_background RoundedFrame("#525252", radius=(10, 0, 10, 0))
                        hover_background RoundedFrame("#7e7e7e", radius=(10, 0, 10, 0))
                    else:
                        idle_background RoundedFrame("#cdcdcd", radius=(10, 0, 10, 0))
                        hover_background RoundedFrame("#9e9e9e", radius=(10, 0, 10, 0))
                    action ok_action



transform phone_confirm_transform:
    subpixel True
    xalign 0.072
    yalign 0.45
    on show:
        zoom 0.0
        ease 0.3 zoom 1.0
        xalign 0.072
        yalign 0.45
    on hide:
        zoom 1.0
        ease 0.3 zoom 0.0
        xalign 0.072
        yalign 0.45

transform phone_confirm_transform_center:
    subpixel True
    xalign 0.527
    yalign 0.45
    on show:
        zoom 0.0
        ease 0.3 zoom 1.0
        xalign 0.527
        yalign 0.45
    on hide:
        zoom 1.0
        ease 0.3 zoom 0.0
        xalign 0.527
        yalign 0.45

style phone_confirm_text is phone_settings_text:
    size 14
    textalign 0.5
    yalign 0.5
    color "#000"
    xalign 0.5
    layout "greedy"

style phone_confirm is phone_settings

style phone_confirm_frame is phone_contacts_frame:
    padding (6, 6, 6, 6)

style phone_confirm_label_text:
    font phone.config.basedir + "Aller_Rg.ttf"
    color "#000"
    outlines []
    size 18
    yalign 0.5
    xalign 0.5