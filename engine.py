import os
import pygame as engine
from colorama import init, Fore

init()
print(Fore.CYAN + '{:*^18}'.format("CYBER PLAYER"), "\n")


def setting():
    print(Fore.YELLOW + "CYBER PLAYER HELPER\n"
                        "/command - MENU: Return you in general menu.\n"
                        "/command - STOP: Stops the song.\n"
                        "/command - PAUSE: Paused the song.\n"
                        "/command - CONT: Enter CONT after PAUSE for continue music.\n"
                        "/command - VOL: You can change volume. Max value = 1. You can enter the float value.\n")


def out_main():
    print(Fore.WHITE + f"USERNAME:", Fore.LIGHTWHITE_EX + f"{os.getlogin()}\n")

    # output playlist
    playlist = {}
    count = 0
    count_list = 0
    for root, dirs, files in os.walk("music"):
        for filename in files:
            count += 1
            playlist[f'{count}'] = filename

    for i in playlist:
        count_list += 1
        print(Fore.LIGHTCYAN_EX + f'{count_list}.', playlist.get(i))
    # output playlist//

    while True:
        try:
            print(Fore.YELLOW + "")
            number = input("ENTER SONG: ")
            while int(number) > len(playlist) or not number.isdigit():
                print(" - Nothing")
                number = input("ENTER: ")
            break
        except ValueError:
            print(Fore.RED + "Invalid value")
            continue

    def run():
        engine.init()
        engine.mixer.music.load(f'music/{playlist.get(number)}')
        engine.mixer.music.play(-1)

        while True:
            print("")
            print(Fore.LIGHTBLUE_EX + f" - NOW PLAY: {playlist.get(number)}")
            print(Fore.LIGHTGREEN_EX + "")
            value = input("GET Command: ")
            value = value.upper()
            if value == 'MENU':
                out_main()

            elif value == "STOP":
                engine.mixer.music.stop()
                out_main()

            elif value == "PAUSE":
                engine.mixer.music.pause()

            elif value == "CONT":
                engine.mixer.music.unpause()
            elif value == "VOL":
                print(Fore.LIGHTCYAN_EX + "")
                volume = input("Enter volume: ")
                volume = float(volume)
                engine.mixer.music.set_volume(volume)

            elif value == "HELP":
                setting()

            elif value == "RADIO":
                for song in playlist:
                    engine.mixer.music.load(f'music/{playlist.get(song)}')
                    engine.mixer.music.play(-1)

            elif len(value) == 0:
                print(Fore.RED + "Field is empty!")

            else:
                print(Fore.RED + "Command not found. Try again.")

    run()


if __name__ == '__main__':
    out_main()
