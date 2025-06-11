import time
from player import Player, Enemy
from rpg_logic import battle, random_event
import configuration

import builtins
builtins.input = lambda prompt="": None

def test_battle():
    player = Player("TestHero", configuration.STARTING_HP, configuration.EXP_TO_NEXT)
    enemy = Enemy("TestEnemy", 30, (5, 10))
    start = time.time()
    battle(player, enemy)
    duration = time.time() - start
    return ("Battle Function", duration)

def test_random_events():
    player = Player("Explorer", configuration.STARTING_HP, configuration.EXP_TO_NEXT)
    start = time.time()
    for _ in range(5):
        random_event(player)
    duration = time.time() - start
    return ("Random Events (x5)", duration)


def run_tests():
    print("📊 SIMPLE PERFORMANCE TESTING\n")
    tests = [test_battle]
    for test in tests:
        name, duration = test()
        print(f"{name}: {duration:.4f} detik")

if __name__ == "__main__":
    run_tests()
