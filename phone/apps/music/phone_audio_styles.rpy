
## Main Player Styles
style phone_music_player_label_text is navigation_button_text:
    font phone.config.basedir + "Aller_Rg.ttf"
    color "#000"
    outlines []
    hover_outlines []
    insensitive_outlines []
    size 22

style phone_music_player_button_text is navigation_button_text:
    font phone.config.basedir + "Aller_Rg.ttf"
    color "#000"
    size 22

style phone_music_player_frame is phone_contacts_frame
style phone_music_window_frame is phone_contacts_frame
style phone_music_settings_frame is phone_contacts_frame

style phone_music_player_text:
    font phone.config.basedir + "Aller_Rg.ttf"
    size 18
    outlines[]
    color "#000"

style phone_music_player_button_text is navigation_button_text

style phone_music_player_hbox:
    spacing 10
    xsize 300

style phone_music_player_frame is phone_contacts_frame

style phone_music_player_bar:
    xsize 320
    ysize 35
    base_bar Frame(phone.config.basedir + "settings_bar.png")
    thumb (phone.config.basedir + "settings_thumb.png")

style phone_music_player_list_bar is phone_music_player_bar:
    xsize 300

transform phone_cover_art_resize(x):
    size(x, x)

## Song Progress Text

style phone_ost_version_text is main_menu_version_text:
    color "#000"
    font phone.config.basedir + "Aller_Rg.ttf"
    size 18
    outlines []

style phone_song_progress_text:
    font phone.config.basedir + "Aller_Rg.ttf"
    size 20
    outlines[]
    color "#000"
    xalign 0.28 
    yalign 0.78

style phone_song_duration_text is phone_song_progress_text:
    xalign 0.79 
    yalign 0.78

## List UI
style phone_music_player_list_title_text is phone_music_player_text:
    size 15
    bold True

style phone_music_player_list_author_text is phone_music_player_text:
    size 13

## Windows
style phone_music_window_button_text is phone_music_player_button_text:
    size 18

style phone_music_window_text is renpy_generic_text:
    size 20
    bold False

style phone_music_settings_label_text:
    font phone.config.basedir + "Aller_Rg.ttf"
    size 18
    color "#000"
    outlines []

style phone_music_player_generic_text is renpy_generic_text:
    size 20
    bold False

style phone_music_list_button_text is navigation_button_text:
    size 18

style phone_l_list:
    left_padding 0