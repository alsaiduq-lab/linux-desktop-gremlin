
# 4. Run Desktop Gremlins!

Once installed, you can find **Gremlin Picker** in your application menu (or app launcher like Rofi/Wofi/Fuzzel). Just search for "Gremlin" and launch it!

![App Launcher](images/ss-app_launcher.png)

Alternatively, you can run the picker from the terminal:

```sh
./scripts/gremlin-picker.sh
```

Otherwise, you can navigate to `~/.config/linux-desktop-gremlin/` and execute the run script directly:

```sh
./run.sh                    # to spawn the default character (specified in ./config.json)
./run.sh <character-name>   # to spawn any character who is available in ./spritesheet/

# You can now close the terminal which you executed these scripts with.
# The gremlin won't be despawned unless you use your hotkeys for closing window,
# like alt+f4 or mod+q.
```

