#!/bin/bash
# Run this script with INCLUDES_GIT=1 in order to install the entire git history

# ========================================================================================
# Clone the repo into ~/.config
# ========================================================================================
FLAG=""
if [[ -z "${INCLUDES_GIT}" ]]; then
    FLAG="--depth 1"
fi

echo "Cloning repo into ~/.config/linux-desktop-gremlin..."
git clone $FLAG https://github.com/iluvgirlswithglasses/linux-desktop-gremlin ~/.config/linux-desktop-gremlin
cd ~/.config/linux-desktop-gremlin


# ========================================================================================
# Install uv and sync
# ========================================================================================
export PATH=$PATH:$HOME/.local/bin
if command -v uv >/dev/null 2>&1; then
    echo "Found uv package manager..."
else
    echo "uv is not installed, installing..."
    echo "Executing: curl -LsSf https://astral.sh/uv/install.sh | sh"
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

uv sync


# ========================================================================================
# Installation Variables
# ========================================================================================
INSTALL_PATH="$HOME/.config/linux-desktop-gremlin"
BIN_PATH="$HOME/.local/bin"
ICON_PATH="$INSTALL_PATH/icon.png"

PICKER_LINK_PATH="$BIN_PATH/gremlin-picker"
PICKER_DESKTOP_FILE="$HOME/.local/share/applications/gremlin_picker.desktop"

DOWNLOADER_LINK_PATH="$BIN_PATH/gremlin-downloader"
DOWNLOADER_DESKTOP_FILE="$HOME/.local/share/applications/gremlin_downloader.desktop"


# ========================================================================================
# Install Gremlin Picker
# ========================================================================================
echo "→ Installing Linux Desktop Gremlin..."
mkdir -p "$INSTALL_PATH" "$BIN_PATH" "$(dirname "$PICKER_DESKTOP_FILE")"
ln -sf "$INSTALL_PATH/scripts/gremlin-picker.sh" "$PICKER_LINK_PATH"
chmod +x "$PICKER_LINK_PATH"

cat >"$PICKER_DESKTOP_FILE" <<EOF
[Desktop Entry]
Name=Gremlin Picker
Comment=Pick your favorite gremlin
Exec=$PICKER_LINK_PATH
Icon=$ICON_PATH
Terminal=false
Type=Application
Categories=Utility;
EOF

chmod 644 "$PICKER_DESKTOP_FILE"


# ========================================================================================
# Install Gremlin Downloader
# ========================================================================================
echo "→ Installing Gremlin Downloader..."
mkdir -p "$(dirname "$DOWNLOADER_DESKTOP_FILE")"
ln -sf "$INSTALL_PATH/scripts/gremlin-downloader.sh" "$DOWNLOADER_LINK_PATH"
chmod +x "$DOWNLOADER_LINK_PATH"

cat >"$DOWNLOADER_DESKTOP_FILE" <<EOF
[Desktop Entry]
Name=Gremlin Downloader
Comment=Download some gremlins
Exec=$DOWNLOADER_LINK_PATH
Icon=$ICON_PATH
Terminal=false
Type=Application
Categories=Utility;
EOF

chmod 644 "$DOWNLOADER_DESKTOP_FILE"

echo "Installed successfully! :3"
