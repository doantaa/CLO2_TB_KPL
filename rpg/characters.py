# ====================
# Character Classes
# ====================
import random

from configuration import CONFIG


class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        damage_taken = max(0, amount - self.defense)
        self.hp -= damage_taken
        print(f"{self.name} menerima {damage_taken} damage! (HP: {self.hp})")

    def deal_damage(self):
        return self.attack + random.randint(-5, 5)

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"


class Player(Character):
    def __init__(self, name):
        stats = CONFIG["player"]
        super().__init__(name, stats["hp"], stats["attack"], stats["defense"])

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} menyembuhkan diri (+{amount} HP)! (HP: {self.hp})")

    def defend(self):
        boost = 5
        self.defense += boost
        print(f"{self.name} meningkatkan pertahanan sementara (+{boost} DEF).")
        return boost

    def reset_defense(self, original_def):
        self.defense = original_def
