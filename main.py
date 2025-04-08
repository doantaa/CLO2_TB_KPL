from simple_term_menu import TerminalMenu
import subprocess

menu_options = ["Tic Tac Toe", "RPG", "Typing Speed Game", "Keluar"]

while True :
    terminal_menu = TerminalMenu(menu_options, title="Main Menu")
    menu_index = terminal_menu.show()

    if menu_index == 0:
        subprocess.call(["python", "tic_tac_toe.py"])
        input("Game Berakhir, press Enter untuk kembali ke main menu...")
    elif menu_index == 1:
        subprocess.call(["python", "rpg.py"])
        input("Game Berakhir, press Enter untuk kembali ke main menu...")
    elif menu_index == 2:
        subprocess.call(["python", "typing_speed.py"])
        input("Game Berakhir, press Enter untuk kembali ke main menu...")
    elif menu_index == 3:
        print("Terimakasih telah bermain")
        break

