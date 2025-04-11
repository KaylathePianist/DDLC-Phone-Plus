default whichfunction2 = ""

init python in calculator:
    equation = ""
    number1 = ""
    number2 = ""
    whichfunction = ""
    number1temp = ""
    pressedequals = False

    def press(num): 
        global equation
        global number1
        global number2
        global number1temp
        global pressedequals
        if len(equation) == 16:
            pass
        else:
            if pressedequals == True:
                number1temp = ""
                equation = ""
                number1 = ""
                pressedequals = False
            if equation == "error":
                equation = ""
            if number1temp != "":
                number2 = number2 + str(num)
                equation = number2
            else:
                number1 = number1 + str(num)
                equation = number1


    def plus():
        global number1temp
        global number1
        global whichfunction
        global equation
        global pressedequals
        pressedequals = False
        number1temp = number1
        whichfunction = "plus"

    def divide():
        global number1temp
        global number1
        global whichfunction
        global equation
        global pressedequals
        pressedequals = False
        number1temp = number1
        whichfunction = "divide"

    def times():
        global number1temp
        global number1
        global whichfunction
        global equation
        global pressedequals
        pressedequals = False
        number1temp = number1
        whichfunction = "times"

    def minus():
        global number1temp
        global number1
        global whichfunction
        global equation
        global pressedequals
        pressedequals = False
        number1temp = number1
        whichfunction = "minus"

    # Function to evaluate the final expression 
    def equalpress(): 
        # Try and except statement is used 
        # for handling the errors like zero 
        # division error etc. 
    
        # Put that code inside the try block 
        # which may generate the error 
        global number1
        global number2
        global equation
        global number1temp
        try: number1 = float(number1)
        except: number1 = 0.0
        if whichfunction != "":
            if number2 == "":
                equation = "error"
            else:
                number2 = float(number2)

        try: 
    
            global equation
            global number1
            global number2
            global whichfunction
            global pressedequals

            if whichfunction == "plus":
                equation = number1+number2
            elif whichfunction == "minus":
                equation = number1-number2
            elif whichfunction == "times":
                equation = number1*number2
            elif whichfunction == "divide":
                equation = number1/number2
            else:
                if equation != "":
                    equation = number1
                else:
                    equation = 0       
            equation = '{0:g}'.format(equation)
            number1 = equation
            pressedequals = True
            whichfunction = ""
            number2 = ""
            renpy.restart_interaction()



        # if error is generate then handle 
        # by the except block 
        except: 
            global equation
            global number1
            global number2
            global number1temp
            global whichfunction
            number1 = ""
            number2 = ""
            number1temp = ""
            equation = "error"
            whichfunction = ""

            renpy.restart_interaction()

    
    # Function to clear the contents 
    # of text entry box 
    def clear(): 
        global equation
        global number1
        global number2
        global number1temp
        number1temp = ""
        number1 = ""
        number2 = ""
        equation = ""
        renpy.restart_interaction()

init python:
    def equation_text(st, at):
        return Text(calculator.equation, style='phone_number_text'), 0.5

style phone_number_text is phone_confirm_text:
    size 30

image numberdisplay:
    DynamicDisplayable(equation_text)

init python:
    config.keymap['button_select'].remove('K_KP_ENTER')
    config.keymap['button_select'].remove('K_RETURN')

