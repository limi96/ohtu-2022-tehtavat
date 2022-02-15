class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        points = self.goals + self.assists
        return_string = f"{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(points)}"
        return return_string 
