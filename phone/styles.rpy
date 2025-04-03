init python:
    renpy.register_style_preference("mode", "light", style._phone_application_button_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_main_text, "color", "#fff")
    renpy.register_style_preference("mode", "light", style.phone_main_frame_bottom_frame, "background", "#ffffff62")
    renpy.register_style_preference("mode", "light", style.app_base_frame, "background", "#F2F2F2")
    renpy.register_style_preference("mode", "light", style.app_base_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.app_base_button_text, "color", "#0094FF")
    renpy.register_style_preference("mode", "light", style.phone_calendar_button_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_calendar_notes_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_calendar_notes_frame, "background", RoundedFrame("#e0e0e0", radius=(0, 25, 0, 25)))
    renpy.register_style_preference("mode", "light", style.phone_call_history_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_confirm_text, "color", "#000000")
    renpy.register_style_preference("mode", "light", style.phone_confirm_label_text, "color", "#000000")
    renpy.register_style_preference("mode", "light", style.phone_contacts_button, "hover_background", Solid("#e4e4e4"))
    renpy.register_style_preference("mode", "light", style.phone_contacts_text, "color", "#525252")
    renpy.register_style_preference("mode", "light", style.phone_contacts_no_friends_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_contacts_date_text, "color", "#9d9d9d")
    renpy.register_style_preference("mode", "light", style.phone_typing_frame, "background", phone.character.get_textbox("#f2f2f2"))
    renpy.register_style_preference("mode", "light", style.phone_typing_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_typing_istyping_text, "color", "#626262")
    renpy.register_style_preference("mode", "light", style.phone_textbox_frame, "background", "#F2F2F2")
    renpy.register_style_preference("mode", "light", style.phone_textbox_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_messages_choice_button_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_messages_choice_button, "background", RoundedFrame(Solid("#eeeeee"), radius=phone.config.textbox_radius, outline_width=2.0, outline_color="#9b9b9b"))
    renpy.register_style_preference("mode", "light", style.phone_messages_choice_button, "hover_background", RoundedFrame(Solid("#b4b4b4"), radius=phone.config.textbox_radius, outline_width=2.0, outline_color="#4d4d4d"))
    renpy.register_style_preference("mode", "light", style.phone_messages_text_label, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_messages_button_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_page_label_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_page_label_text, "outlines", [(2, "#fff", 0, 0), (1, "#fff", 1, 1)])
    renpy.register_style_preference("mode", "light", style.phone_slot_button_text, "color", "#666")
    renpy.register_style_preference("mode", "light", style.phone_history_label_text, "color", "#525252")
    renpy.register_style_preference("mode", "light", style.phone_history_text, "color", "#000000")
    renpy.register_style_preference("mode", "light", style.phone_history_name_text, "color", "#525252")
    renpy.register_style_preference("mode", "light", style.phone_history_frame, "background", "#fff")
    renpy.register_style_preference("mode", "light", style.phone_history_window, "background", "#fff")
    renpy.register_style_preference("mode", "light", style.phone_history_vbox, "background", "#fff")
    renpy.register_style_preference("mode", "light", style.phone_history_viewport, "background", "#fff")
    renpy.register_style_preference("mode", "light", style.phone_settings_text, "color", "#525252")
    renpy.register_style_preference("mode", "light", style.phone_settings2_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_settings_button, "idle_background", "#e4e4e4")
    renpy.register_style_preference("mode", "light", style.phone_settings_button, "hover_background", "#999999")
    renpy.register_style_preference("mode", "light", style.phone_music_player_label_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_music_player_button_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_music_player_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_song_progress_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_music_settings_label_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_ost_version_text, "color", "#000")
    renpy.register_style_preference("mode", "light", style.phone_save_input, "color", "#000")


    renpy.register_style_preference("mode", "dark", style._phone_application_button_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_main_text, "color", "#797979")
    renpy.register_style_preference("mode", "dark", style.phone_main_frame_bottom_frame, "background", "#00000062")
    renpy.register_style_preference("mode", "dark", style.app_base_frame, "background", "#2b2b2b")
    renpy.register_style_preference("mode", "dark", style.app_base_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.app_base_button_text, "color", "#00d61d")
    renpy.register_style_preference("mode", "dark", style.phone_calendar_button_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_calendar_notes_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_calendar_notes_frame, "background", RoundedFrame("#222222", radius=(0, 25, 0, 25)))
    renpy.register_style_preference("mode", "dark", style.phone_call_history_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_confirm_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_confirm_label_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_contacts_button, "hover_background", Solid("#2b2b2b"))
    renpy.register_style_preference("mode", "dark", style.phone_contacts_text, "color", "#ececec")
    renpy.register_style_preference("mode", "dark", style.phone_contacts_no_friends_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_contacts_date_text, "color", "#cccccc")
    renpy.register_style_preference("mode", "dark", style.phone_typing_frame, "background", phone.character.get_textbox("#252525"))
    renpy.register_style_preference("mode", "dark", style.phone_typing_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_typing_istyping_text, "color", "#e9e9e9")
    renpy.register_style_preference("mode", "dark", style.phone_textbox_frame, "background", "#131313")
    renpy.register_style_preference("mode", "dark", style.phone_textbox_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_messages_choice_button_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_messages_choice_button, "background", RoundedFrame(Solid("#333333"), radius=phone.config.textbox_radius, outline_width=2.0, outline_color="#636363"))
    renpy.register_style_preference("mode", "dark", style.phone_messages_choice_button, "hover_background", RoundedFrame(Solid("#535353"), radius=phone.config.textbox_radius, outline_width=2.0, outline_color="#b9b9b9"))
    renpy.register_style_preference("mode", "dark", style.phone_messages_text_label, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_messages_button_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_page_label_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_page_label_text, "outlines", [(2, "#000000", 0, 0), (1, "#000000", 1, 1)])
    renpy.register_style_preference("mode", "dark", style.phone_slot_button_text, "color", "#cecece")
    renpy.register_style_preference("mode", "dark", style.phone_history_label_text, "color", "#b6b6b6")
    renpy.register_style_preference("mode", "dark", style.phone_history_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_history_name_text, "color", "#b6b6b6")
    renpy.register_style_preference("mode", "dark", style.phone_history_frame, "background", "#202020")
    renpy.register_style_preference("mode", "dark", style.phone_history_window, "background", "#202020")
    renpy.register_style_preference("mode", "dark", style.phone_history_vbox, "background", "#202020")
    renpy.register_style_preference("mode", "dark", style.phone_history_viewport, "background", "#000000")
    renpy.register_style_preference("mode", "dark", style.phone_settings_text, "color", "#b6b6b6")
    renpy.register_style_preference("mode", "dark", style.phone_settings2_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_settings_button, "idle_background", "#292929")
    renpy.register_style_preference("mode", "dark", style.phone_settings_button, "hover_background", "#575757")
    renpy.register_style_preference("mode", "dark", style.phone_music_player_label_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_music_player_button_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_music_player_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_song_progress_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_music_settings_label_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_ost_version_text, "color", "#ffffff")
    renpy.register_style_preference("mode", "dark", style.phone_save_input, "color", "#ffffff")

