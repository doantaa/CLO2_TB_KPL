"""
Main Menu Game Launcher
Menampilkan menu terminal dan mengeksekusi game sesuai pilihan pengguna.
"""

from simple_term_menu import TerminalMenu
import subprocess
import sys


import os

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
        0: lambda: run_game("tic_tac_toe/tic_tac_toe_main.py"),
        1: lambda: run_game("rpg/rpg_main.py"),
        2: lambda: run_game("guess_words/guess_words_main.py"),
        3: exit_program
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
        terminal_menu = TerminalMenu(menu_options, title=title)
        selected_index = terminal_menu.show()

        action = actions.get(selected_index)

        if action:
            action()
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
