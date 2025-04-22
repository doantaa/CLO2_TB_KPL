from player import Player
from rpg_logic import random_event, heal_player
import configuration
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Menampilkan menu pilihan dan lokasi saat ini."""

    print("\n📍 Lokasi saat ini: Hutan Damai")
    print("Apa yang ingin kamu lakukan?")
    print("[1] Jelajahi")
    print("[2] Istirahat")
    print("[3] Keluar")

def main():
    clear_screen()
    text = """ 
   _________    ______  ______  ___    ____  ___       ____  ____  ______
  / ____/   |  / __ \ \/ / __ )/   |  / __ \/   |     / __ \/ __ \/ ____/ 
 / /   / /| | / /_/ /\  / __  / /| | / /_/ / /| |    / /_/ / /_/ / / __  
/ /___/ ___ |/ ____/ / / /_/ / ___ |/ _, _/ ___ |   / _, _/ ____/ /_/ /  
\____/_/  |_/_/     /_/_____/_/  |_/_/ |_/_/  |_|  /_/ |_/_/    \____/  
 
Welcome to RPG Game!                                                                                                                         
    """

    print(text)

    name = input("Masukkan nama Capybara kamu: ") or "CapyBoi"
    player = Player(name, configuration.STARTING_HP, configuration.EXP_TO_NEXT)
    clear_screen()
    choice = "0"

    while True:
        if choice == "0":
            player.print_header()
            print_menu()
            choice = input("> ")
        if choice == "1":
            clear_screen()
            player.print_header()
            random_event(player)
            print_menu()
        elif choice == "2":
            clear_screen()
            player.print_header()
            heal_player(player)
            print_menu()
        elif choice == "3":
            clear_screen()
            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀  ______          _                    __ __           _ __  
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀ /_  __/__  _____(_)___ ___  ____ _   / //_/___ ______(_) /_ 
⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀  / / / _ \/ ___/ / __ `__ \/ __ `/  / ,< / __ `/ ___/ / __ |
⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ / / /  __/ /  / / / / / / / /_/ /  / /| / /_/ (__  ) / / / /
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀/_/  \___/_/  /_/_/ /_/ /_/\__,_/  /_/ |_\__,_/____/_/_/ /_/ 
⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀
            """)
            break
        else:
            print("Pilihan tidak valid.")
            time.sleep(1.5)

        choice = input("> ")

if __name__ == "__main__":
    main()
