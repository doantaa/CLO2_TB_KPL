import cProfile
import pstats
import time
import datetime
import os
import psutil
from tic_tac_toe_main import check_win, check_draw

def run_performance_test():
    board_win = ['X', 'X', 'X', '4', '5', '6', '7', '8', '9']
    board_draw = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']

    for _ in range(10000):
        check_win(board_win, 'X')
        check_draw(board_draw)

if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    start_time = time.time()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    profiler = cProfile.Profile()
    profiler.enable()

    try:
        run_performance_test()
        status = "SUKSES ✅"
    except Exception as e:
        status = f"GAGAL (Terlalu lambat) ❌ ({e})"

    profiler.disable()
    end_time = time.time()
    duration = end_time - start_time
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

    print(f"📅 Waktu Uji: {timestamp}")
    print(f"⏱️ Waktu Eksekusi: {duration:.4f} detik")
    print(f"🧠 CPU Usage: ~{cpu_usage:.2f}%")
    print(f"💾 RAM Usage: ~{mem_usage:.2f} MB")
    print(f"✅ Status: {status}")
    print(f"🔎 Rangkuman cProfile (Top 10 fungsi):\n")

    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(10)
