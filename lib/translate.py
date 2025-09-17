import json


class translate:
    def __init__(self):
        self.path = "./dictionary.json"
        self.dictionary = self.loadFromFile() or {}
        # format is -> { word : [{contextOne : meaningOne}, {contextTwo : meaningTwo}] }
        self.wordAdded: dict
        self.cmDictPair: dict
        self.cmPairContainer = []

    def addWord(self, word, context, meaning):
        self.cmDictPair = {context: meaning}
        self.cmPairContainer.append(self.cmDictPair)
        tcontainer = self.cmPairContainer
        # ^^^ doing this because i cant pass a pointer to json
        self.wordAdded = {word: tcontainer}
        del tcontainer
        self.addWordContextPair()
        self.saveToFile()

    def findWord(self, word):
        for k, v in self.dictionary.items():  # reminder that v is a list of dicts
            try:
                if k == word:
                    print(word, ":", sep="")
                    for item in v:
                        txt = ", ".join(
                            f"{key}: {value}" for key, value in item.items()
                        )
                        print("   ", txt)

                else:
                    print("word not found")
            except Exception as e:
                print("Error finding word,", e)

    def display(self):
        pass

    def saveToFile(self):
        try:
            if self.dictionary == {} or self.dictionary is None:
                # do not rewrite file when shit hits the fan
                raise Exception

            with open(self.path, "w") as f:
                json.dump(self.dictionary, indent=4, fp=f)

        except Exception:
            print("Aborted saving tofile, empty dictionary:")

    def loadFromFile(self):
        try:
            with open(self.path, "r") as f:
                dictionary = json.load(f)
            return dictionary

        except Exception as e:
            print("error reading dictionary from file: ", e)

    def addWordContextPair(self):
        try:
            for k, v in self.wordAdded.items():
                # if word exists, add context meaning pair to word
                if k in self.dictionary.keys():
                    self.dictionary[k].append(self.cmDictPair)
                else:
                    # adds a whole new word and context meaning pair
                    self.dictionary.update(self.wordAdded)

        except Exception as e:
            print("Failure to add pair to dictionary: ", e)
