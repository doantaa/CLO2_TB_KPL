def display_board(board):
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

# Tabel kombinasi kemenangan
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Baris
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Kolom
    (0, 4, 8), (2, 4, 6)              # Diagonal
]

def check_win(board, player_symbol):
    return any(all(board[i] == player_symbol for i in combo) for combo in winning_combinations)

def check_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def get_valid_move(board):
    while True:
        try:
            move = int(input("Pilih posisi (1-9): ")) - 1
            if 0 <= move < 9 and board[move] not in ['X', 'O']:
                return move
            else:
                print("Posisi tidak valid atau sudah diisi, coba lagi.")
        except ValueError:
            print("Input harus berupa angka antara 1 hingga 9.")

def display_scoreboard(scoreboard):
    print("\n===== SCOREBOARD AKHIR =====")
    for name, score in scoreboard.items():
        print(f"{name} ({score['symbol']}): {score['wins']} menang")
    print("============================\n")

# Table-Driven Construction (menu navigasi)
def main_menu():
    actions = {
        "1": start_game,
        "2": exit_game
    }

    while True:
        print("=== MENU UTAMA ===")
        print("1. Mulai Game")
        print("2. Keluar")
        choice = input("Pilih menu: ")
        action = actions.get(choice)

        if action:
            action()
        else:
            print("Pilihan tidak valid, coba lagi.")

# Fungsi keluar
def exit_game():
    print("Terima kasih telah bermain! 👋")
    exit()


# Jalankan program
if __name__ == "__main__":
    main_menu()
