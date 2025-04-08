# ====================
# Runtime Configuration
# ====================
CONFIG = {
    "player": {
        "hp": 100,
        "attack": 20,
        "defense": 8
    },
    "enemies": [
        {"name": "Slime", "hp": 40, "attack": 12, "defense": 4},
        {"name": "Goblin", "hp": 60, "attack": 18, "defense": 6},
        {"name": "Troll", "hp": 80, "attack": 25, "defense": 10}
    ],
    "actions": {
        "attack": {
            "label": "⚔️ Serang",
            "effect": lambda player, enemy: enemy.take_damage(player.deal_damage())
        },
        "defend": {
            "label": "🛡️ Bertahan",
            "effect": lambda player, enemy: player.defend()
        },
        "heal": {
            "label": "💖 Sembuh",
            "effect": lambda player, enemy: player.heal(15)
        }
    }
}