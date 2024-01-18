screen snake_overlay(snake):
    style_prefix "snake_overlay"

    if snake.has_started():
        vbox:
            align (0.0, 0.0)
            null height 360
            add DynamicDisplayable(snake_app.score_count, snake=snake)
            add DynamicDisplayable(snake_app.hi_score, snake=snake)
        
        showif snake.is_paused():
            add "#0008"

            vbox:
                text _("PAUSED") style_suffix "title"
                text _("Click to resume.") 

        elif snake.is_gameover():
            add "#0008"

            vbox:
                text _("GAME OVER") style_suffix "title"
                $ score = snake.get_score()
                text _("Score: [score]")
                $ high_score = snake.get_high_score()
                if score > high_score:
                    text _("New High Score!")
                text _("Click to restart.")

    else:
        vbox:
            align (0.0, 0.0)
            null height 360
            text _("Click to start.")
    fixed:
        imagebutton:
            idle phone.config.basedir + "snake_play_icon.png"
            action Function(snake.imagebuttoneventup)
            at snakerotate2
            yoffset 355
            xpos 0.5
        imagebutton:
            idle phone.config.basedir + "snake_play_icon.png"
            action Function(snake.imagebuttoneventleft)
            at snakerotate3
            yoffset 417
            xpos 0.33
        imagebutton:
            idle phone.config.basedir + "snake_play_icon.png"
            action NullAction()
            at snakeinvis
            yoffset 420
            xpos 0.5
        imagebutton:
            idle phone.config.basedir + "snake_play_icon.png"
            action Function(snake.imagebuttoneventright)
            yoffset 426
            xpos 0.71
            at snakezoomonly
        imagebutton:
            idle phone.config.basedir + "snake_play_icon.png"
            action Function(snake.imagebuttoneventdown)
            at snakerotate
            yoffset 485
            xpos 0.5
        imagebutton:
            idle phone.config.basedir + "pause_icon.png"
            action Function(snake.pausebutton)
            yoffset 440
            xpos 0.03
            at snakezoomonly

transform snakezoomonly:
    zoom 1.8

transform snakeinvis:
    alpha 0.0
    zoom 1.8

transform snakerotate:
    rotate 90
    zoom 1.8

transform snakerotate2:
    rotate -90
    zoom 1.8

transform snakerotate3:
    rotate 180
    zoom 1.8

style snake_overlay_frame is empty
style snake_overlay_vbox is empty
style snake_overlay_text is empty

style snake_overlay_title is snake_overlay_text

style snake_overlay_frame:
    background "#0008"
    padding (0, 0)

style snake_overlay_vbox:
    align (0.5, 0.5)

style snake_overlay_text:
    font phone.config.basedir + "Aller_Rg.ttf"
    xalign 0.5

style snake_overlay_title:
    font phone.config.basedir + "Aller_Rg.ttf"
    size 36

screen phone_snake():

    use _phone():
        style_prefix "phone_calendar"

        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Snake") xalign 0.5 text_align 0.5

            style_prefix "snake"
            default snake = snake.SnakeOverlay()

            fixed:
                xfill True
                xalign 0.5
                add snake
                use snake_overlay(snake)

style snake_fixed is empty

style snake_fixed:
    fit_first True

init python in snake_app:
    from store import Text

    def score_count(st, at, snake):
        d = Text("Score: {}".format(snake.get_score()), color="#fff")
        return d, 0.0
    
    def hi_score(st, at, snake):
        hs = Text("High Score: {}".format(snake.get_high_score()), color="#fff")
        return hs, 0.0

default persistent.hiscore = 10