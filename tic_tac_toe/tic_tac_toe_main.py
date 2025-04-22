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

if __name__ == "__main__":
    tic_tac_toe()
