import time
import cProfile
import pstats
from datetime import datetime
import psutil
from guess_words_main import fetch_words_from_api

def test_fetch_words_performance():
    print("▶️ Performance Test - fetch_words_from_api\n")
    start_time = time.time()

    # 🧠 Ambil info awal penggunaan resource
    process = psutil.Process()
    cpu_start = psutil.cpu_percent(interval=None)
    mem_start = process.memory_info().rss / (1024 * 1024)  # dalam MB

    # 🔍 CProfile setup
    profiler = cProfile.Profile()
    profiler.enable()

    fetch_words_from_api(length=5, max_results=100)

    profiler.disable()
    end_time = time.time()

    # 📊 Hitung hasil akhir
    cpu_end = psutil.cpu_percent(interval=None)
    mem_end = process.memory_info().rss / (1024 * 1024)
    duration = end_time - start_time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cpu_usage = cpu_end
    mem_usage = mem_end - mem_start

    # Save profiling stats as .prof (raw format)
    profiler.dump_stats("performance_stats.prof")

    # Tampilkan dan simpan ringkasan
    status = 'LULUS' if duration < 2.0 else 'GAGAL (Terlalu lambat)'

    # Simpan ke file
    with open("performance_result.txt", "w") as f:
        f.write(f"📅 Waktu Uji: {timestamp}\n")
        f.write("▶️ Performance Test - fetch_words_from_api\n")
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

    assert duration < 2.0, "fetch_words terlalu lambat!"

if __name__ == '__main__':
    test_fetch_words_performance()
