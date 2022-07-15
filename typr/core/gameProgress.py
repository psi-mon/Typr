from dataclasses import dataclass
from .typeThingProvider import TypeType, typeThingProvider

@dataclass
class Stats:
    cpm: int = 0
    typo: int = 0


class gameProgress():
    def __init__(self, provider: typeThingProvider, rounds:int = 5) -> None:
        self.rounds = rounds
        self.current_round = 0
        self.provider = provider
        self.stats = []


    def getText(self)->str:
        self.current_round +=1
        self.stats.append(Stats())
        return self.provider.getTypeThing()

    def isGameOver(self)->bool:
        return self.rounds == self.current_round

    def addTypo(self, count:int)->None:
        self.stats[-1].typo +=count

    def addCPM(self, cpm:int)->None:
        self.stats[-1].cpm = cpm

    def totalTypos(self)->int:
        total:int = 0
        for i in self.stats:
            total += i.typo
        return total

    def currentProg(self)->str:
        return f"{self.current_round}/{self.rounds}"

