import time
import cProfile
import pstats
import psutil
from datetime import datetime

from rpg_logic import random_event
from player import Player  # Pastikan kelas Player tersedia

def test_random_event_performance():
    print("▶️ Performance Test - random_event(player)\n")
    start_time = time.time()

    # 🧠 Ambil info awal penggunaan resource
    process = psutil.Process()
    cpu_start = psutil.cpu_percent(interval=None)
    mem_start = process.memory_info().rss / (1024 * 1024)  # dalam MB

    # 🔍 CProfile setup
    profiler = cProfile.Profile()
    profiler.enable()

    # Inisialisasi player dummy
    player = Player(name="Tester", starting_hp=100, exp_to_next=100)
    random_event(player)

    profiler.disable()
    end_time = time.time()

    # 📊 Hitung hasil akhir
    cpu_end = psutil.cpu_percent(interval=None)
    mem_end = process.memory_info().rss / (1024 * 1024)
    duration = end_time - start_time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cpu_usage = cpu_end
    mem_usage = mem_end - mem_start

    # Save profiling stats
    profiler.dump_stats("rpg/game_logic_performance.prof")

    status = 'LULUS' if duration < 2.0 else 'GAGAL (Terlalu lambat)'

    with open("rpg/game_logic_performance_result.txt", "w") as f:
        f.write(f"📅 Waktu Uji: {timestamp}\n")
        f.write("▶️ Performance Test - random_event(player)\n")
        f.write(f"⏱️ Waktu Eksekusi: {duration:.4f} detik\n")
        f.write(f"🧠 CPU Usage: ~{cpu_usage:.2f}%\n")
        f.write(f"💾 RAM Usage: ~{mem_usage:.2f} MB\n")
        f.write(f"✅ Status: {status}\n\n")
        f.write("🔎 Rangkuman cProfile (Top 10 fungsi berdasarkan cumulative time):\n")

        stats = pstats.Stats(profiler, stream=f)
        stats.strip_dirs().sort_stats('cumtime').print_stats(10)

    # Tampilkan juga ke terminal
    print(f"📅 Waktu Uji: {timestamp}")
    print(f"⏱️ Waktu Eksekusi: {duration:.4f} detik")
    print(f"🧠 CPU Usage: ~{cpu_usage:.2f}%")
    print(f"💾 RAM Usage: ~{mem_usage:.2f} MB")
    print(f"✅ Status: {status}")
    print("\n🔎 Rangkuman cProfile (Top 10 fungsi):\n")

    stats = pstats.Stats(profiler)
    stats.strip_dirs().sort_stats('cumtime').print_stats(10)

    assert duration < 2.0, "random_event terlalu lambat!"

if __name__ == '__main__':
    test_random_event_performance()
