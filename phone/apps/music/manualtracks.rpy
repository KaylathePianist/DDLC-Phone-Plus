
init python:    
    ## Manual Soundtracks Options
    #     name - The songs' name [REQUIRED]
    #     author - The songs' artist [REQUIRED]
    #     path - The path to the song [REQUIRED]
    #     album - The songs' album
    #     albumartist - The song' album artist
    #     composer - The songs' composer (person who made the music piece)
    #     genre - The songs' genre
    #     description - The song' description/comment
    #     cover_art - The path to the songs' cover art or 'False'
    #                 (without quotes) if this song has no cover art [REQUIRED]
    #     unlocked = 'True' (without quotes) for unlocked or 
    #                renpy.seen_audio("path/to/song") for True/False 
    #                determination

    your_reality = soundtrack(
        name = "Your Reality",
        author = "Monika",
        path = "bgm/credits.ogg",
        description = "I made mistakes, hurt you, hurt my friends. All I can do is hope you all forgive me.",
        cover_art = False,
        unlocked = True
    )     
    manualDefineList.append(your_reality)
    
    ohayou_sayori = soundtrack(
        name = "Ohayou, Sayori!",
        path = "bgm/2.ogg",
        author = "Dan Salvato",
        description = "ohio sayori lmao lol",
        cover_art = "mod_assets/phone/music_player/logo.png",
        unlocked = True
    )
    manualDefineList.append(ohayou_sayori)

    ## Example

    # poem_panic = soundtrack(
    #     name = "Poem Panic",
    #     path = "bgm/example.ogg",
    #     author = "Dan Salvato",
    #     description = "Example",
    #     unlocked = renpy.seen_audio("bgm/example.ogg")
    # )
    # manualDefineList.append(poem_panic)