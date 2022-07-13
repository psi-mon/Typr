
from .typeThingProvider import TypeType, typeThingProvider

class gameProgress():
    def __init__(self, provider: typeThingProvider, rounds:int = 10) -> None:
        self.rounds = rounds
        self.provider = provider
        self.stats = []


    def getText(self)->str:
        self.rounds -=1
        return self.provider.getTypeThing()

    def isGameOver(self)->bool:
        return self.rounds == 0

    def addStat(self, cpm:int, typo:int):
        self.stats.append({cpm,typo})
