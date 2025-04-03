
# Determines Compact Mode or List Mode UIs
# Automatically reverts the music playing before the player launched.
# Add a fadein/out to the track similar to Poweramp or music players with one.
default persistent.fadein = False
default persistent.music_continue = False
default musicispaused = True
default persistent.musicstarted = False

image PhonereadablePos = DynamicDisplayable(ost_info.music_pos)
image PhonereadableDur = DynamicDisplayable(ost_info.music_dur)
image PhonetitleName = DynamicDisplayable(ost_info.dynamic_title_text)

image PhoneauthorName = DynamicDisplayable(ost_info.dynamic_author_text)

image PhonealbumName = DynamicDisplayable(ost_info.dynamic_album_text)

image PhonecoverArt:
    DynamicDisplayable(ost_info.refresh_cover_data)

screen phone_music():
    use _phone():
        style_prefix "phone_music_player"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Music") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:

                    default bar_val = AdjustableAudioPositionValue()
                            
                    if not ost_info.get_current_soundtrack():
                        vbox:
                            ypos 0.1
                            xalign 0.5

                            if persistent.darkmode:
                                text "No music is currently playing.":
                                    color "#fcfcfc"
                                    outlines[]
                                    size 18
                            else:
                                text "No music is currently playing.":
                                    color "#000"
                                    outlines[]
                                    size 18
                            null height 6
                            hbox:
                                style_prefix "phone_settings"
                                button:
                                    text _("Music List") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                                    action [PhoneMenu("phone_music_list_type"), With(Dissolve(0.25))]
                            null height 10
                            hbox:
                                style_prefix "phone_settings"
                                button:
                                    text _("Settings") xalign 0.0 yalign 0.5
                                    text _(">") xalign 1.0 yalign 0.5
                                    action [PhoneMenu("phone_music_settings"), With(Dissolve(0.25))]

                    else:

                        vbox:
                            yalign 0.1
                            spacing 10
                    
                            add "PhonecoverArt" at phone_cover_art_resize(180):
                                xalign 0.5

                            vbox:
                                yalign 0.42

                                vbox:
                                    xsize 340
                                    xoffset 20
                                    add "PhonetitleName" 

                                    add "PhoneauthorName" 

                                    add "PhonealbumName" 
                                null height 15
                                hbox:
                                    xalign 0.5
                                    spacing 15
                                    if persistent.darkmode:
                                        imagebutton:
                                            at transform:
                                                xzoom -1
                                            idle "mod_assets/phone/music_player/refreshDark.png"
                                            hover "mod_assets/phone/music_player/refreshHover.png"
                                            action [SensitiveIf(renpy.music.is_playing(channel='phone_music')), Function(ost_controls.rewind_music)]
                                    else:
                                        imagebutton:
                                            at transform:
                                                xzoom -1
                                            idle "mod_assets/phone/music_player/refreshList.png"
                                            hover "mod_assets/phone/music_player/refreshHover.png"
                                            action [SensitiveIf(renpy.music.is_playing(channel='phone_music')), Function(ost_controls.rewind_music)]

                                    if persistent.darkmode:
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/backwardDark.png"
                                            hover "mod_assets/phone/music_player/backwardHover.png"
                                            action [Function(ost_controls.next_track, True)]
                                    else:
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/backward.png"
                                            hover "mod_assets/phone/music_player/backwardHover.png"
                                            action [Function(ost_controls.next_track, True)]

                                    if ost_controls.pausedState:
                                        if persistent.darkmode:
                                            imagebutton:
                                                idle "mod_assets/phone/music_player/playDark.png"
                                                action [Function(ost_controls.play_music), SetVariable("musicispaused", False)]
                                        else:
                                            imagebutton:
                                                idle "mod_assets/phone/music_player/play.png"
                                                action [Function(ost_controls.play_music), SetVariable("musicispaused", False)]
                                    else:
                                        if persistent.darkmode:
                                            imagebutton:
                                                idle "mod_assets/phone/music_player/pauseDark.png"
                                                action [Function(ost_controls.pause_music), SetVariable("musicispaused", True)]
                                        else:
                                            imagebutton:
                                                idle "mod_assets/phone/music_player/pause.png"
                                                action [Function(ost_controls.pause_music), SetVariable("musicispaused", True)]

                                    if persistent.darkmode:
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/forwardDark.png"
                                            hover "mod_assets/phone/music_player/forwardHover.png"
                                            action [Function(ost_controls.next_track)]
                                    else:
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/forward.png"
                                            hover "mod_assets/phone/music_player/forwardHover.png"
                                            action [Function(ost_controls.next_track)]

                                    if persistent.darkmode:
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/refreshDark.png"
                                            hover "mod_assets/phone/music_player/refreshHover.png"
                                            action [SensitiveIf(renpy.music.is_playing(channel='phone_music')), Function(ost_controls.forward_music)]
                                    else:
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/refreshList.png"
                                            hover "mod_assets/phone/music_player/refreshHover.png"
                                            action [SensitiveIf(renpy.music.is_playing(channel='phone_music')), Function(ost_controls.forward_music)]
                                        
                                null height 20
                                hbox:
                                    xalign 0.5
                                    spacing 15
                                    if persistent.darkmode:
                                        imagebutton:
                                            idle ConditionSwitch("ost_controls.loopSong", "mod_assets/phone/music_player/replayOnDark.png", 
                                                                "True", "mod_assets/phone/music_player/replayDark.png")
                                            hover "mod_assets/phone/music_player/replayHover.png"
                                            action [ToggleVariable("ost_controls.loopSong", False, True)]
                                        imagebutton:
                                            idle ConditionSwitch("ost_controls.randomSong", "mod_assets/phone/music_player/shuffleOnDark.png", 
                                                                "True", "mod_assets/phone/music_player/shuffleDark.png")
                                            hover "mod_assets/phone/music_player/shuffleHover.png"
                                            action [ToggleVariable("ost_controls.randomSong", False, True)]
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/infoDark.png"
                                            hover "mod_assets/phone/music_player/infoHover.png"
                                            action [PhoneMenu("phone_music_info")]
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/musicwindowDark.png"
                                            hover "mod_assets/phone/music_player/musicwindowHover.png"
                                            action [PhoneMenu("phone_music_list_type")]
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/settingsDark.png"
                                            hover "mod_assets/phone/music_player/settingsHover.png"
                                            action [PhoneMenu("phone_music_settings")]
                                    else:
                                        imagebutton:
                                            idle ConditionSwitch("ost_controls.loopSong", "mod_assets/phone/music_player/replayOn.png", 
                                                                "True", "mod_assets/phone/music_player/replay.png")
                                            hover "mod_assets/phone/music_player/replayHover.png"
                                            action [ToggleVariable("ost_controls.loopSong", False, True)]
                                        imagebutton:
                                            idle ConditionSwitch("ost_controls.randomSong", "mod_assets/phone/music_player/shuffleOn.png", 
                                                                "True", "mod_assets/phone/music_player/shuffle.png")
                                            hover "mod_assets/phone/music_player/shuffleHover.png"
                                            action [ToggleVariable("ost_controls.randomSong", False, True)]
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/info.png"
                                            hover "mod_assets/phone/music_player/infoHover.png"
                                            action [PhoneMenu("phone_music_info")]
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/musicwindow.png"
                                            hover "mod_assets/phone/music_player/musicwindowHover.png"
                                            action [PhoneMenu("phone_music_list_type")]
                                        imagebutton:
                                            idle "mod_assets/phone/music_player/settings.png"
                                            hover "mod_assets/phone/music_player/settingsHover.png"
                                            action [PhoneMenu("phone_music_settings")]

                        hbox:
                            yalign 0.82
                            vbox:
                                hbox:
                                    null width 6
                                    bar:
                                        value bar_val
                                        hovered bar_val.hovered
                                        unhovered bar_val.unhovered

                                hbox:
                                    add "PhonereadablePos" 
                                    add "PhonereadableDur" xpos 140

                        hbox:
                            yalign 0.92
                            null width 20
                            if persistent.darkmode:
                                imagebutton:
                                    idle ConditionSwitch("preferences.get_volume(\"phone\") == 0.0", 
                                        "mod_assets/phone/music_player/volumeDark.png", "True", 
                                        "mod_assets/phone/music_player/volumeOnDark.png")
                                    hover ConditionSwitch("preferences.get_volume(\"phone\") == 0.0", 
                                        "mod_assets/phone/music_player/volumeHover.png", "True", 
                                        "mod_assets/phone/music_player/volumeOnHover.png")
                                    action [Function(ost_controls.mute_player)]
                            else:
                                imagebutton:
                                    idle ConditionSwitch("preferences.get_volume(\"phone\") == 0.0", 
                                        "mod_assets/phone/music_player/volume.png", "True", 
                                        "mod_assets/phone/music_player/volumeOn.png")
                                    hover ConditionSwitch("preferences.get_volume(\"phone\") == 0.0", 
                                        "mod_assets/phone/music_player/volumeHover.png", "True", 
                                        "mod_assets/phone/music_player/volumeOnHover.png")
                                    action [Function(ost_controls.mute_player)]
                            bar:
                                style "phone_music_player_bar"
                                value Preference ("phone volume")
                                xsize 200
                                yalign 0.5


                    text "DDLC OST-Player v[ostVersion]":
                        xalign 1.0 yalign 1.0
                        xoffset -10 yoffset -10
                        style "phone_ost_version_text"

                    if not config.developer:
                        hbox:
                            xalign 0.5 
                            yalign 0.98

                            python:
                                try:
                                    renpy.open_file("RPASongMetadata.json")
                                    file_found = True
                                except: file_found = False
                            
                            if not file_found:
                                if persistent.darkmode:
                                    imagebutton:
                                        idle "mod_assets/phone/music_player/osterrorDark.png"
                                        action Show("phone_dialogue", message="{b}Warning{/b}\nThe RPA metadata file hasn't been generated.\nSongs in the {i}track{/i} folder won't be listed if you build your mod without it.\n Set {i}config.developer{/i} to {u}True{/u} in order to generate this file.",
                                            ok_action=Hide("phone_dialogue"))
                                else:
                                    imagebutton:
                                        idle "mod_assets/phone/music_player/osterror.png"
                                        action Show("phone_dialogue", message="{b}Warning{/b}\nThe RPA metadata file hasn't been generated.\nSongs in the {i}track{/i} folder won't be listed if you build your mod without it.\n Set {i}config.developer{/i} to {u}True{/u} in order to generate this file.",
                                            ok_action=Hide("phone_dialogue"))

                    # Start the music playing on entry to the music room.
                    timer 0.01 action [Function(ost_main.ost_start), Stop("music", fadeout=1.0)]

                    # Restore the main menu music upon leaving.


