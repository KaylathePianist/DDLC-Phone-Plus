DDLC Phone+ by CalebthePianist (Original Phone by Elckarow)

Current Version: 1.1
Better EMR Phone Equivalent Version: 3.2.2

This tool is an alternate version of Elckarow's "Better EMR Phone", meant to include extra screens and features that you might want to use in your mod.
If you don't need these extra features, download the original phone.
If you have any questions about the NEW features of the phone, message CalebthePianist on Discord.
If you have any questions about the ORIGINAL phone, you can message Elckarow on Discord as well.
To see a script that shows you most of the features automatically, call phone_discussion_test in your script.

New Features:
- Stickers (images that can't be enlargened in a discussion, show them with *sticker "mc" "n1"* or similar)
- Pre-defined emojis, including DDLC emotes
- Port of the DDLC Music Player to the phone
- Phone versions of the save, load, settings, achievements, gallery, about, and history screens
- A calculator app, in case you'd ever need that
- A camera app that takes photos and saves them to your device, as well as a screen to view the images
- An alternate quick menu that allows constant and easy access to the base phone screen
- A home button on the phone that takes you back to the base screen

If you use this in your project, credit Elckarow and CalebthePianist.

INSTALL INSTRUCTIONS:
- Put both .rpy files and the entire "Phone" folder inside your "mod_assets" folder.

REQUIRED CHANGES IN YOUR MOD:
- In screens.rpy, change the name of "screen confirm()" to "screen confirm_orig()"
- Also in screens.rpy, find the statement "use quick_menu" in "screen say(who, what)", and replace it with "use quick_menu_phone".
- Go to splash.rpy and find the label splashscreen. Add "$ in_splash = True" to the beginning and "$ in_splash = False" to the ending (right before the "return" function). 
- Go to the label after_load in splash.rpy and add the following lines:
    $ persistent.musicstarted = False
    $ ost_controls.pause_music()

That's it! Everything should work as intended. (I hope)

CREDITS:
Better EMR Phone © 2022-2024 Elckarow.
Phone+ Addon Copyright © 2023-2024 CalebthePianist.
Code adapted from the DDLC Mod Template 2.0 and DDLC Music Player (© 2019-2024 Bronya-Rand), Ren'Py Color Picker by Feniks, and screenshot code by bink on the Ren'Py Forums.
Twemoji designs are licensed under CC-BY 4.0.
Chibi stickers were created by Team Salvato and edited by Leomonade.
Special thanks to M3rc, Keita, and Elckarow for assistance and help.

Official Better EMR Phone Documentation: https://better-emr-phone.readthedocs.io/en/latest

Original download link: https://github.com/Elckarow/Better-EMR-Phone
