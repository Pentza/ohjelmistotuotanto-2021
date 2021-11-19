from playerReader import PlayerReader
from playerStats import PlayerStats
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorer_by_nationality('FIN')

    print(f'Players from FIN {datetime.now()}')
    tuloste = f'{"name":20}{"team":12}{"goals":10}{"assists":14}{"points":10}'
    print(tuloste)
    print(len(tuloste)*'-')

    for player in players:
        print(player)
    
if __name__ == "__main__":
    main()