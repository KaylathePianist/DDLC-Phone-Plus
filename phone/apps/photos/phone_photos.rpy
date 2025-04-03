screen photos_gallery():
    use _phone():
        style_prefix "phone_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Photos") xalign 0.5 text_align 0.5
            viewport:
                draggable True
                mousewheel True
                yfill True
                frame:
                    vbox:
                        null height 34
                        button:
                            action PhoneMenu("photos_gallery2")
                            hbox:
                                xfill True
                                text _("Camera Roll") xalign 0.0 yalign 0.5
                                text _(">") xalign 1.0 yalign 0.5
                        null height 10
                        button:
                            action PhoneMenu("photos_gallery3")
                            hbox:
                                xfill True
                                text _("Special Gallery") xalign 0.0 yalign 0.5
                                text _(">") xalign 1.0 yalign 0.5
                        null height 10

screen photos_gallery2():
    use _phone():
        style_prefix "phone_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Camera Roll") xalign 0.5 text_align 0.5
            viewport:
                yfill True
                frame:
                    vpgrid:
                        id "pg2"
                        draggable True
                        mousewheel True
                        cols 2
                        spacing 6
                        xalign 0.5
                        $ getphotolist()
                        for i in photolist:
                            $ photoname = str(i)
                            $ photoimg = ("photos/" + photoname)
                            imagebutton:
                                at transform:
                                    zoom 0.13
                                action Show("_phone_gallery_image", dissolve, img=photoimg)
                                idle photoimg
                    vbar value YScrollValue("pg2") xalign 1.99 ysize 560




screen photos_gallery3():
    use _phone():
        style_prefix "phone_settings"
        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Special Gallery") xalign 0.5 text_align 0.5
            viewport:
                yfill True
                frame:
                    vpgrid:
                        id "pg3"
                        cols 2
                        spacing 6
                        mousewheel True
                        draggable True
                        xalign 0.5
                        for name, gl in galleryList.items():
                            if gl.unlocked:
                                imagebutton: 
                                    idle gl.image
                                    at transform:
                                        zoom 0.13
                                    action Show("_phone_gallery_image", dissolve, img=gl.image)

                            else:
                                imagebutton: 
                                    idle "mod_assets/phone/assets/galleryLock.png"
                                    at transform:
                                        zoom 0.13
                                    action Show("phone_dialogue", message="This image is locked. Continue playing [config.name] to unlock this image.", ok_action=Hide("phone_dialogue"))


                    vbar value YScrollValue("pg3") xalign 1.99 ysize 560


screen _phone_gallery_image(img):
    style_prefix "phone_images"
    modal True
    add Solid("#000")

    add img:
        align (0.5, 0.5)
    
    textbutton _("Return"):
        align (0.1, 0.9)
        action Hide("_phone_gallery_image", dissolve)
    key "K_ESCAPE" action Hide("_phone_gallery_image", dissolve)

