
# Mulai game
def start_game():
    player1_name = input("Masukkan nama pemain 1 (X): ")
    player2_name = input("Masukkan nama pemain 2 (O): ")

    scoreboard = {
        player1_name: {'symbol': 'X', 'wins': 0},
        player2_name: {'symbol': 'O', 'wins': 0}
    }

    play_again = 'y'

    while play_again.lower() == 'y':
        board = ['1','2','3','4','5','6','7','8','9']
        current_symbol = 'X'
        current_player = player1_name

        print("\n🎮 Game Dimulai!")
        display_board(board)

        game_over = False
        while not game_over:
            print(f"Giliran {current_player} ({current_symbol})")
            move = get_valid_move(board)
            board[move] = current_symbol
            display_board(board)

            if check_win(board, current_symbol):
                print(f"🎉 Selamat {current_player}, kamu menang!")
                scoreboard[current_player]['wins'] += 1
                game_over = True
            elif check_draw(board):
                print("😐 Yahh permainan seri.")
                game_over = True
            else:
                current_symbol = 'O' if current_symbol == 'X' else 'X'
                current_player = player2_name if current_player == player1_name else player1_name

        play_again = input("Main lagi? (yes/no): ")

    display_scoreboard(scoreboard)

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
