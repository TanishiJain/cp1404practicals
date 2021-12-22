class ProgrammingLanguage:

    def __init__(self, field=" ", typing=" ", reflection=" ", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} typing, Reflecton = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"