class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.equal_names = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}
        self.advantage_names = {1:"Advantage player1", -1:"Advantage player2"}
        self.full_point = 4
        self.deuce_point = 3
        self.win_threshold = 2

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1


    def equal_score(self, current_score):

        if (current_score > self.deuce_point): 
            return "Deuce"

        return self.equal_names[current_score]+"-All"

    def advantage_score(self, minus_result): 

        if minus_result in self.advantage_names.keys(): 
            return self.advantage_names[minus_result]

        if minus_result >= self.win_threshold:
            return "Win for player1"
        else:
            return "Win for player2"


    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self.equal_score(self.m_score1)

        elif self.m_score1 >= self.full_point or self.m_score2 >= self.full_point:
            minus_result = self.m_score1 - self. m_score2
            score = self.advantage_score(minus_result)

        else:
            score = self.in_between_scores(temp_score, score)
            
        return score

    def in_between_scores(self, temp_score, score): 
        for i in range(1, self.deuce_point):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2
            score += self.equal_names[temp_score]
        return score