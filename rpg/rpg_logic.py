# ====================
# Game Logic
# ====================

import random
import configuration
from player import Enemy
from print_library import *


def battle(player, enemy):
    while player.hp > 0 and enemy.hp > 0:

        input("\nTekan Enter untuk menyerang...")
        dmg = player.attack()
        enemy.hp -= dmg

        if enemy.hp <= 0:
            print(f"✅ {enemy.name} kalah!")
            player.gain_exp(50)
            input("\nTekan Enter untuk melanjutkan...")
            clear_screen()
            return

        edmg = enemy.attack()
        player.hp -= edmg
        clear_screen()
        player.print_header()
        enemy.print_header()
        print(f"\n⚔️  Pertarungan dimulai: {player.name} vs {enemy.name}!\n")
        print(f"👉 {player.name} menyerang {enemy.name} dengan {dmg} damage!")
        print(f"💢 {enemy.name} menyerang {player.name} dengan {edmg} damage!")


    if player.hp <= 0:
        print("💀 Kamu kalah! Game over.")
        exit()


def random_event(player):
    event_keys = list(configuration.ENEMIES.keys()) + ["healing"]
    chosen = random.choice(event_keys)

    if chosen == "healing":
        print("\n🔍 Kamu menemukan buah segar di tanah!")
        heal_player(player)
    else:
        enemy_data = configuration.ENEMIES[chosen]
        enemy = Enemy(chosen, enemy_data["hp"], enemy_data["attack_range"])
        enemy.print_header()
        print(f"\n🔍 Kamu bertemu seekor {enemy.name}!")
        battle(player, enemy)

def heal_player(player):
    heal = random.randint(15, 30)
    player.hp = min(player.max_hp, player.hp + heal)
    print(f"🍌 Kamu makan buah dan memulihkan {heal} HP! Sekarang: {player.hp}/{player.max_hp}")