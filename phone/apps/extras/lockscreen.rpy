init -1 default lockscreen.pwtimes = 0
init -1 default lockscreen.pwcorrect = False
init -1 default lockscreen.pwlocked = False
init -1 default lockscreen.pwincorrect = False

init python in lockscreen:
    from renpy.store import store, Transform
    from store.phone import config
    correct = phone.config.passcode
    pwinput = ""
    pwdisplay = ""
    pwincorrect = False
    pwattempts = phone.config.pass_attempts
    def press(num):
        global correct
        global pwinput
        global pwdisplay
        global pwtimes
        global pwcorrect
        global pwincorrect
        global pwlocked
        if pwdisplay == "Incorrect":
            pwinput = ""
            pwdisplay = ""
        if pwcorrect == True:
            pass
        elif pwattempts > 0 and pwtimes == pwattempts:
            pwdisplay = "Phone locked."
            pwlocked = True
            pass
        if pwlocked == True:
            pass
        else:
            pwinput = pwinput + str(num)
            pwdisplay = pwdisplay + "*"
        if len(pwinput) == 6:
            if pwinput == correct:
                pwdisplay = "Correct"
                pwcorrect = True
            else:
                global pwtimes
                pwdisplay = "Incorrect"
                pwtimes += 1
                pwincorrect = True
        renpy.restart_interaction()

init python:
    def updatelockscreen():
        if lockscreen.pwlocked == True:
            lockscreen.pwdisplay = "Phone locked."
            renpy.restart_interaction()

init python:
    def lockscreen_text(st, at):
        return Text(lockscreen.pwdisplay, style='phone_lock_text'), 0.5

image lockscreendisplay:
    DynamicDisplayable(lockscreen_text)

screen phone_lock_screen():
    style_prefix "phone_lockscreen"
    side "c":
        viewport:
            draggable True
            mousewheel True
            yfill True
            frame:
                vbox:
                    spacing 40
                    xalign 0.5
                    null height 22
                    text "Enter passcode or use touch id" size 18
                    add "lockscreendisplay"
                    null height 10
                vbox:
                    null height 180
                    xfill True
                    spacing 20
                    hbox:
                        xalign 0.5
                        spacing 25
                        button:
                            xsize 80
                            ysize 80
                            text "1" align (0.5, 0.2) size 30
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 1)
                        button:
                            xsize 80
                            ysize 80
                            text "2" align (0.5, 0.2) size 30
                            text "A B C" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 2)
                        button:
                            xsize 80
                            ysize 80
                            text "3" align (0.5, 0.2) size 30
                            text "D E F" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 3)
                    hbox:
                        xalign 0.5
                        spacing 25
                        button:
                            xsize 80
                            ysize 80
                            text "4" align (0.5, 0.2) size 30
                            text "G H I" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 4)
                        button:
                            xsize 80
                            ysize 80
                            text "5" align (0.5, 0.2) size 30
                            text "J K L" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 5)
                        button:
                            xsize 80
                            ysize 80
                            text "6" align (0.5, 0.2) size 30
                            text "M N O" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 6)
                    hbox:
                        xalign 0.5
                        spacing 25
                        button:
                            xsize 80
                            ysize 80
                            text "7" align (0.5, 0.2) size 30
                            text "P Q R S" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 7)
                        button:
                            xsize 80
                            ysize 80
                            text "8" align (0.5, 0.2) size 30
                            text "T U V" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 8)
                        button:
                            xsize 80
                            ysize 80
                            text "9" align (0.5, 0.2) size 30
                            text "W X Y Z" align (0.5, 0.85) size 16
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 9)
                    hbox:
                        xalign 0.5
                        spacing 10
                        button:
                            xsize 80
                            ysize 80
                            text "0" align (0.5, 0.2) size 30
                            idle_background RoundedFrame("#525252", radius=(45, 45, 45, 45))
                            hover_background RoundedFrame("#7e7e7e", radius=(45, 45, 45, 45))
                            action Function(lockscreen.press, 0)

            if lockscreen.pwcorrect == True:
                timer 0.3 action [Notify("Phone unlocked."), SetVariable("phone2", "Unlocked"), SetVariable("phoneunlocked1", True), SetField(persistent, "phoneunlocked", True)]
            if lockscreen.pwincorrect == True:
                timer 0.3 action [Notify("Incorrect password.")]
            if phonelocked1 == True:
                timer 0.02 action [SetField(lockscreen, "pwlocked", True), Function(updatelockscreen)]
            if lockscreen.pwlocked == True:
                timer 0.01 action SetField(persistent, "phonelocked", True)
            if lockscreen.pwlocked == True:
                timer 0.01 action Function(lockedout.unlock)

default persistent.phonelocked = False
default persistent.phoneunlocked = False

style phone_lock_text is phone_number_text:
    color "#ffffff"

style phone_lockscreen is phone_confirm

style phone_lockscreen_text is phone_confirm_text:
    color "#ffffff"

style phone_lockscreen_frame is phone_contacts_frame:
    padding (0, 0, 0, 0)
    background "#3f3f3f"

style phone_lockscreen_button_text is phone_confirm_button_text:
    size 32
    outlines []