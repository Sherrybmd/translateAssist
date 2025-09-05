from lib import CLI, translate

GUI = CLI.gui()


def main():
    session = translate.translate()
    choice = input("__________________\n1_find word\n2_add word\n3_remove word\n>")

    if choice == "q":
        return

    elif choice == "1":
        pass

    elif choice == "2":
        word = GUI.getWord()
        context = GUI.getContext(word)
        meaning = GUI.getMeaning(context)

        session.addWord(word, context, meaning)

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    print(session.dictionary)
    del session


while True:
    main()
