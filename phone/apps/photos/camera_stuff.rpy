default persistent.photos = []


init python:
    import os, hashlib, io
    from datetime import datetime
    #This function is called by the UI button when it is clicked.
    def camera_take_photo():

        # First we call the actual photo taking function and save the return value in newPhoto

        newPhoto = renpy.invoke_in_new_context(_camera_take_photo)

        # Now we display a transition that looks like a camera flash. This makes it look really good. ;)

        renpy.transition(Fade(0,0,0.5,color=(255,255,255,255)))

        # The saved photo name is now added to photos. Photos is a list that keeps track of the photos
        # we have already taken. Since the photoname is also the filename, use this name to load the
        # photos.

        persistent.photos.append(newPhoto)

        # Now we return to the parent function. In this case it's the one responsible for building the camera
        # UI, but it might be different in your case. You might not need this at all.

        ###### return "photo_taken"
    
    # This function is called by the one above and takes the actual photo. This is where the magic happens.    
    def _camera_take_photo():

        # First we initiate an interaction that doesn't display overlays and windows. We don't want them in our photo.
        # So we create a pausebehavior that pauses the game for 0.0 seconds and then continues. That's enough time to
        # take the photo. Then we start the interaction.

        ui.pausebehavior(0.0)
        ui.interact(suppress_overlay=True, suppress_window=True)

        # Now we take a screenshot, and get the screenshots image data from the corresponding variable.

        renpy.take_screenshot((1280,720))
        photo = renpy.game.interface.get_screenshot()

        # Now we create the filename. In this case, we use the MD5 hash of the image. This means that each image will
        # have a unique name and that no image can exist twice. This saves disk space if you take the same photo twice
        # by accident. It will overwrite the first one.

        photoname = datetime.now().strftime("%Y%m%d-%H%M%S")

        # We now define the directory we want to save the file to. I chose /game/pho/, but it's up to you.
        if renpy.android:
            photodir = os.environ['ANDROID_PUBLIC'] + "/game/photos/"
        else:
            photodir = config.basedir + "/game/photos/"

        # We create it if it doesn't exist. Somebody might have deleted it by accident and that would probably cause
        # the game to crash. We don't want that.

        if(os.path.isdir(photodir) == False):
            os.mkdir(photodir)

        # Now we open the file. This will automatically create it if it doesn't exist already. Then we write the image
        # data into the file and close it again.

        f = open(photodir + photoname + ".png","wb")
        f.write(photo)
        f.close()

        # Now we just return the name and we're done here.

        return photoname


    def camera_save_photo():

        # First we call the actual photo taking function and save the return value in newPhoto

        newPhoto = renpy.invoke_in_new_context(_camera_save_photo)

        # The saved photo name is now added to photos. Photos is a list that keeps track of the photos
        # we have already taken. Since the photoname is also the filename, use this name to load the
        # photos.

        persistent.photos.append(newPhoto)

        # Now we return to the parent function. In this case it's the one responsible for building the camera
        # UI, but it might be different in your case. You might not need this at all.

        ###### return "photo_taken"
    
    # This function is called by the one above and takes the actual photo. This is where the magic happens.    
    def _camera_save_photo():

        # First we initiate an interaction that doesn't display overlays and windows. We don't want them in our photo.
        # So we create a pausebehavior that pauses the game for 0.0 seconds and then continues. That's enough time to
        # take the photo. Then we start the interaction.
        # Now we take a screenshot, and get the screenshots image data from the corresponding variable.
        renpy.take_screenshot((1280,720))
        photo = renpy.game.interface.get_screenshot()

        # Now we create the filename. In this case, we use the MD5 hash of the image. This means that each image will
        # have a unique name and that no image can exist twice. This saves disk space if you take the same photo twice
        # by accident. It will overwrite the first one.

        photoname = datetime.now().strftime("%Y%m%d-%H%M%S")

        # We now define the directory we want to save the file to. I chose /game/pho/, but it's up to you.
        if renpy.android:
            photodir = os.environ['ANDROID_PUBLIC'] + "/game/photos/"
        else:
            photodir = config.basedir + "/game/photos/"

        # We create it if it doesn't exist. Somebody might have deleted it by accident and that would probably cause
        # the game to crash. We don't want that.

        if(os.path.isdir(photodir) == False):
            os.mkdir(photodir)

        # Now we open the file. This will automatically create it if it doesn't exist already. Then we write the image
        # data into the file and close it again.

        f = open(photodir + photoname + ".png","wb")
        f.write(photo)
        f.close()

        # Now we just return the name and we're done here.

        return photoname



screen phone_camera(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5):
    key "K_ESCAPE" action [PhoneReturn(), Function(ost_controls.get_music_pos)]
    frame style "empty" modal True:
        at transform:
            subpixel True zoom 1.0
            xpos xpos xanchor xanchor
            ypos ypos yanchor yanchor
        
        background Transform(
            phone.config.basedir + "camera.png",
            subpixel=True,
            align=(0.5, 0.5),
        )
    imagebutton:
        xpos 0.7642
        ypos 0.43
        hover phone.config.basedir + "camerabuttonhover.png"
        idle phone.config.basedir + "camerabutton.png"
        action Function(camera_take_photo)
    button:
        xsize 35
        ysize 35
        idle_background RoundedFrame("#ff0000", radius=(20, 20, 20, 20))
        hover_background RoundedFrame("#ff7c7c", radius=(20, 20, 20, 20))
        text _("X"):
            style "camerax_button_text"
            xalign 0.5
        ypos 0.158
        xpos 0.14
        action [PhoneReturn(), Function(ost_controls.get_music_pos)]
    imagebutton:
        xpos 0.786
        ypos 0.28
        idle phone.config.basedir + "switch.png"
        at transform:
            zoom 1.2
        action NullAction()
    $ getphotolist()
    if photolist != []:
        $ getphotolistsingle()
        for i in photolist:
            $ photoname = str(i)
            $ photoimg = ("photos/" + photoname)
        imagebutton:
            at transform:
                crop (280, 0, 720, 720)
                zoom 0.1
            xpos 0.775
            ypos 0.69
            idle photoimg
            action PhoneMenu("photos_gallery2")
    imagebutton:
        at transform:
            zoom 1.0
        action [PhoneReturn(), SetVariable("pressedhome", True)]
        idle phone.config.basedir + "phonehome.png"
        hover phone.config.basedir + "phonehomehover.png"
        xpos 0.861
        ypos 0.417
    if pressedhome:
        timer 0.0001 action PhoneReturn()
style camerax is empty

style camerax_button_text:
    outlines [ ]
    color "#ffffff" size 30
    font phone.config.basedir + "Aller_Rg.ttf"

default photolist = []

init python:
    import os, fnmatch

    def getphotolist():
        global photolist
        if renpy.android:
            list = fnmatch.filter(os.listdir(os.environ['ANDROID_PUBLIC'] + "/game/photos/"), "*.png")
        else:
            list = fnmatch.filter(os.listdir(config.basedir + "/game/photos/"), "*.png")
        photolist = list

    def getphotolistsingle():
        global photolist
        for i in photolist:
            return (i)