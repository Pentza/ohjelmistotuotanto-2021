class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score_name(self, score):
        names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
            4: "Deuce"
        }
        return names[score]

        
    def draw_results(self):
        if self.m_score1 == 4:
            return self.get_score_name(self.m_score1)
        return f'{self.get_score_name(self.m_score1)}-All'

    def get_advantage_or_win(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"


    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.draw_results()

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_advantage_or_win()
        
        return f'{self.get_score_name(self.m_score1)}-{self.get_score_name(self.m_score2)}'
