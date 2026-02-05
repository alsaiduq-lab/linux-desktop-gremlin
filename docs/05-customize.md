
# 5. 🔧 Customizations!

https://github.com/user-attachments/assets/26e2a3b0-4fde-4a3a-926f-ad9f1e1cfb07

## How to Make Your Gremlin Annoy You (Occasionally!)

Do you want the gremlins to annoy you at random time or not? 😜

To control this, open `./spritesheet/<character>/emote-config.json`. You'll see:

```json
{
    "AnnoyEmote": true,
    "MinEmoteTriggerMinutes": 5,
    "MaxEmoteTriggerMinutes": 15,
    "EmoteDuration": 3600
}
```

If you set `AnnoyEmote` to `false`, then nothing happens. If you set it to `true`, however:
- If the gremlin goes without any *"caring interactions"* (no pats, no drags, no clicks,...) they will get bored 😢.
- If you leave them bored for a while (a random time between `MinEmoteTriggerMinutes` and `MaxEmoteTriggerMinutes`), they will suddenly play a special emote (with sound!) all by themselves 😙😙.
- The emote will last for the number of milliseconds set in `EmoteDuration`.
  - *(Note: For now, this duration only affects the animation, not the sound effect, sorry 😢.)*

You can also trigger this animation by hovering over the gremlin and press "P". You can customize this key too, just take a look at `./config.json`.

## How to Enable or Disable the System Tray

This program's systray is disabled by default, and you won't lose any functionality by disabling the systray either. However, if you need it, you might enable it by modifying the `Systray` field in `./config.json` to `true`.

