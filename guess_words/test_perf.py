import time
from main import fetch_words_from_api

def test_fetch_words_performance():
    print("▶️ Performance Test - fetch_words_from_api")

    start_time = time.time()
    fetch_words_from_api(length=5, max_results=100)
    end_time = time.time()

    duration = end_time - start_time
    print(f"⏱️ Waktu eksekusi: {duration:.4f} detik")

    assert duration < 2.0, "fetch_words terlalu lambat!"

if __name__ == '__main__':
    test_fetch_words_performance()
