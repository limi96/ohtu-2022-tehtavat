class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:    
    def matches():
        return True

class Not: 
    def __init__(self, match):
        self._match = match
    
    def matches(self, player):
        if self._match.matches(player):
            return False
        return True

class Or: 
    
    # def __init__(self, match_one, match_two):
    #     self._match_one = match_one
    #     self._match_two = match_two

    # def matches(self, player):
    #     statement = self._match_one.matches(player) or self._match_two.matches(player)
    #     if statement: 
    #         return True
    #     return False

    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        return False

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value