
# 2. Install Linux Desktop Gremlins

## Automatic installation (Linux only)

Just run the following script, and it will take care of the rest:

```sh
# this will install to ~/.config/linux-desktop-gremlin/
curl -s https://raw.githubusercontent.com/iluvgirlswithglasses/linux-desktop-gremlin/refs/heads/main/install.sh | bash
```

It is recommended that you check the content of the script before running.

## Automatic installation, with full git history (Linux only)

If you wish to install this repository with full git history (this will add ~200MB), please run the following script:

```sh
# this will install to ~/.config/linux-desktop-gremlin/
curl -s https://raw.githubusercontent.com/iluvgirlswithglasses/linux-desktop-gremlin/refs/heads/main/install.sh | INCLUDES_GIT=1 bash
```

## Manual installation

You can install dependencies either in a Python virtual environment or using your system's package manager.

<details>
  <summary>Method A: Virtual Environment (Recommended)</summary>

  There's nothing that can go wrong about this, except for the disk space. This also works on Windows and MacOS.

  ```sh
  # clone repository
  git clone https://github.com/iluvgirlswithglasses/linux-desktop-gremlin
  cd linux-desktop-gremlin

  # install uv -- a fast Python package manager -- then sync packages
  curl -LsSf https://astral.sh/uv/install.sh | sh
  uv sync
  ```
</details>

<details>
  <summary>Method B: System Package Manager</summary>

  This method uses your distribution's packages to save disk space. You will need PySide6 and its Qt6 dependencies.

  ```sh
  # Example for Arch Linux
  yay -S pyside6 qt6-base
  ```
</details>