screen phone_calculator():
    use _phone():
        style_prefix "phone_calculator"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Calculator") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:
                    vbox:
                        spacing 10
                        xalign 0.5
                        null height 22
                        add "numberdisplay"
                        null height 10
                    vbox:
                        null height 80
                        xfill True
                        spacing 20
                        hbox:
                            xalign 0.5
                            spacing 10
                            button:
                                xsize 225
                                ysize 70
                                text "Clear" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.clear)
                                keysym ["K_BACKSPACE", "K_DELETE"]
                            button:
                                xsize 70
                                ysize 70
                                text "/" align (0.5, 0.5)
                                if whichfunction2 == "divide":
                                    idle_background "calcbuttonidle"
                                    hover_background "calcbuttonhover"
                                else:
                                    idle_background "calccirclebuttonidle"
                                    hover_background "calccirclebuttonhover"
                                action [Function(calculator.divide), SetVariable("whichfunction2", "divide")]
                                keysym ["K_KP_DIVIDE", "K_SLASH"]
                        hbox:
                            xalign 0.5
                            spacing 10
                            button:
                                xsize 70
                                ysize 70
                                text "7" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 7)
                                keysym ["K_7", "K_KP7"]
                            button:
                                xsize 70
                                ysize 70
                                text "8" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 8)
                                keysym ["K_8", "K_KP8"]
                            button:
                                xsize 70
                                ysize 70
                                text "9" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 9)
                                keysym ["K_9", "K_KP9"]
                            button:
                                xsize 70
                                ysize 70
                                text "x" align (0.5, 0.5)
                                if whichfunction2 == "times":
                                    idle_background "calcbuttonidle"
                                    hover_background "calcbuttonhover"
                                else:
                                    idle_background "calccirclebuttonidle"
                                    hover_background "calccirclebuttonhover"
                                action [Function(calculator.times), SetVariable("whichfunction2", "times")]
                                keysym ["K_ASTERISK", "K_KP_MULTIPLY"]
                        hbox:
                            xalign 0.5
                            spacing 10
                            button:
                                xsize 70
                                ysize 70
                                text "4" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 4)
                                keysym ["K_4", "K_KP4"]
                            button:
                                xsize 70
                                ysize 70
                                text "5" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 5)
                                keysym ["K_5", "K_KP5"]
                            button:
                                xsize 70
                                ysize 70
                                text "6" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 6)
                                keysym ["K_6", "K_KP6"]
                            button:
                                xsize 70
                                ysize 70
                                text "+" align (0.5, 0.5)
                                if whichfunction2 == "plus":
                                    idle_background "calcbuttonidle"
                                    hover_background "calcbuttonhover"
                                else:
                                    idle_background "calccirclebuttonidle"
                                    hover_background "calccirclebuttonhover"
                                action [Function(calculator.plus), SetVariable("whichfunction2", "plus")]
                                keysym ["K_PLUS", "K_KP_PLUS"]
                        hbox:
                            xalign 0.5
                            spacing 10
                            button:
                                xsize 70
                                ysize 70
                                text "1" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 1)
                                keysym ["K_1", "K_KP1"]
                            button:
                                xsize 70
                                ysize 70
                                text "2" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 2)
                                keysym ["K_2", "K_KP2"]
                            button:
                                xsize 70
                                ysize 70
                                text "3" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 3)
                                keysym ["K_3", "K_KP3"]
                            button:
                                xsize 70
                                ysize 70
                                text "-" align (0.5, 0.5)
                                if whichfunction2 == "minus":
                                    idle_background "calcbuttonidle"
                                    hover_background "calcbuttonhover"
                                else:
                                    idle_background "calccirclebuttonidle"
                                    hover_background "calccirclebuttonhover"
                                action [Function(calculator.minus), SetVariable("whichfunction2", "minus")]
                                keysym ["K_MINUS", "K_KP_MINUS"]
                        hbox:
                            xalign 0.5
                            spacing 10
                            button:
                                xsize 145
                                ysize 70
                                text "0" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, 0)
                                keysym ["K_0", "K_KP_0"]
                            button:
                                xsize 70
                                ysize 70
                                text "." align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action Function(calculator.press, ".")
                                keysym ["K_PERIOD", "K_KP_PERIOD"]
                            button:
                                xsize 70
                                ysize 70
                                text "=" align (0.5, 0.5)
                                idle_background "calccirclebuttonidle"
                                hover_background "calccirclebuttonhover"
                                action [Function(calculator.equalpress), SetVariable("whichfunction2", "")]
                                keysym ["K_EQUALS", "K_KP_EQUALS", "K_RETURN", "K_KP_ENTER"]

image calccirclebuttonidle = ConditionSwitch(
    "darkmode", RoundedFrame("#525252", radius=35),
    "True", RoundedFrame("#cdcdcd", radius=35))

image calccirclebuttonhover = ConditionSwitch(
    "darkmode", RoundedFrame("#7e7e7e", radius=35),
    "True", RoundedFrame("#9e9e9e", radius=35))

image calcbuttonidle = ConditionSwitch(
    "darkmode", RoundedFrame("#7e7e7e", radius=35),
    "True", RoundedFrame("#9e9e9e", radius=35))

image calcbuttonhover = ConditionSwitch(
    "darkmode", RoundedFrame("#aaaaaa", radius=35),
    "True", RoundedFrame("#838383", radius=35))

style phone_calculator is phone_confirm

style phone_calculator_frame is phone_contacts_frame

style phone_calculator_button_text is phone_confirm_button_text:
    size 32
    outlines []