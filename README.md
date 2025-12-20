# WARNING
I sadly am no longer maintaining these as much as my SWAY config files.


# dotfiles
My dotfiles for i3 **anyone** can use or modify.

It has:

- A good color scheme
- Built in keybinds
- Picom config with rounded corners
- i3blocks config


# Dependencies

Debian required: `sudo apt install i3 i3blocks rofi`

Debian optionals `sudo apt install picom cava btop`


# Display Managers

I recommend using [ly](https://codeberg.org/fairyglade/ly) as a display manager.

## Installation 

### Arch Linux
On arch linux you can easily install ly with: `sudo pacman -S ly`

### Debian
On debian however it is very very painful to install ly.
First install brew: `sudo apt install brew`
Second install with brew zig: `brew install zig`
Finally compile and install ly with [these instructions](https://codeberg.org/fairyglade/ly).
