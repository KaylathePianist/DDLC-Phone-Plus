# /!\ default
# pc as in phone character :monikk:

default persistent.playercolor = "#484848"
default persistent.s_color = "#22Abf8"
default persistent.y_color = "#a327d6"
default persistent.m_color = "#0a0"
default persistent.n_color = "#fbb"

define pc_mc      = phone.character.Character('MC', phone.asset("mc_icon.png"), "mc", 35, persistent.playercolor)
define pc_sayori  = phone.character.Character('Sayori', phone.asset("sayori_icon.png"), "s", 21, persistent.s_color)
define pc_monika  = phone.character.Character('Monika', phone.asset("monika_icon.png"), "m", 40, persistent.m_color)
define pc_yuri    = phone.character.Character('Yuri', phone.asset("yuri_icon.png"), "y", 20, persistent.y_color)
define pc_natsuki = phone.character.Character('Natsuki', phone.asset("natsuki_icon.png"), "n", 45, persistent.n_color)


default pov_key = "mc"

define phone_mc = Character(kind=mc, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_s  = Character(kind=s, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_m  = Character(kind=m, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_y  = Character(kind=y, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_n  = Character(kind=n, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

default mc_sayo_gc = phone.group_chat.GroupChat('Sayori', phone.asset("sayori_icon.png"), "mc_sayo").add_character("mc").add_character("s")

init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)
    add_app_to_all_characters(camera_app)
    add_app_to_all_characters(photos_app)
    add_app_to_all_characters(calculator_app)
    add_app_to_all_characters(music_app)
    add_app_to_all_characters(awards_app)
    add_app_to_all_characters(about_app)
    add_app_to_all_characters(settings_app, page=None)
    add_app_to_all_characters(dialogue_history_app, page=None)
    add_app_to_all_characters(save_app, page=None)
    add_app_to_all_characters(load_app, page=None)

init 100 python in phone.calendar:
    add_calendar_to_all_characters(2023, 11, SUNDAY)
    mc_nov_2023_calendar = get_calendar(2023, 11)
    mc_nov_2023_calendar[22].description ="The release of Phone+ was today! Hooray!"

label phone_discussion_test:
    $ test_phoneplus_gc = phone.group_chat.GroupChat('Sayori', phone.asset("sayori_icon.png"), "phoneplus").add_character("mc").add_character("s").add_character("m").add_character("n")
    phone discussion "phoneplus":
        time year 2023 month 11 day 19 hour 19 minute 31 delay -1
        label "'[player]' added 'Sayori' to the group" delay -1
        "mc" "Hey there!"
        "mc" "Thank you for using the Phone+ addon!"
        "s" "Thanks to Elckarow for making the original Better EMR Phone!"
        "s" "He did all of the actual phone stuff like calling, texting, and making the phone work!"
        "mc" "Yeah, I just ported stuff and added menu screens to this thing."
        "mc" "Some stuff is ported from Bronya-Rand's {a=https://github.com/Bronya-Rand/DDLCModTemplate2.0}Mod Template{/a} extras..."
        "s" "And the {a=https://github.com/Bronya-Rand/DDLC-OSTPlayer}Music Player{/a} is originally by them too!"
        "mc" "If you don't really need all this extra stuff, just download the original version {a=https://github.com/Elckarow/Better-EMR-Phone}here.{/a}"
        "mc" "If you are interested in DDLC mods, be sure to check out the mod {a=https://undercurrentsmod.weebly.com}Doki Doki Undercurrents{/a}!"
        "mc" "Elckarow made this phone partially for that mod, and it's also a pretty cool mod in general."
        "mc" "In case you encounter an issue (or wanna make a suggestion),"
        "mc" "please DM Elckarow on Discord or open an issue on {a=https://github.com/Elckarow/Better-EMR-Phone}GitHub{/a}."
        "s" "but if the question is about some of the new features, then DM calebthepianist on Discord instead!"
        "s" "otherwise elbow might fridge react you, ehehe..."
        label "'Natsuki' has added herself to the group" delay -1
        "n" "ugh, what does that even mean?"
        "n" "just use a normal emoji or something!"
        "n" "{emoji=natpissed}"
        "s" "Wow, that looks just like you!"
        "n" "yeah, there's also a bunch of emojis in here!"
        "n" "we even have some stickers made by Leomonade!"
        sticker "n" "n6"
        "s" "you can look in the files to see what the emojis and stickers look like! ehehe..."
        "s" "so you don't have to define your own stuff..."
        "n" "unless you want to add even more {emoji=monishrug}"
        label "'Natsuki' added 'Monika' to the group" delay -1
        "n" "Monika, explain the other new stuff."
        "m" "Some of the new features include a calculator, a camera that will save screenshots to your files, and an app to view those photos!"
        "m" "Plus, the music player and the extra screens from the mod template have been ported to this thing!"
        "n" "that's pretty cool i guess"
        "n" "there are also audio messages, but those have always been here"
        audio "n" "bgm/2g.ogg"
        "s" "guys, stop talking, just let them mess around and test out the phone!"
        "m" "ahaha, you're right."
    phone end discussion
    call phone_screen_test
    return

label phone_call_test:
    if is_renpy_version_or_above(7, 6, 0):
        phone call "s" video
        show bg sayori_bedroom onlayer phone_video_call
        show sayori 4x at i11 onlayer phone_video_call
        phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
        show sayori 1a at t42
        phone_mc "Um...hi?"
        show sayori at t43
        pause 1.0
        show sayori at t11
        "Why is she always this energetic?"
        phone_mc "Well, thanks for showing me all of this stuff."
        show sayori 1x
        phone_s "No problem, [player]! Have fun with it!"
        show sayori 2x
        phone_s "Byeeeeee~"
        phone end call
        "..."
    else:
        phone call "s"
        phone_s "Ohayouuuu!!!!!!"
        phone_mc "Um...hi?"
        "why is she always this energetic?"
        phone_mc "Well, thanks for showing me all of this stuff."
        phone_s "no problem, [player]! Have fun with it!"
        phone_s "Byeeeeee~"
        phone end call
        "..."
    phone discussion "phoneplus":
        "m" "so, yeah! That's about it!"
        "m" "Again, if you have any questions, make sure to ask either Elckarow or CalebthePianist on Discord depending on what the question is about~"
        "n" "if you aren't really sure, just ask Caleb. Elbow usually just tells you to 'read the docs' and that doesn't always help me, ugh..."
        "s" "Natsuki! Stop complaining!"
        "n" "fine, fine, whatever."
        "m" "Thanks for using the Phone+!"
        sticker "m" "m4"
        "m" "ahaha~"
    phone end discussion
    return

default phonetest_done = False
default phonetest_speak = False

label phone_screen_test:
    "..."
    $ phone.call_screen("phone")
    "..."
    if not phonetest_speak:
        phone discussion "phoneplus":
            "m" "So, done checking it out?"
            menu:
                "Yep!":
                    $ phonetest_done = True
                    "mc" "Yep!"
                "(I'm not finished yet)":
                    $ phonetest_speak = True
    else:
        phone discussion "phoneplus":
            menu:
                "Yep!":
                    $ phonetest_done = True
                    "mc" "Yep!"
                "(I'm not finished yet)":
                    $ phonetest_speak = True
    phone discussion:
        if phonetest_done == True:
            "m" "Great!"
            "m" "Let's show you a phone call example, too."
            "s" "I'll call you!"
            "s" "If you're on a new enough version of Renpy, then we can even do video calls!"
            "n" "specifically, at least renpy 7.6!"
            "n" "and there's not really any reason to use an old version anyways!"
            "mc" "I can agree with that {emoji=smile}"
            "mc" "Anyways, go ahead and call me, Sayori."
            pass
    if phonetest_done == True:
        phone end discussion
        call phone_call_test
        return
    else:
        phone end discussion
        jump phone_screen_test
