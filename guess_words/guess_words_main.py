import time
import random
import json
import os
import sys

WORDS = ["python", "keyboard", "runtime", "variable", "function",
         "object", "modular", "looping", "import", "random"]

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path) as f:
            config = json.load(f)
    except FileNotFoundError:
        print("❌ config.json tidak ditemukan.")
        sys.exit(1)

    validate_config(config)
    return config

def validate_config(config):
    assert config.get("mode") in ["susun", "tebak"], "Config error: mode harus 'susun' atau 'tebak'."
    assert isinstance(config.get("rounds"), int) and config["rounds"] > 0, "Config error: rounds harus > 0."

def get_user_config(default_config):
    print("\n📦 Runtime Config Detected:")
    print(f"Mode default: {default_config['mode']}")
    print(f"Jumlah ronde default: {default_config['rounds']}")

    pilih = input("Gunakan config ini? (y/n): ").strip().lower()
    if pilih == 'y':
        return default_config
    else:
        # Interaktif input
        while True:
            mode = input("Pilih mode (susun / tebak): ").strip().lower()
            if mode in ["susun", "tebak"]:
                break
            print("❗ Mode tidak valid.")

        while True:
            try:
                rounds = int(input("Jumlah ronde (angka > 0): "))
                if rounds > 0:
                    break
            except ValueError:
                pass
            print("❗ Jumlah ronde tidak valid.")

        user_config = {"mode": mode, "rounds": rounds}
        validate_config(user_config)
        return user_config

def countdown(seconds):
    print("⏳ Persiapan...")
    for i in range(seconds, 0, -1):
        print(f"{i}...", end=" ", flush=True)
        time.sleep(1)
    print("\n💥 Mulai!")

def play_susun_kata(config):
    print("\n🧠 Susun Kata!")
    score = 0

    for i in range(config["rounds"]):
        print(f"\n🔀 Round {i+1}")
        word = random.choice(WORDS)
        scrambled = ''.join(random.sample(word, len(word)))
        assert sorted(scrambled) == sorted(word)

        print(f"Susun huruf ini: {scrambled}")
        answer = input("➤ Jawaban kamu: ")

        if answer.strip().lower() == word:
            print("✅ Betul!")
            score += 1
        else:
            print(f"❌ Salah! Jawaban: {word}")

    print(f"\n🏁 Selesai! Skor kamu: {score}/{config['rounds']}")

def play_hangman(config):
    print("\n🕵️ Tebak Kata (Tebak Kata)!")
    score = 0

    for i in range(config["rounds"]):
        print(f"\n🎯 Round {i+1}")
        word = random.choice(WORDS)
        guessed = ["_"] * len(word)
        attempts = len(word) + 2

        while attempts > 0 and "_" in guessed:
            print("Kata: " + " ".join(guessed))
            guess = input("➤ Tebak huruf: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print("❗ Masukkan satu huruf.")
                continue

            if guess in word:
                for idx, char in enumerate(word):
                    if char == guess:
                        guessed[idx] = guess
                print("✅ Betul!")
            else:
                attempts -= 1
                print(f"❌ Salah! Sisa: {attempts}")

        if "_" not in guessed:
            print(f"🎉 Selamat! Kata: {word}")
            score += 1
        else:
            print(f"😢 Gagal! Jawaban: {word}")

    print(f"\n🏁 Selesai! Skor kamu: {score}/{config['rounds']}")

def guess_words_main():
    default_config = load_config()
    config = get_user_config(default_config)

    print("=== 🎮 GAME SUSUN KATA & TEBAK KATA ===")

    if config["mode"] == "susun":
        play_susun_kata(config)
    elif config["mode"] == "hangman":
        play_hangman(config)
    else:
        print("❌ Mode tidak dikenal.")

if __name__ == "__main__":
    main()
