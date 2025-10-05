from lib import CLI, translate

GUI = CLI.gui()


def main():
    session = translate.translate()
    choice = input(
        "__________________\n1_find word\n2_add word\n3_remove word\n4_showAll\n>"
    )

    if choice == "q":
        return -1

    elif choice == "1":
        word = GUI.getWord()
        session.findWord(word)

    elif choice == "2":
        word = GUI.getWord()
        context = GUI.getContext(word)
        meaning = GUI.getMeaning(context)

        session.addWord(word, context, meaning)

    elif choice == "3":
        pass

    elif choice == "4":
        session.display()

    del session


while True:
    if main() == -1:
        break
