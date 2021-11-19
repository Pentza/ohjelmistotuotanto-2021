
class PlayerStats:
    def __init__(self, playerlist: list):
        self.players = playerlist.players

    def top_scorer_by_nationality(self, nationality: str):
        top_scorers = []
        for player in sorted(self.players, key=lambda p: p.points, reverse=True):
            if player.nationality == nationality:
                top_scorers.append(player)
        return top_scorers
