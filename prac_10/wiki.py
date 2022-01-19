import wikipedia


def main():
    search = input("Enter something:")
    while search != "":
        print(wikipedia.search(search))

        print(wikipedia.search(search, results=3))

        print(wikipedia.summary("GitHub"))
        search = input("Enter something:")
    else:
        pass

    monty = wikipedia.page("Monty")

    print(monty.title)
    print(monty.url)
    print(monty.summary)

    try:
        mercury = wikipedia.summary("Monty")
    except wikipedia.exceptions.DisambiguationError as t:
        print(t.options)

if __name__ == '__main__':
    main()