screen phone_music_list_type(type=None):

    use _phone():
        style_prefix "phone_music_window"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Music List") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:

                    frame:

                        side "c":
                            xfill True
                            viewport id "mlt":
                                mousewheel True
                                draggable True
                                has vbox
                                style_prefix "phone_settings"

                                if type is None:
                                    null height 10
                                    button:
                                        text _("All Songs") xalign 0.0 yalign 0.5
                                        text _(">") xalign 1.0 yalign 0.5
                                        action [PhoneReturn(), PhoneMenu("phone_music_list")]
                                    null height 10
                                    button:
                                        text _("Artist") xalign 0.0 yalign 0.5
                                        text _(">") xalign 1.0 yalign 0.5
                                        action [PhoneReturn(), PhoneMenu("phone_music_list", type="artist")]
                                    null height 10
                                    button:
                                        text _("Album Artist") xalign 0.0 yalign 0.5
                                        text _(">") xalign 1.0 yalign 0.5
                                        action [PhoneReturn(), PhoneMenu("phone_music_list_type", type="albumartist")]
                                    null height 10
                                    button:
                                        text _("Composer") xalign 0.0 yalign 0.5
                                        text _(">") xalign 1.0 yalign 0.5
                                        action [PhoneReturn(), PhoneMenu("phone_music_list_type", type="composer")]
                                    null height 10
                                    button:
                                        text _("Genre") xalign 0.0 yalign 0.5
                                        text _(">") xalign 1.0 yalign 0.5
                                        action [PhoneReturn(), PhoneMenu("phone_music_list_type", type="genre")]

                                else:
                                    python:
                                        temp_list = []
                                        for st in soundtracks:
                                            if type == "artist":
                                                if st.author not in temp_list:
                                                    temp_list.append(st.author)
                                            elif type == "albumartist":
                                                if st.albumartist not in temp_list:
                                                    temp_list.append(st.albumartist)
                                            elif type == "composer":
                                                if st.composer not in temp_list:
                                                    temp_list.append(st.composer)
                                            elif type == "genre":
                                                if st.genre not in temp_list:
                                                    temp_list.append(st.genre)
                                        
                                        temp_list = sorted(temp_list)

                                    for st in temp_list:
                                        null height 10
                                        button:
                                            text _("[st]") xalign 0.0 yalign 0.5
                                            text _(">") xalign 1.0 yalign 0.5
                                            action [PhoneReturn(), PhoneMenu("phone_music_list", type=type, arg=st)]

            
