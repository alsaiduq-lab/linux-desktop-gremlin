
import os
import settings
from PySide6.QtGui import QPixmap

CACHE = {}

SPRITE_MAP = {
    "idle": "idle.png",
    "intro": "intro.png",
    "left": "left.png",
    "right": "right.png",
    "forward": "forward.png",
    "backward": "backward.png",
    "outro": "outro.png",
    "grab": "grab.png",
    "widle": "wIdle.png",
    "click": "click.png",
    "hover": "hover.png",
    "sleep": "sleep.png",
    "firel": "fireL.png",
    "firer": "fireR.png",
    "reload": "reload.png",
    "pat": "pat.png",
}


def get(animation_name: str):
    """ Gets a QPixmap from the cache or loads it from disk. """
    animation_name = animation_name.lower()

    if animation_name in CACHE:
        return CACHE[animation_name]

    file_name = SPRITE_MAP.get(animation_name)
    if not file_name:
        print(f"Error: Unknown animation name '{animation_name}'")
        return None

    sheet = load_sprite(settings.Settings.StartingChar, file_name)
    if sheet:
        CACHE[animation_name] = sheet
    return sheet


def load_sprite(file_folder, file_name, root_folder="Gremlins"):
    """ Loads a sprite from disk into a QPixmap. """
    path = os.path.join(
        settings.BASE_DIR,
        "SpriteSheet", root_folder, file_folder, file_name
    )
    if not os.path.exists(path):
        print(f"Warning: Sprite file not found at {path}")
        return None

    try:
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print(f"Error: Failed to load pixmap from {path}")
            return None
        return pixmap
    except Exception as e:
        print(f"Error loading sprite {path}: {e}")
        return None


def clear_cache():
    CACHE.clear()
