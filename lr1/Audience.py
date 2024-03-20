class Audience:
    def __init__(self):
        self.__count: int = 0

    @property
    def count(self):
        return self.__count

    def rest(self):
        print('antract now~~')

    def add(self):
        self.__count += 1

    def remove(self):
        self.__count -= 1
