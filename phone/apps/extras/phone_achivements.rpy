screen phone_achievements():
    use _phone():
        style_prefix "phone_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Achievements") xalign 0.5 text_align 0.5
            viewport:
                yfill True
                fixed:

                    vbox:
                        ypos 0.01
                        xpos 0.15

                        hbox:

                            if selectedAchievement:

                                add ConditionSwitch(
                                        selectedAchievement.unlocked, selectedAchievement.image, "True",
                                        selectedAchievement.locked) at achievement_scaler(64)
                            else:
                                null height 75

                            spacing 20

                            vbox:
                                ypos 0.2

                                if selectedAchievement:

                                    text selectedAchievement.name

                                    if not selectedAchievement.unlocked and not selectedAchievement.show_desc_while_locked:
                                        if isinstance(selectedAchievement, AchievementCount):
                                            text "[selectedAchievement.locked_desc] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                        else:
                                            text selectedAchievement.locked_desc
                                    else:
                                        if isinstance(selectedAchievement, AchievementCount):
                                            text "[selectedAchievement.description] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                        else:
                                            text selectedAchievement.description
                                else:
                                    null height 80

                    # This vpgrid is responsible for the list of achievements in the game.
                    vpgrid:
                        cols 5
                        spacing 6
                        mousewheel True
                        draggable True

                        xalign 0.5
                        yoffset 80
                        for name, al in achievementList.items():

                            imagebutton:
                                idle Transform(ConditionSwitch(
                                        al.unlocked, al.image, "True",
                                        al.locked), size=(64,64))
                                action SetVariable("selectedAchievement", al)
