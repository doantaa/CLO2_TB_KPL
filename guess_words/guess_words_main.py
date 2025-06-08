title = """

                           ('-.    .-')     .-')           (`\ .-') /`             _  .-')  _ .-') _    .-')    
                         _(  OO)  ( OO ).  ( OO ).          `.( OO ),'            ( \( -O )( (  OO) )  ( OO ).  
  ,----.    ,--. ,--.   (,------.(_)---\_)(_)---\_)      ,--./  .--.   .-'),-----. ,------. \     .'_ (_)---\_) 
 '  .-./-') |  | |  |    |  .---'/    _ | /    _ |       |      |  |  ( OO'  .-.  '|   /`. ',`'--..._)/    _ |  
 |  |_( O- )|  | | .-')  |  |    \  :` `. \  :` `.       |  |   |  |, /   |  | |  ||  /  | ||  |  \  '\  :` `.  
 |  | .--, \|  |_|( OO )(|  '--.  '..`''.) '..`''.)      |  |.'.|  |_)\_) |  |\|  ||  |_.' ||  |   ' | '..`''.) 
(|  | '. (_/|  | | `-' / |  .--' .-._)   \.-._)   \      |         |    \ |  | |  ||  .  '.'|  |   / :.-._)   \ 
 |  '--'  |('  '-'(_.-'  |  `---.\       /\       /      |   ,'.   |     `'  '-'  '|  |\  \ |  '--'  /\       / 
  `------'   `-----'     `------' `-----'  `-----'       '--'   '--'       `-----' `--' '--'`-------'  `-----'  
                                                                                                                         
"""

import time
import random
import requests
import os 

def clear_screen():
    # ✅ Clean Code: Fungsi single responsibility, nama jelas, tidak menerima input user.
    os.system('cls' if os.name == 'nt' else 'clear')


def fetch_words_from_api(length=5, max_results=10):
    # ✅ Clean Code: Validasi parameter pakai assert
    assert isinstance(length, int) and length > 0, "length harus bilangan bulat positif"
    assert isinstance(max_results, int) and max_results > 0, "max_results harus bilangan bulat positif"

    try:
        # ✅ Clean Code: Penamaan variabel jelas dan meaningful
        pattern = "?" * length
        url = f"https://api.datamuse.com/words?sp={pattern}&max={max_results}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        words = [item["word"] for item in data if item["word"].isalpha()]
        return words if words else ["default", "kata", "cadangan"]
    except requests.RequestException:
        # ✅ Clean Code: Fallback mechanism ketika terjadi error
        print("❌ Gagal mengambil kata dari Datamuse API. Gunakan fallback.")
        return ["default", "kata", "cadangan"]


def countdown(seconds):
    # ✅ Clean Code: Fungsi kecil, melakukan satu hal saja, modular dan reusable
    print("⏳ Persiapan...")
    for i in range(seconds, 0, -1):
        print(f"{i}...", end=" ", flush=True)
        time.sleep(1)
    print("\n💥 Mulai!")


def play_susun_kata(words, rounds, cheat=False):
    # ✅ Clean Code: Fungsi punya parameter jelas (input list, jumlah ronde, mode cheat)
    print("\n🧠 Susun Kata!")
    score = 0

    for i in range(rounds):
        print(f"\n🔀 Round {i+1}")
        word = random.choice(words)
        scrambled = ''.join(random.sample(word, len(word)))

        # ✅ Clean Code: Validasi menggunakan assert, menjamin scrambling benar
        assert sorted(scrambled) == sorted(word)

        print(f"Susun huruf ini: {scrambled}")
        if cheat:
            print(f"💡 (Jawaban: {word})")

        answer = input("➤ Jawaban kamu: ")
        if answer.strip().lower() == word:
            print("✅ Betul!")
            score += 1
        else:
            print(f"❌ Salah! Jawaban: {word}")

    print(f"\n🏁 Selesai! Skor kamu: {score}/{rounds}")


def play_hangman(words, rounds):
    # ✅ Clean Code: Fungsi modular dan deskriptif
    print("\n🕵️ Tebak Kata!")
    score = 0

    for i in range(rounds):
        print(f"\n🎯 Round {i+1}")
        word = random.choice(words)
        guessed = ["_"] * len(word)
        attempts = len(word) + 2

        while attempts > 0 and "_" in guessed:
            print("Kata: " + " ".join(guessed))
            guess = input("➤ Tebak huruf: ").strip().lower()

            # ✅ Clean Code: Validasi input user dengan handling error
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

    print(f"\n🏁 Selesai! Skor kamu: {score}/{rounds}")


def main():
    # ✅ Clean Code: Struktur main terpisah dari logika inti, mudah dibaca
    clear_screen()
    print(title)
    
    try:
        length = int(input("Masukkan panjang kata yang diinginkan (misal 5): "))
    except ValueError:
        print("❗ Input tidak valid, gunakan angka. Default ke 5.")
        length = 5

    words = fetch_words_from_api(length=length)
    rounds = 3
    mode = input("Pilih mode (susun / tebak): ").strip().lower()

    cheat = True  # Untuk debugging/testing
    countdown(3)

    if mode == "susun":
        play_susun_kata(words, rounds, cheat)
    elif mode == "tebak":
        play_hangman(words, 1)
    else:
        print("❌ Mode tidak dikenal.")


if __name__ == "__main__":
    main()
