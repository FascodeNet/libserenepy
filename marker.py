###                 GNU LESSER GENERAL PUBLIC LICENSE
###                       Version 3, 29 June 2007
### Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
### Everyone is permitted to copy and distribute verbatim copies
### of this license document, but changing it is not allowed.

class colors: # Colors
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    light_gray = '\033[37m'
    darkgray = '\033[90m'
    light_red = '\033[91m'
    light_green = '\033[92m'
    light_yellow = '\033[93m'
    light_blue = '\033[94m'
    light_magenta = '\033[95m'
    light_cyan = '\033[96m'
    reset = '\033[0m'

class style: # Style
    bold = '\033[1m'
    underlined = '\033[4m'
    reset = '\033[0m'

class backgroundcolors: # Backgroundcolors
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    reset = '\033[0m'


if __name__ == '__main__':
    print(colors.black + "Black text" + colors.reset)
    print(colors.red + "Red text" + colors.reset)
    print(colors.blue + "Blue text" + colors.reset)
    print(colors.cyan + "Cyan text" + colors.reset)
    print(colors.darkgray + "Darkgray text" + colors.reset)
    print(colors.green + "green text" + colors.reset)
    print(colors.light_blue + "Light Blue text" + colors.reset)
    print(colors.light_cyan + "Light cyan text" + colors.reset)
    print(colors.light_gray + "Light gray text" + colors.reset)
    print(colors.light_green + "Light green text" + colors.reset)
    print(colors.light_magenta + "Light magenta text" + colors.reset)
    print(colors.light_red + "Light red text" + colors.reset)
    print(colors.light_yellow + "Light yellow text" + colors.reset)
    print(style.bold + "Bold text" + style.reset)
    print(style.underlined + "Underlined text" + style.reset)
    print(backgroundcolors.black + "Black Background" + backgroundcolors.reset)
    print(backgroundcolors.blue + "Blue Background" + backgroundcolors.reset)
    print(backgroundcolors.red + "Red Background" + backgroundcolors.reset)
    print(backgroundcolors.cyan + "Cyan Background" + backgroundcolors.reset)
    print(backgroundcolors.green + "Green Background" + backgroundcolors.reset)
    print(backgroundcolors.magenta + "Megenta Background" + backgroundcolors.reset)
    print(colors.darkgray + backgroundcolors.yellow + "Yellow Background" + backgroundcolors.reset)

