init -150 python in phone.emojis:
    from renpy.store import store, Transform, phone, config as renpy_config
    from store.phone import config
    import os
    _constant = True

    import string
    _NOT_ALLOWED_CHARACTERS = set(string.punctuation.strip("_") + " ")

    _emojis = { }

    def add(name, emoji):
        global _NOT_ALLOWED_CHARACTERS
        if set(name) & _NOT_ALLOWED_CHARACTERS:
            raise Exception("not a valid emoji name: {}".format(name))
        
        global _emojis
        _emojis[name] = renpy.displayable(emoji)
        
    def get(name):
        return _emojis[name]
    
    renpy_config.self_closing_custom_text_tags["emoji"] = \
        lambda tag, name: [
            (renpy.TEXT_DISPLAYABLE, Transform(get(name), subpixel=True, ysize=1.0, fit="contain"))
        ]

    import re
    _tag_pattern = re.compile(r"\{emoji\=([a-zA-Z0-9_]*)\}")

    def format_emoji_tag(s):
        for emoji in _tag_pattern.findall(s): s = _tag_pattern.sub(":" + emoji + ":", s, 1)
        return s

init 1000 python hide in phone.emojis:
    if config.auto_emojis:
        emoji_base_path = phone.asset("emojis")

        try:
            for emoji in os.listdir(phone.path_join(renpy_config.basedir, "game", emoji_base_path)):
                path = phone.path_join(emoji_base_path, emoji)

                if os.path.isdir(phone.path_join(renpy_config.basedir, path)):
                    continue

                name, extension = os.path.splitext(emoji)
                
                if extension.lower() not in renpy_config.image_extensions:
                    continue

                add(name, path)

        except OSError:
            pass

# prevent `default`
python early in phone.emojis:
    pass

python early:
    config.special_namespaces["store.phone.emojis"] = type(config.special_namespaces["store.config"])(phone.emojis, "phone.emojis")