screen phone_music_list(type=None, arg=None):

    use _phone():
        style_prefix "phone_music_window"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Music List") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:


                    python:
                        new_soundtrack_list = []
                        for st in soundtracks:
                            if type == "artist":
                                if arg == st.author:
                                    new_soundtrack_list.append(st)
                            elif type == "albumartist":
                                if arg == st.albumartist:
                                    new_soundtrack_list.append(st)
                            elif type == "composer":
                                if arg == st.composer:
                                    new_soundtrack_list.append(st)
                            elif type == "genre":
                                if arg == st.genre:
                                    new_soundtrack_list.append(st)
                            else:
                                new_soundtrack_list.append(st)
                                
                        new_soundtrack_list = sorted(new_soundtrack_list, key=lambda new_soundtrack_list: new_soundtrack_list.name)

                    frame:


                        side "c":
                            xfill True
                            viewport id "ml":
                                draggable True
                                mousewheel True
                                has vbox
                                style_prefix "phone_settings"

                                for nst in new_soundtrack_list:
                                    null height 10
                                    button:
                                        text _("[nst.name]") xalign 0.0 yalign 0.5
                                        text _(">") xalign 1.0 yalign 0.5
                                        action [PhoneReturn(), Function(ost_info.set_current_soundtrack, nst), Function(ost_controls.play_music)]

