import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    print(f'Players from FIN {datetime.now()}\n')
    tuloste = f'{"name":20}{"team":12}{"goals":10}{"assists":14}{"points":10}'
    print(tuloste)
    print(len(tuloste)*'-')

    for player in sorted(players, key=lambda player: player.points, reverse=True):
        if player.nationality == 'FIN':
            print(player)
    
if __name__ == "__main__":
    main()