from os import system


class gui:
    def __init__(self):
        pass

    def getWord(self):
        word = input("Write the word: \n>")
        return word

    def getContext(self, word: str):
        try:
            context = input(f"give context for {word}:\n>")
            system("clear")
            return context
        except Exception as e:
            print("error in getContext exec")
            print(e)
            raise

    def getMeaning(self, context: str):
        try:
            meaning = input(f"give meaning in this context: {context}:\n>")
            system("clear")
            return meaning
        except Exception as e:
            print("error in getMeaning exec")
            print(e)
            raise
