from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    list = [ruby, python, visual_basic]
    print("The dynamically typed languagues are:")
    for i in list:
        if i.is_dynamic():
            print(i.field)


main()