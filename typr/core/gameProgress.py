from dataclasses import dataclass
from math import floor
from .typeThingProvider import TypeType, typeThingProvider

@dataclass
class Stats:
    cpm: int = 0
    typo: int = 0
    totalChars: int = 0
    skipped:bool = False
    time:int = 0 # the time it took to complete

    def getAcc(self)->float:
        if self.typo >= self.totalChars:
          return 0
        return abs( (self.typo / self.totalChars) * 100 - 100)

    def getCWP(self)->float:
        return self.totalChars / (self.time / 60)

    def getWPM(self)->float:
        return round (self.getCWP() / 5)



class gameProgress():
    def __init__(self, provider: typeThingProvider, rounds:int = 5) -> None:
        self.rounds = rounds
        self.current_round = 0
        self.provider = provider
        self.stats = []


    def getText(self)->str:
        self.current_round +=1
        text = self.provider.getTypeThing()
        self.stats.append(Stats(0,0,len(text)))
        return text

    def isGameOver(self)->bool:
        return self.rounds == self.current_round

    def addTypo(self, count:int)->None:
        self.stats[-1].typo +=count

    def addCPM(self, cpm:int)->None:
        self.stats[-1].cpm = cpm

    def setDuration(self, time:float)->None:
        self.stats[-1].time = time

    def totalTypos(self)->int:
        total:int = 0
        for i in self.stats:
            total += i.typo
        return total

    def perfectRounds(self)->int:
        total: int = 0
        for i in self.stats:
            if i.typo == 0 and not i.skipped:
                total += 1
        return total

    def totalChars(self)->int:
        total:int = 0
        for i in self.stats:
            if not i.skipped:
                total += i.totalChars
        return total

    def averageAcc(self)->float:
        total:float = 0
        amount: int = 0
        for i in self.stats:
            if not i.skipped:
                amount += 1
                total += i.getAcc()

        if amount == 0:
            return 0

        return floor(total / amount)

    def averageCPM(self)->float:
        total:float = 0
        amount: int = 0
        for i in self.stats:
            if not i.skipped:
                amount += 1
                total += i.getCWP()

        if amount == 0:
            return 0

        return floor(total / amount)
    
    def averageWPM(self)->float:
        total:float = 0
        amount: int = 0
        for i in self.stats:
            if not i.skipped:
                amount += 1
                total += i.getWPM()

        if amount == 0:
            return 0

        return floor(total / amount)


    def currentProg(self)->str:
        return f"{self.current_round}/{self.rounds}"

    def skipRound(self)->None:
        self.stats[-1].skipped = True
