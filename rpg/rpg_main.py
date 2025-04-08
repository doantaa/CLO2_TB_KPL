from characters import Player
from rpg_logic import choose_enemy, battle


def main():
    print("👋 Selamat datang di RPG!")
    name = input("Masukkan nama karaktermu: ")
    player = Player(name)

    enemy = choose_enemy()
    battle(player, enemy)

    print("🏁 Permainan selesai. Terima kasih sudah bermain!")


if __name__ == "__main__":
    main()
