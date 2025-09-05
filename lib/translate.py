import json


class translate:
    def __init__(self):
        self.path = "./dictionary.json"
        self.wordAdded = ""

    def addWord(self, word, context, meaning):
        self.wordAdded = {word: {context: meaning}}
        self.saveToFile()

    def findWord(self):
        pass

    def display(self):
        pass

    def saveToFile(self):
        with open(self.path, "a+") as f:
            json.dump(self.wordAdded, indent=4, fp=f)

    def loadFromFile(self):
        pass

    def checkForDupe(self):
        pass
