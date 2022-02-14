import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_not_found_in_list_is_none(self): 
        test_player = self.statistics.search("Niinistö")
        self.assertEqual(test_player, None)

    def test_found_in_list_gives_correct_player(self):
        test_player = str(self.statistics.search("Gretzky"))
        player = str(Player("Gretzky", "EDM", 35, 89))
        self.assertEqual(test_player, player)

    def test_top_score_correct(self): 
        top_list = self.statistics.top_scorers(3)
        test_player = str(top_list[0])
        player = str(Player("Gretzky", "EDM", 35, 89))
        self.assertEqual(test_player, player)
        
    def test_correct_number_of_players_by_teams(self):
        player_list = self.statistics.team("EDM")
        list_length = len(player_list)
        self.assertEqual(list_length, 3)

