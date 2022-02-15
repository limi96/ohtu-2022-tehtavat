import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)
    # print(response)
    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists'],
        )

        players.append(player)

    for player in players:
        print(player)
        break

if __name__ == "__main__":
    main()