init python:

    # Define function to open the menu
    global main_menu
    global in_splash
    def show_phone_menu():
        if not renpy.get_screen("_phone"):
            if not renpy.get_screen("phone_contacts"):
                if not renpy.get_screen("phone_discussion"):
                    if not renpy.get_screen("phone_savegame"):
                        if not renpy.get_screen("phone_loadgame"):
                            if not renpy.get_screen("phone_settings"):
                                if not renpy.get_screen("phone_dialogue_history"):
                                    if not renpy.get_screen("phone_call_history"):
                                        if not renpy.get_screen("phone_calendar"):
                                            if not renpy.get_screen("phone_say"):
                                                if not renpy.get_screen("phone_advanced"):
                                                    if not renpy.get_screen("phone_video_call"):
                                                        if not renpy.get_screen("phone_call"):
                                                            if not renpy.get_screen("phone_saveload"):
                                                                if not renpy.get_screen("_phone_image"):
                                                                    if not renpy.get_screen("phone_calculator"):
                                                                        if not renpy.get_screen("phone_achievements"):
                                                                            if not renpy.get_screen("photos_gallery"):
                                                                                if not renpy.get_screen("photos_gallery2"):
                                                                                    if not renpy.get_screen("photos_gallery3"):
                                                                                        if not renpy.get_screen("phone_music"):
                                                                                            if not renpy.get_screen("_phone_image2"):
                                                                                                if not renpy.get_screen("phone_camera"):
                                                                                                    if not renpy.get_screen("phone_info"):
                                                                                                        if not main_menu:
                                                                                                            if not in_splash:
                                                                                                                phone.call_screen("phone")

    # Add key to 'open_pause_menu', this case is 'a' on keyboard
    config.keymap["open_phone_menu"] = ["K_ESCAPE"]
    
    # When key is pressed at anytime, open custom screen.
    config.underlay.append(renpy.Keymap(open_phone_menu=show_phone_menu))

