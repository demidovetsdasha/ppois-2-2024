class Actor:
    def __init__(self, name, age):
        self.__name: str = name
        self.__age: str = age
        self.__has_suite: bool = False

    @property
    def has_suite(self):
        return self.__has_suite

    def play(self, role):
        print(f"playing {role}~~")

    def dress(self):
        self.__has_suite = True
        print(f'{self.__name} now has a suite')
