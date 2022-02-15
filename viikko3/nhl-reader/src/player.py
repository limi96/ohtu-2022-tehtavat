class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.points = goals + assists

    def get_nationality(self):
        return self.nationality
    
    def __str__(self):
        # points = self.goals + self.assists
        # return_string = f"{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(points)}"
        return_string = f"{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(self.points)} {self.nationality}"
        return return_string 