screen phone_music_settings():
    use _phone():
        style_prefix "phone_music_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Music Settings") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:

                    frame:

                        side "c":
                            xfill True
                            yfill True

                            viewport id "mlt":
                                mousewheel True
                                draggable True
                                has vbox
                                

                                vbox:
                                    null height 10
                                    hbox:
                                        xfill True
                                        style_prefix "phone_settings2"
                                        text _("Fade In/Out") yalign 0.5
                                        imagebutton:
                                            xalign 1.0 yalign 0.5
                                            idle (phone.config.basedir + "settings1.png")
                                            selected_idle (phone.config.basedir + "settings3.png")
                                            hover (phone.config.basedir + "settings2.png")
                                            selected_hover (phone.config.basedir + "settings4.png")
                                            action InvertSelected(ToggleField(persistent, "fadein", False, True))
                                    null height 5
                                    if persistent.darkmode:
                                        add Solid("#fff"):
                                            xysize (1.0, 1) nearest True 
                                    else:
                                        add Solid("#000"):
                                            xysize (1.0, 1) nearest True 
                                    null height 5
                                    hbox:
                                        xfill True
                                        style_prefix "phone_settings2"
                                        text _("Continue Outside Phone") yalign 0.5
                                        imagebutton:
                                            xalign 1.0 yalign 0.5
                                            idle (phone.config.basedir + "settings1.png")
                                            selected_idle (phone.config.basedir + "settings3.png")
                                            hover (phone.config.basedir + "settings2.png")
                                            selected_hover (phone.config.basedir + "settings4.png")
                                            action InvertSelected(ToggleField(persistent, "music_continue", False, True))
                                    null height 10
                                    hbox:
                                        style_prefix "phone_settings"
                                        button:
                                            action Show("phone_dialogue", message="DDLC OST-Player by Bronya-Rand.\nCopyright © 2020-2023 BronyaRand.\nAdapted into Phone+ by Caleb Spjute..", ok_action=Hide("phone_dialogue"))
                                            hbox:
                                                xfill True
                                                text _("About DDLC OST-Player") xalign 0.0 yalign 0.5
                                                text _(">") xalign 1.0 yalign 0.5

screen phone_music_info():

    use _phone():
        style_prefix "phone_music_window"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Song Info") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:

                    frame:

                        side "c":
                            xpos 0.05
                            ypos 0.2
                            xfill True

                            viewport id "mi":
                                mousewheel True
                                draggable True
                                has vbox
                                style_prefix "phone_settings"

                                python:
                                    albumartist = ost_info.get_album_artist()
                                    composer = ost_info.get_composer()
                                    genre = ost_info.get_genre()
                                    sideloaded = ost_info.get_sideload()
                                    comment = ost_info.get_description() or None
                                
                                text "{u}Album Artist{/u}: [albumartist]"
                                text "{u}Composer{/u}: [composer]"
                                text "{u}Genre{/u}: [genre]"
                                text "{u}Sideloaded{/u}: [sideloaded]"
                                text "{u}Comment{/u}: [comment]"

