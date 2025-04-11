default lockscreen.pwtimes = 0
default lockscreen.pwcorrect = False
default lockscreen.pwlocked = False
default lockscreen.pwincorrect = False
default phonelocked = False
default phoneunlocked = False

init python in lockscreen:
    from renpy import store
    from store import phone
    from store.phone import config
    config.hide_status_bar_screens.append("phone_lockscreen")
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
        if store.phonelocked:
            return
        if pwdisplay == "Incorrect":
            pwinput = ""
            pwdisplay = ""
        if pwlocked == True:
            pwinput = ""
            pass
        elif pwcorrect == True:
            pwinput = ""
            pass
        else:
            pwinput = pwinput + str(num)
            pwdisplay = pwdisplay + "*"
        if len(pwinput) == 6:
            if pwinput == correct:
                pwdisplay = "Correct"
                pwcorrect = True
            elif pwattempts > 0 and pwtimes == pwattempts:
                pwdisplay = "Phone locked."
                pwlocked = True
                pwinput = ""
                pass
            else:
                pwdisplay = "Incorrect"
                pwtimes += 1
                pwincorrect = True
        renpy.restart_interaction()

init python:
    def lockscreen_text(st, at):
        if phonelocked:
            return Text("Phone locked.", style="phone_lock_text"), 0.5
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
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 1)
                            keysym ["K_1", "K_KP_1"]
                        button:
                            xsize 80
                            ysize 80
                            text "2" align (0.5, 0.2) size 30
                            text "A B C" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 2)
                            keysym ["K_2", "K_KP_2"]
                        button:
                            xsize 80
                            ysize 80
                            text "3" align (0.5, 0.2) size 30
                            text "D E F" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 3)
                            keysym ["K_3", "K_KP_3"]
                    hbox:
                        xalign 0.5
                        spacing 25
                        button:
                            xsize 80
                            ysize 80
                            text "4" align (0.5, 0.2) size 30
                            text "G H I" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 4)
                            keysym ["K_4", "K_KP_4"]
                        button:
                            xsize 80
                            ysize 80
                            text "5" align (0.5, 0.2) size 30
                            text "J K L" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 5)
                            keysym ["K_5", "K_KP_5"]
                        button:
                            xsize 80
                            ysize 80
                            text "6" align (0.5, 0.2) size 30
                            text "M N O" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 6)
                            keysym ["K_6", "K_KP_6"]
                    hbox:
                        xalign 0.5
                        spacing 25
                        button:
                            xsize 80
                            ysize 80
                            text "7" align (0.5, 0.2) size 30
                            text "P Q R S" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 7)
                            keysym ["K_7", "K_KP_7"]
                        button:
                            xsize 80
                            ysize 80
                            text "8" align (0.5, 0.2) size 30
                            text "T U V" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 8)
                            keysym ["K_8", "K_KP_8"]
                        button:
                            xsize 80
                            ysize 80
                            text "9" align (0.5, 0.2) size 30
                            text "W X Y Z" align (0.5, 0.85) size 16
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 9)
                            keysym ["K_9", "K_KP_9"]
                    hbox:
                        xalign 0.5
                        spacing 10
                        button:
                            xsize 80
                            ysize 80
                            text "0" align (0.5, 0.2) size 30
                            idle_background "circlebuttonidle"
                            hover_background "circlebuttonhover"
                            action Function(lockscreen.press, 0)
                            keysym ["K_0", "K_KP_0"]

    if lockscreen.pwcorrect:
        timer 0.2 action Call("correct_code", from_current=True)
    if lockscreen.pwlocked:
        timer 0.2 action Call("wrong_code", from_current=True)

label correct_code:
    $ phoneunlocked = True
    $ lockscreen.pwcorrect = False
    "The phone unlocks. I got the correct code!"
    $ phone.menu = False
    $ phone._stack_depth = 0
    $ phone.call_screen("phone")
    return

label wrong_code:
    $ phonelocked = True
    $ lockscreen.pwlocked = False
    "The phone displays the words 'Phone locked.'"
    "This can't be good."
    return

style phone_lock_text is phone_number_text

style phone_lockscreen is phone_confirm

style phone_lockscreen_text is phone_confirm_text

style phone_lockscreen_frame is phone_contacts_frame:
    padding (0, 0, 0, 0)
    background "#dbdbdb"

style phone_lockscreen_button_text is phone_confirm_button_text:
    size 32
    outlines []

init python:
    renpy.register_style_preference("mode", "light", style.phone_lockscreen_frame, "background", "#dbdbdb")
    renpy.register_style_preference("mode", "dark", style.phone_lockscreen_frame, "background", "#3f3f3f")