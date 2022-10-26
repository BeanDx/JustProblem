from cgi import print_arguments
import os
import sys
import colorama
from colorama import init
from colorama import Fore, Back, Style
import time
from time import sleep
from ast import While
import webbrowser as wb
init(autoreset=True)


def eng():
        print(
                Fore.RED
                + Style.NORMAL
                + "Note: If you want to see an ASCII image of your OS, then enter one of the outputs below:"
        )
        print("")
        print(Fore.GREEN + Style.BRIGHT + "ArchLinux")
        print(Fore.GREEN + Style.BRIGHT + "GarudaLinux")
        print(Fore.GREEN + Style.BRIGHT + "FreeBSD")
        print(Fore.GREEN + Style.BRIGHT + "GentooLinux")
        print(Fore.GREEN + Style.BRIGHT + "GuixLinux")
        print(Fore.GREEN + Style.BRIGHT + "HaikuOS")
        print(Fore.GREEN + Style.BRIGHT + "MacOS")
        print(Fore.GREEN + Style.BRIGHT + "ManjaroLinux")
        print(Fore.GREEN + Style.BRIGHT + "OpenWrt")
        print(Fore.GREEN + Style.BRIGHT + "PureOS")
        print(Fore.GREEN + Style.BRIGHT + "UbuntuLinux")
        print("")

        os_eng = input(Fore.YELLOW + Style.BRIGHT + "Enter your OS: ")
        them_eng = input(Fore.YELLOW + Style.BRIGHT + "Enter the topic of the problem: ")
        probl_eng = input(Fore.YELLOW + Style.BRIGHT + "Describe the problem: ")

        if os.sys.platform == "win32":
                os.system("cls")
        else:
                os.system("clear")

        if os_eng == "ArchLinux":
                print(Fore.BLUE + "      /\\      ") # ArchLinux
                print(Fore.BLUE + "     /  \\     ") # ArchLinux
                print(Fore.BLUE + "    / /\\ \\    ") # ArchLinux
                print(Fore.BLUE + "   / /  \\ \\   ") # ArchLinux
                print(Fore.BLUE + "  / /    \\ \\  ") # ArchLinux
                print(Fore.BLUE + " / / _____\\ \\ ") # ArchLinux
                print(Fore.BLUE + "/_/  \`----.\\_\\") # ArchLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        elif os_eng == "GarudaLinux":
                print(Fore.MAGENTA + "         _______         ") # GarudaLinux
                print(Fore.MAGENTA + "      __/       ""_      ") # GarudaLinux
                print(Fore.MAGENTA + "    _/     /      ""_    ") # GarudaLinux
                print(Fore.MAGENTA + "  _/      /_________""  ") # GarudaLinux
                print(Fore.MAGENTA + "_/                  |") # GarudaLinux
                print(Fore.MAGENTA + "\\     ____________") # GarudaLinux
                print(Fore.MAGENTA + " \\_            __/ ") # GarudaLinux
                print(Fore.MAGENTA + "   \\__________/   ") # GarudaLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

        if os_eng == "FreeBSD":
                print(Fore.RED + "/\\,-'''''-,/\\") # FreeBSD
                print(Fore.RED + "\\_)       (_/") # FreeBSD
                print(Fore.RED + "|    .  .   |") # FreeBSD
                print(Fore.RED + "|           |") # FreeBSD
                print(Fore.RED + " ;    __   ;") # FreeBSD
                print(Fore.RED + "  '-_____-'") # FreeBSD

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

        elif os_eng == "GentooLinux":
                print(Fore.WHITE + " _-----_ ") # GentooLinux
                print(Fore.WHITE + "(       \\") # GentooLinux
                print(Fore.WHITE + "\\    0   \\") # GentooLinux
                print(Fore.WHITE + " \\        )") # GentooLinux
                print(Fore.WHITE + " /      _/") # GentooLinux
                print(Fore.WHITE + "(     _-") # GentooLinux
                print(Fore.WHITE + "\\____-") # GentooLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        if os_eng == "GuixLinux":
                print(Fore.YELLOW + "|.__          __.|")  # GuixLinux
                print(Fore.YELLOW + "|__ \\        / __|") # GuixLinux
                print(Fore.YELLOW + "   \\ \\      / /") # GuixLinux
                print(Fore.YELLOW + "     \\ \\    / /") # GuixLinux
                print(Fore.YELLOW + "      \\ \\  / /") # GuixLinux
                print(Fore.YELLOW + "       \\ \\/ /") # GuixLinux
                print(Fore.YELLOW + "         \\__/") # GuixLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        elif os_eng == "HaikuOS":
                print(Fore.GREEN + "       ,^,       ")  # HaikuOS
                print(Fore.GREEN + "     /   \\     ") # HaikuOS
                print(Fore.GREEN + "*--_ ;     ; _--*") # HaikuOS
                print(Fore.GREEN + "\\   '"     "'   /") # HaikuOS
                print(Fore.GREEN + "'.           .'") # HaikuOS
                print(Fore.GREEN + ".-'"         "'-.") # HaikuOS
                print(Fore.GREEN + "'-.__.   .__.-'") # HaikuOS
                print(Fore.GREEN + "       |_|     ") # HaikuOS

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        if os_eng == "GLUnix":
                print(Fore.YELLOW + "       |       ") # GLUnix
                print(Fore.YELLOW + "       |          |") # GLUnix
                print(Fore.YELLOW + "                  |") # GLUnix
                print(Fore.YELLOW + "  |    ________  ") # GLUnix
                print(Fore.YELLOW + "  |  /\\   |    \\  ") # GLUnix
                print(Fore.YELLOW + "    /  \\  |     \\  |    ") # GLUnix
                print(Fore.YELLOW + "   /    \\        \\ |") # GLUnix
                print(Fore.YELLOW + "  /      \\________\\") # GLUnix
                print(Fore.YELLOW + "  \\      /        /") # GLUnix
                print(Fore.YELLOW + "   \\    /        /") # GLUnix
                print(Fore.YELLOW + "    \\  /        /") # GLUnix
                print(Fore.YELLOW + "     \\/________/") # GLUnix

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        elif os_eng == "MacOS":
                print(Fore.GREEN + "       .:'       ") # MacOS
                print(Fore.GREEN + "    _ :'_    ") # MacOS
                print(Fore.GREEN + " .'\`_\`-'_\`\`.") # MacOS
                print(Fore.GREEN + ":________.-'") # MacOS
                print(Fore.GREEN + ":_______:") # MacOS
                print(Fore.GREEN + " :_______\`-;") # MacOS
                print(Fore.GREEN + "  \`._.-._.'") # MacOS

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        if os_eng == "ManjaroLinux":
                print(Fore.GREEN + "||||||||| ||||") # ManjaroLinux
                print(Fore.GREEN + "||||||||| ||||") # ManjaroLinux
                print(Fore.GREEN + "||||      ||||") # ManjaroLinux
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux   
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

        elif os_eng == "OpenWrt":
                print(Fore.GREEN + "_______") # OpenWrt
                print(Fore.GREEN + "|       |.-----.-----.-----.") # OpenWrt
                print(Fore.GREEN + "|   -   ||  _  |  -__|     |") # OpenWrt
                print(Fore.GREEN + "|_______||   __|_____|__|__|") # OpenWrt
                print(Fore.GREEN + " ________|__|    __") # OpenWrt
                print(Fore.GREEN + "|  |  |  |.----.|  |_") # OpenWrt
                print(Fore.GREEN + "|  |  |  ||   _||   _|") # OpenWrt
                print(Fore.GREEN + "|________||__|  |____|") # OpenWrt

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        if os_eng == "PureOS":
                print(Fore.YELLOW + " _____________") # PureOS
                print(Fore.YELLOW + "|  _________  |") # PureOS
                print(Fore.YELLOW + "| |  .   .  | |") # PureOS
                print(Fore.YELLOW + "| |    _    | |") # PureOS
                print(Fore.YELLOW + "| |_________| |") # PureOS
                print(Fore.YELLOW + "|_____________|") # PureOS

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        elif os_eng == "UbuntuLinux":
                print(Fore.YELLOW + "         _    ") # UbuntuLinux
                print(Fore.YELLOW + "     ---(_)") # UbuntuLinux
                print(Fore.YELLOW + " _/  ---  \\") # UbuntuLinux
                print(Fore.YELLOW + "(_) |   |") # UbuntuLinux
                print(Fore.YELLOW + " \\  --- _/") # UbuntuLinux
                print(Fore.YELLOW + " ---(_)") # UbuntuLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        
        else:
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Name of OS: " + Fore.BLUE + os_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Problem topic: " + Fore.BLUE + them_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Description of the problem: " + Fore.BLUE + probl_eng)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")


