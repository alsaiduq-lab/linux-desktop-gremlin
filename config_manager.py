
import os
import settings


def load_master_config():
    """ Loads the main config.txt file. """
    path = os.path.join(settings.BASE_DIR, "config.txt")
    if not os.path.exists(path):
        print(f"Warning: Master config file not found at {path}")
        return

    s = settings.Settings
    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not line or '=' not in line:
                continue

            parts = line.split('=', 1)
            if len(parts) != 2:
                continue

            key = parts[0].strip().upper()
            value = parts[1].strip()

            try:
                match key:
                    case "START_CHAR":
                        s.StartingChar = value
                    case "SPRITE_SPEED":
                        s.FrameRate = int(value)
                    case "FOLLOW_RADIUS":
                        s.FollowRadius = float(value)
                    case "SPRITE_COLUMN":
                        s.SpriteColumn = int(value)
                    case "FRAME_HEIGHT":
                        s.FrameHeight = int(value)
                    case "FRAME_WIDTH":
                        s.FrameWidth = int(value)
                    case _:
                        pass
            except ValueError:
                print(
                    f"Warning: Could not parse key '{key}' with value '{value}'")


def load_config_char():
    """ Loads the character-specific config.txt file. """
    path = os.path.join(
        settings.BASE_DIR,
        "SpriteSheet", "Gremlins", settings.Settings.StartingChar, "config.txt"
    )
    if not os.path.exists(path):
        print(f"Warning: Character config file not found at {path}")
        return

    f = settings.FrameCounts
    with open(path, 'r') as f_char:
        for line in f_char.readlines():
            line = line.strip()
            if not line or '=' not in line:
                continue

            parts = line.split('=', 1)
            if len(parts) != 2:
                continue

            key = parts[0].strip().upper()
            value = parts[1].strip()

            try:
                val_int = int(value)
                match key:
                    case "FRAME_RATE":
                        settings.Settings.FrameRate = val_int
                    case "INTRO_FRAME_COUNT":
                        f.Intro = val_int
                    case "IDLE_FRAME_COUNT":
                        f.Idle = val_int
                    case "UP_FRAME_COUNT":
                        f.Up = val_int
                    case "DOWN_FRAME_COUNT":
                        f.Down = val_int
                    case "LEFT_FRAME_COUNT":
                        f.Left = val_int
                    case "RIGHT_FRAME_COUNT":
                        f.Right = val_int
                    case "OUTRO_FRAME_COUNT":
                        f.Outro = val_int
                    case "GRAB_FRAME_COUNT":
                        f.Grab = val_int
                    case "WALK_IDLE_FRAME_COUNT":
                        f.WalkIdle = val_int
                    case "CLICK_FRAME_COUNT":
                        f.Click = val_int
                    case "HOVER_FRAME_COUNT":
                        f.Hover = val_int
                    case "SLEEP_FRAME_COUNT":
                        f.Sleep = val_int
                    case "FIRE_L_COUNT":
                        f.LeftFire = val_int
                    case "FIRE_R_COUNT":
                        f.RightFire = val_int
                    case "RELOAD_COUNT":
                        f.Reload = val_int
                    case "PAT_COUNT":
                        f.Pat = val_int
                    case _:
                        pass
            except ValueError:
                print(
                    f"Warning: Could not parse key '{key}' with value '{value}'")
