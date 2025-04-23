import timeit

setup_code = '''
from tic_tac_toe_main import check_win
board = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
'''

execution_time = timeit.timeit("check_win(board, 'X')", setup=setup_code, number=100000)
print(f"Waktu eksekusi check_win sebanyak 100000x: {execution_time:.5f} detik")
