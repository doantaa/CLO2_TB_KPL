"""
Main Menu Game Launcher
Menampilkan menu terminal dan mengeksekusi game sesuai pilihan pengguna.
"""

import platform
import subprocess
import sys
import os

# Import sesuai OS
if platform.system() == "Windows":
    from InquirerPy import inquirer
else:
    from simple_term_menu import TerminalMenu


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_game(path: str):
    """
    Menjalankan file python game berdasarkan path.
    Setelah game selesai, tunggu input dari user sebelum kembali ke menu utama.
    """
    try:
        subprocess.call([sys.executable, path])
        input("\nGame selesai. Tekan Enter untuk kembali ke menu utama...")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan game: {e}")


def exit_program():
    """Keluar dari program."""
    print("Terima kasih telah bermain 👋")
    sys.exit(0)


def main():
    """
    Fungsi utama yang menampilkan menu dan menangani input pengguna.
    """
    menu_options = [
        "Tic Tac Toe",
        "RPG",
        "Typing Speed Game",
        "Keluar"
    ]

    actions = {
        "Tic Tac Toe": lambda: run_game("tic_tac_toe/tic_tac_toe_main.py"),
        "RPG": lambda: run_game("rpg/rpg_main.py"),
        "Typing Speed Game": lambda: run_game("guess_words/guess_words_main.py"),
        "Keluar": exit_program
    }

    while True:
        clear_screen()
        title = """
  __  __ _       _    _____                      
 |  \/  (_)     (_)  / ____|                     
 | \  / |_ _ __  _  | |  __  __ _ _ __ ___   ___ 
 | |\/| | | '_ \| | | | |_ |/ _` | '_ ` _ \ / _ |
 | |  | | | | | | | | |__| | (_| | | | | | |  __/
 |_|  |_|_|_| |_|_|  \_____|\__,_|_| |_| |_|\___|
  _______                     _  _                
 |__   __|                   | || |               
    | | ___  __ _ _ __ ___   | || |_              
    | |/ _ \/ _` | '_ ` _ \  |__   _|            
    | |  __/ (_| | | | | | |    | |               
    |_|\___|\__,_|_| |_| |_|    |_|               
        """

        print(title)

        if platform.system() == "Windows":
            selected_option = inquirer.select(
                message="Pilih game yang ingin dijalankan:",
                choices=menu_options
            ).execute()
        else:
            terminal_menu = TerminalMenu(menu_options)
            selected_index = terminal_menu.show()
            selected_option = menu_options[selected_index]

        action = actions.get(selected_option)
        if action:
            action()
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
