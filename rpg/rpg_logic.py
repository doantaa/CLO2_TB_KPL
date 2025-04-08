# ====================
# Game Logic
# ====================
import random

from characters import Character, Player
from configuration import CONFIG


def choose_enemy():
    enemy_data = random.choice(CONFIG["enemies"])
    return Character(**enemy_data)


def battle(player: Player, enemy: Character):
    print(f"⚔️ Pertarungan dimulai: {player.name} vs {enemy.name}")

    original_def = player.defense
    while player.is_alive() and enemy.is_alive():
        print(f"{player}")
        print(f"{enemy}")

        # Display action menu
        for i, (key, action) in enumerate(CONFIG["actions"].items(), 1):
            print(f"{i}. {action['label']}")
        choice = input("Pilih aksi: ")

        try:
            action_key = list(CONFIG["actions"].keys())[int(choice) - 1]
            action = CONFIG["actions"][action_key]
            action["effect"](player, enemy)
        except (IndexError, ValueError):
            print("Pilihan tidak valid.")
            continue

        if enemy.is_alive():
            damage = enemy.deal_damage()
            print(f"{enemy.name} menyerang balik!")
            player.take_damage(damage)

        # Reset defense if defended
        player.reset_defense(original_def)

    # Result
    if player.is_alive():
        print(f"🎉 {player.name} menang!")
    else:
        print(f"💀 {player.name} kalah... Coba lagi nanti.")

