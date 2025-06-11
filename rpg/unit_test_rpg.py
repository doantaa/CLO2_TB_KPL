import unittest
from unittest.mock import patch
from player import Player, Enemy
import configuration
from rpg_logic import heal_player, random_event


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestPlayer", 100, 100)

    def test_attack_range(self):
        for _ in range(100):
            dmg = self.player.attack()
            self.assertTrue(10 <= dmg <= 20)

    def test_gain_exp_and_level_up(self):
        self.player.gain_exp(150)
        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.player.exp, 0)
        self.assertEqual(self.player.hp, self.player.max_hp)
        self.assertEqual(self.player.exp_to_next, 150)

    def test_heal_player(self):
        self.player.hp = 50
        with patch('random.randint', return_value=20):
            heal_player(self.player)
            self.assertEqual(self.player.hp, 70)

    def test_heal_cannot_exceed_max_hp(self):
        self.player.hp = 95
        with patch('random.randint', return_value=20):
            heal_player(self.player)
            self.assertEqual(self.player.hp, 100)

class TestEnemy(unittest.TestCase):

    def test_enemy_attack_range(self):
        enemy = Enemy("Goblin", 30, (5, 10))
        for _ in range(100):
            dmg = enemy.attack()
            self.assertTrue(5 <= dmg <= 10)


class TestRandomEvent(unittest.TestCase):

    def setUp(self):
        self.player = Player("Capy", 100, 100)

    @patch('rpg_logic.random.choice', return_value="healing")
    @patch('rpg_logic.random.randint', return_value=20)
    def test_random_event_healing(self, mock_randint, mock_choice):
        self.player.hp = 70
        random_event(self.player)
        self.assertEqual(self.player.hp, 90)

    @patch('rpg_logic.random.choice', return_value="Goblin")
    @patch('rpg_logic.battle')
    def test_random_event_enemy(self, mock_battle, mock_choice):
        configuration.ENEMIES = {
            "Goblin": {
                "hp": 30,
                "attack_range": (5, 10)
            }
        }
        random_event(self.player)
        mock_battle.assert_called_once()


if __name__ == '__main__':
    unittest.main()
