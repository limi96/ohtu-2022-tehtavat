from player_reader import PlayerReader
from player import Player
class PlayerStats:

    def __init__(self, player_reader): 
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality): 
        all_players_list = self.player_reader.get_players()
        player_list = filter(lambda player: (player.nationality == nationality), all_players_list)
        top_scores_list = sorted(player_list, key = lambda player : player.points, reverse = True)
        return top_scores_list