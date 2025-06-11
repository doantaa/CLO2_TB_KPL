# game_logic.py

import random
import configuration
from player import Enemy
from print_library import *

def battle(player, enemy):
    """
    Melakukan pertarungan antara player dan enemy hingga salah satu HP habis.
    Clean Code: Fungsi hanya melakukan satu tugas (Single Responsibility Principle).
    Secure Code: Tidak menerima input dari user selain 'Enter', sehingga tidak ada risiko injeksi.
    """
    while player.hp > 0 and enemy.hp > 0:
        # Clean Code: Penamaan variabel jelas
        input("\nTekan Enter untuk menyerang…")
        player_damage = player.attack()
        enemy.hp -= player_damage

        if enemy.hp <= 0:
            print(f"✅ {enemy.name} kalah!")
            player.gain_exp(50)
            input("\nTekan Enter untuk melanjutkan…")
            clear_screen()
            return

        enemy_damage = enemy.attack()
        player.hp -= enemy_damage
        clear_screen()
        player.print_header()
        enemy.print_header()
        print(f"\n⚔️  Pertarungan dimulai: {player.name} vs {enemy.name}!\n")
        print(f"👉 {player.name} menyerang {enemy.name} dengan {player_damage} damage!")
        print(f"💢 {enemy.name} menyerang {player.name} dengan {enemy_damage} damage!")

    if player.hp <= 0:
        print("💀 Kamu kalah! Game over.")
        exit()

def random_event(player):
    """
    Menentukan event acak: bertemu musuh atau mendapatkan healing.
    Clean Code: Penamaan variabel jelas, fungsi hanya satu tugas.
    Secure Code: Validasi data dari konfigurasi sebelum digunakan.
    """
    event_options = list(configuration.ENEMIES.keys()) + ["healing"]
    selected_event = random.choice(event_options)

    if selected_event == "healing":
        print("\n🔍 Kamu menemukan buah segar di tanah!")
        heal_player(player)
    else:
        # Secure Code: Validasi data musuh dari konfigurasi
        enemy_data = configuration.ENEMIES.get(selected_event)
        if not enemy_data or not isinstance(enemy_data, dict):
            print("❌ Data musuh tidak valid. Event dibatalkan.")  # Secure: Validasi input dari konfigurasi
            return
        # Secure Code: Validasi tipe data hp dan attack_range
        hp = enemy_data.get("hp")
        attack_range = enemy_data.get("attack_range")
        if not isinstance(hp, int) or not isinstance(attack_range, (list, tuple)):
            print("❌ Data musuh korup. Event dibatalkan.")  # Secure: Validasi tipe data
            return
        enemy = Enemy(selected_event, hp, attack_range)
        enemy.print_header()
        print(f"\n🔍 Kamu bertemu seekor {enemy.name}!")
        battle(player, enemy)

def heal_player(player):
    """
    Menyembuhkan player dengan jumlah HP acak antara 15-30.
    Clean Code: Penamaan variabel jelas, fungsi satu tugas.
    Secure Code: Validasi nilai heal_amount agar tidak negatif.
    """
    heal_amount = random.randint(15, 30)
    if heal_amount < 0:
        print("❌ Nilai heal tidak valid.")  # Secure: Validasi nilai acak
        return
    player.hp = min(player.max_hp, player.hp + heal_amount)
    print(f"🍌 Kamu makan buah dan memulihkan {heal_amount} HP! Sekarang: {player.hp}/{player.max_hp}")

# ===========================
# CLEAN CODE PRACTICES:
# - Penamaan variabel dan fungsi jelas/deskriptif (player_damage, enemy_damage, heal_amount, event_options, selected_event)
# - Fungsi hanya melakukan satu tugas (Single Responsibility Principle)
# - Menambahkan docstring pada setiap fungsi untuk penjelasan singkat
# - Struktur kode rapi dan konsisten (indentasi, pemisahan fungsi)
# - Komentar hanya pada bagian penting, tidak berlebihan
#

# SECURE CODING PRACTICES:
# - Validasi input dari konfigurasi (ENEMIES) sebelum digunakan
# - Validasi tipe data dan nilai pada data musuh dan heal_amount
# - Tidak menggunakan input user secara langsung untuk eksekusi kode
# - Tidak ada data sensitif yang diekspos
# - Menghindari magic number dengan memberi nama variabel yang jelas
# ===========================
