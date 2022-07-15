import requests
from enum import Enum

class TypeType(Enum):
    LOCAL = 1
    EN = 2
    DE = 3
    PYTHON = 4
    TYPESCRIPT = 5
    CSHARP = 6
    SINGLECHAR = 7
    NUMBERS = 8


class typeThingProvider():
    def __init__(self, ttype:TypeType) -> None:
        self.type = ttype
        self.provider = self.__csharpProvider

        match ttype:
            case TypeType.LOCAL:
                self.provider = self.__localProvider
            case TypeType.EN:
                self.provider = self.__enProvider
            case TypeType.DE:
                self.provider = self.__deProvider
            case TypeType.PYTHON:
                self.provider = self.__pythonProvider
            case TypeType.TYPESCRIPT:
                self.provider = self.__typeScriptProvider
            case TypeType.CSHARP:
                self.provider = self.__csharpProvider
            case TypeType.SINGLECHAR:
                self.provider = self.__singleCharProvider
            case TypeType.NUMBERS:
                self.provider = self.__numbersProvider
            case _:
                self.provider = self.__singleCharProvider
        
    def __getRandomWikiSentence(self, loca: str)->str:
        titleUrl = ''
        sumUrl = ''
        sum = 'bub'
        match loca:
            case 'en':
                titleUrl = 'https://en.wikipedia.org/api/rest_v1/page/random/title'
                sumUrl = 'https://en.wikipedia.org/api/rest_v1/page/summary/'
            case 'de':
                titleUrl = 'https://de.wikipedia.org/api/rest_v1/page/random/title'
                sumUrl = 'https://de.wikipedia.org/api/rest_v1/page/summary/'
                pass
            case _:
                pass
      # get random title
        r = requests.get(titleUrl)
        if r.status_code != 200:
            raise # Custome error to display in error screen
        js = r.json()
        title = js['items'][0]['title']
        # get summary 
        r = requests.get(f"{sumUrl}{title}")
        if r.status_code != 200:
            raise # add Custome error to display in error screen
        js = r.json()
        sum = js['extract']

        # return the first sentence of the extraction
        return sum.partition('.')[0] + '.'



    def __localProvider(self)->str:
        return "Your typing some local shit"

    def __enProvider(self)->str:
        return self.__getRandomWikiSentence('en')
        #return "Your typing in english mate"

    def __deProvider(self)->str:
        return self.__getRandomWikiSentence('de')

    def __pythonProvider(self)->str:
        return "def someClass(self)"

    def __typeScriptProvider(self)->str:
        return "let fu = new Array<string>();"

    def __csharpProvider(self)->str:
        return "const fu = new AwesomeClass<int>()"

    def __singleCharProvider(self)->str:
        return "j"

    def __numbersProvider(self)->str:
        return "42"

    def getTypeThing(self)->str:
        return self.provider()
