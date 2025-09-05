import json


class translate:
    def __init__(self):
        self.path = "./dictionary.json"

        self.dictionary = self.loadFromFile() or {}

        self.wordAdded: dict
        self.contextPairs = []

    def addWord(self, word, context, meaning):
        self.contextPairs.append({context: meaning})
        pair = self.contextPairs
        self.wordAdded = {word: pair}
        del pair
        self.addWordContextPair()
        self.saveToFile()

    def findWord(self):
        pass

    def display(self):
        pass

    def saveToFile(self):
        if self.dictionary == {}:  # do not rewrite file when shit hits the fan
            print("stopped atempt to clear the file")
            return

        with open(self.path, "w") as f:
            json.dump(self.dictionary, indent=4, fp=f)

    def loadFromFile(self):
        try:
            with open(self.path, "r") as f:
                dictionary = json.load(f)
            return dictionary
        except Exception:
            pass

    def addWordContextPair(self):
        for k, v in self.wordAdded.items():
            if k in self.dictionary.keys():
                self.dictionary[k].append(v)
            else:
                self.dictionary.update(self.wordAdded)
