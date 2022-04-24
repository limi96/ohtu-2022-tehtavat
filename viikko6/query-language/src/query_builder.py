from matchers import *

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(matcher=And(self._matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(matcher=And(self._matcher, HasFewerThan(value, attr)))

    def playsIn(self, team):
        return QueryBuilder(matcher=And(self._matcher, PlaysIn(team)))

    def oneOf(self, *matchers): 
        return QueryBuilder(matcher=Or(*matchers))

    def build(self): 
        return self._matcher