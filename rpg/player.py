# ====================
# Player Classes
# ====================

import random
import configuration

class Player:
    def __init__(self, name, starting_hp, exp_to_next):
        self.name = name
        self.level = 1
        self.hp = starting_hp
        self.max_hp = starting_hp
        self.exp = 0
        self.exp_to_next = exp_to_next

    def attack(self):
        return random.randint(10, 20)

    def gain_exp(self, amount):
        self.exp += amount
        print(f"\n✨ {self.name} mendapat {amount} EXP!")
        if self.exp >= self.exp_to_next:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_to_next += 50
        self.max_hp += configuration.LEVEL_UP_BONUS_HP
        self.hp = self.max_hp
        print(f"\n🎉 Level up! {self.name} sekarang level {self.level}!")

    def print_header(self):
        """Menampilkan header dengan status pemain (nama, HP, level)."""
        print(f"╔═════════════════════════════════")
        print(f"║  {self.name}")
        print(f"║  HP: {self.hp}/{self.max_hp}    ")
        print(f"║  Exp: {self.exp}/{self.exp_to_next}    ")
        print(f"║  Level: {self.level}    ")
        print(f"╚════════════════════════════════")

class Enemy:
    def __init__(self, name, hp, attack_range):
        self.name = name
        self.hp = hp
        self.attack_range = attack_range

    def attack(self):
        return random.randint(*self.attack_range)
    def print_header(self):
        """Menampilkan header dengan status pemain (nama, HP, level)."""
        print(f"║  Enemy: {self.name}")
        print(f"║  HP: {self.hp}")
        print(f"╚════════════════════════════════")