def rus():
    print(
        Fore.RED
        + Style.NORMAL
        + "Примечание: Если вы хотите увидеть ASCII изображение вашей ОС, то введите один из ниже выведенных:"
    )
    print("")
    print(Fore.GREEN + Style.BRIGHT + "ArchLinux")
    print(Fore.GREEN + Style.BRIGHT + "GarudaLinux")
    print(Fore.GREEN + Style.BRIGHT + "FreeBSD")
    print(Fore.GREEN + Style.BRIGHT + "GentooLinux")
    print(Fore.GREEN + Style.BRIGHT + "HaikuOS")
    print(Fore.GREEN + Style.BRIGHT + "HydroOS")
    print(Fore.GREEN + Style.BRIGHT + "GLUnix")
    print(Fore.GREEN + Style.BRIGHT + "MacOS")
    print(Fore.GREEN + Style.BRIGHT + "ManjaroLinux")
    print(Fore.GREEN + Style.BRIGHT + "OpenWrt")
    print(Fore.GREEN + Style.BRIGHT + "PureOS")
    print(Fore.GREEN + Style.BRIGHT + "UbuntuLinux")
    print("")

    os_rus = input(Fore.YELLOW + Style.BRIGHT + "Введите Вашу ОС (Пример: ArchLinux): ")
    them_rus = input("Введите тему проблемы: ")
    probl_rus = input("Опишите проблему: ")

    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    if os_rus == "ArchLinux":
                print(Fore.BLUE + "      /\\      ") # ArchLinux
                print(Fore.BLUE + "     /  \\     ") # ArchLinux
                print(Fore.BLUE + "    / /\\ \\    ") # ArchLinux
                print(Fore.BLUE + "   / /  \\ \\   ") # ArchLinux
                print(Fore.BLUE + "  / /    \\ \\  ") # ArchLinux
                print(Fore.BLUE + " / / _____\\ \\ ") # ArchLinux
                print(Fore.BLUE + "/_/  \`----.\\_\\") # ArchLinux


                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

    elif os_rus == "GarudaLinux":
                print(Fore.MAGENTA + "         _______         ") # GarudaLinux
                print(Fore.MAGENTA + "      __/       ""_      ") # GarudaLinux
                print(Fore.MAGENTA + "    _/     /      ""_    ") # GarudaLinux
                print(Fore.MAGENTA + "  _/      /_________""  ") # GarudaLinux
                print(Fore.MAGENTA + "_/                  |") # GarudaLinux
                print(Fore.MAGENTA + "\\     ____________") # GarudaLinux
                print(Fore.MAGENTA + " \\_            __/ ") # GarudaLinux
                print(Fore.MAGENTA + "   \\__________/   ") # GarudaLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

    if os_rus == "FreeBSD":
                print(Fore.RED + "/\\,-'''''-,/\\") # FreeBSD
                print(Fore.RED + "\\_)       (_/") # FreeBSD
                print(Fore.RED + "|    .  .   |") # FreeBSD
                print(Fore.RED + "|           |") # FreeBSD
                print(Fore.RED + " ;    __   ;") # FreeBSD
                print(Fore.RED + "  '-_____-'") # FreeBSD

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

    elif os_rus == "GentooLinux":
                print(Fore.WHITE + " _-----_ ") # GentooLinux
                print(Fore.WHITE + "(       \\") # GentooLinux
                print(Fore.WHITE + "\\    0   \\") # GentooLinux
                print(Fore.WHITE + " \\        )") # GentooLinux
                print(Fore.WHITE + " /      _/") # GentooLinux
                print(Fore.WHITE + "(     _-") # GentooLinux
                print(Fore.WHITE + "\\____-") # GentooLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
    
    if os_rus == "GuixLinux":
        print(Fore.YELLOW + "|.__          __.|")  # GuixLinux
        print(Fore.YELLOW + "|__ \\        / __|") # GuixLinux
        print(Fore.YELLOW + "   \\ \\      / /") # GuixLinux
        print(Fore.YELLOW + "     \\ \\    / /") # GuixLinux
        print(Fore.YELLOW + "      \\ \\  / /") # GuixLinux
        print(Fore.YELLOW + "       \\ \\/ /") # GuixLinux
        print(Fore.YELLOW + "         \\__/") # GuixLinux

        print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
        print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
        print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
        print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
        print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

    elif os_rus == "HaikuOS":
                print(Fore.GREEN + "       ,^,       ")  # HaikuOS
                print(Fore.GREEN + "     /   \\     ") # HaikuOS
                print(Fore.GREEN + "*--_ ;     ; _--*") # HaikuOS
                print(Fore.GREEN + "\\   '"     "'   /") # HaikuOS
                print(Fore.GREEN + "'.           .'") # HaikuOS
                print(Fore.GREEN + ".-'"         "'-.") # HaikuOS
                print(Fore.GREEN + "'-.__.   .__.-'") # HaikuOS
                print(Fore.GREEN + "       |_|     ") # HaikuOS

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
    
    if os_rus == "HydroOS":
                print(Fore.CYAN + "╔╗╔╗──╔╗───╔═╦══╗") # HydroOS
                print(Fore.CYAN + "║╚╝╠╦╦╝╠╦╦═╣║║══╣") # HydroOS
                print(Fore.CYAN + "║╔╗║║║╬║╔╣╬║║╠══║") # HydroOS
                print(Fore.CYAN + "╚╝╚╬╗╠═╩╝╚═╩═╩══╝") # HydroOS
                print(Fore.CYAN + "───╚═╝") # HydroOS

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
    
    elif os_rus == "GLUnix":
                print(Fore.YELLOW + "       |       ") # GLUnix
                print(Fore.YELLOW + "       |          |") # GLUnix
                print(Fore.YELLOW + "                  |") # GLUnix
                print(Fore.YELLOW + "  |    ________  ") # GLUnix
                print(Fore.YELLOW + "  |  /\\   |    \\  ") # GLUnix
                print(Fore.YELLOW + "    /  \\  |     \\  |    ") # GLUnix
                print(Fore.YELLOW + "   /    \\        \\ |") # GLUnix
                print(Fore.YELLOW + "  /      \\________\\") # GLUnix
                print(Fore.YELLOW + "  \\      /        /") # GLUnix
                print(Fore.YELLOW + "   \\    /        /") # GLUnix
                print(Fore.YELLOW + "    \\  /        /") # GLUnix
                print(Fore.YELLOW + "     \\/________/") # GLUnix

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
    
    if os_rus == "MacOS":
                print(Fore.GREEN + "       .:'       ") # MacOS
                print(Fore.GREEN + "    _ :'_    ") # MacOS
                print(Fore.GREEN + " .'\`_\`-'_\`\`.") # MacOS
                print(Fore.GREEN + ":________.-'") # MacOS
                print(Fore.GREEN + ":_______:") # MacOS
                print(Fore.GREEN + " :_______\`-;") # MacOS
                print(Fore.GREEN + "  \`._.-._.'") # MacOS

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
    
    elif os_rus == "ManjaroLinux":
                print(Fore.GREEN + "||||||||| ||||") # ManjaroLinux
                print(Fore.GREEN + "||||||||| ||||") # ManjaroLinux
                print(Fore.GREEN + "||||      ||||") # ManjaroLinux
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux   
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux
                print(Fore.GREEN + "|||| |||| ||||") # ManjaroLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

    if os_rus == "OpenWrt":
                print(Fore.GREEN + "_______") # OpenWrt
                print(Fore.GREEN + "|       |.-----.-----.-----.") # OpenWrt
                print(Fore.GREEN + "|   -   ||  _  |  -__|     |") # OpenWrt
                print(Fore.GREEN + "|_______||   __|_____|__|__|") # OpenWrt
                print(Fore.GREEN + " ________|__|    __") # OpenWrt
                print(Fore.GREEN + "|  |  |  |.----.|  |_") # OpenWrt
                print(Fore.GREEN + "|  |  |  ||   _||   _|") # OpenWrt
                print(Fore.GREEN + "|________||__|  |____|") # OpenWrt

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
    
    elif os_rus == "PureOS":
                print(Fore.YELLOW + " _____________") # PureOS
                print(Fore.YELLOW + "|  _________  |") # PureOS
                print(Fore.YELLOW + "| |  .   .  | |") # PureOS
                print(Fore.YELLOW + "| |    _    | |") # PureOS
                print(Fore.YELLOW + "| |_________| |") # PureOS
                print(Fore.YELLOW + "|_____________|") # PureOS

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")

    if os_rus == "UbuntuLinux":
                print(Fore.YELLOW + "         _    ") # UbuntuLinux
                print(Fore.YELLOW + "     ---(_)") # UbuntuLinux
                print(Fore.YELLOW + " _/  ---  \\") # UbuntuLinux
                print(Fore.YELLOW + "(_) |   |") # UbuntuLinux
                print(Fore.YELLOW + " \\  --- _/") # UbuntuLinux
                print(Fore.YELLOW + " ---(_)") # UbuntuLinux

                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
    
    else:
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Имя ОС: " + Fore.BLUE + os_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✓ Тема проблемы: " + Fore.BLUE + them_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")
                print(Fore.RED + " ~> ✘ Описание проблемы: " + Fore.BLUE + probl_rus)
                print(Fore.GREEN + "▽ ━━━━━━━━━ ▽ ━━━━━━━━━━ ▽ ━━━━━━━━━━ ▽")


def main():
        # wb.open("https://t.me/JustProblems")
        print(
        Fore.GREEN
        + "====░=====░=====░==░=░======░=░=====░=====░==░=====░=====░==░=░======░░==░=░"
    )
        print(Fore.BLUE + "Made by: BeanD        JustProblem            TG: https://t.me/BeanD_TM")
        print(
        Fore.BLUE + "My Projects:            v: 0.1               TG: https://t.me/ProjectsByBeanD"
    )
        print(
        Fore.GREEN
        + "====░=====░=====░==░=░======░=░=====░=====░==░=====░=====░==░=░======░░==░=░"
    )
        print("                         |                    ")
        print("                         |                    ")
        print("                         V                    ")
        print(Fore.RED + "1 - Русский")
        print(Fore.RED + "2 - English")

        lang = int(
        input(
            Fore.YELLOW
            + Style.BRIGHT
            + "Выберите язык программы/Choose the language of the program: "
        )
    )

        if lang == 1:
                rus()
        elif lang == 2:
                eng()
        else:
                main()
main()