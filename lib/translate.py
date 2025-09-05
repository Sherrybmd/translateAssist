import json


class translate:
    def __init__(self):
        self.path = "./dictionary.json"

        self.dictionary = self.loadFromFile() or {}

        self.wordAdded: dict
        self.contextPairs = []
        self.dictPair: dict

    def addWord(self, word, context, meaning):
        self.dictPair = {context: meaning}
        self.contextPairs.append(self.dictPair)
        pair = self.contextPairs  # doing this because i cant pass a pointer to json
        self.wordAdded = {word: pair}
        del pair
        self.addWordContextPair()
        self.saveToFile()

    def findWord(self):
        pass

    def display(self, keyword=""):
        if keyword == "":
            for word, contextPair in self.dictionary.items():
                print("________________")
                print(f"{word}: ", end="\n    ")  # 4 indent space
                for pair in contextPair:
                    for context, meaning in pair.items():
                        print(f"{context}:  {meaning}", end="\n    ")
                print()

        else:
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
                self.dictionary[k].append(self.dictPair)
            else:
                self.dictionary.update(self.wordAdded)
