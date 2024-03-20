class Place:
    def __init__(self, row, place):
        self.__row = row
        self.__place = place
        self.__is_empty = True

    @property
    def is_empty(self):
        return self.__is_empty

    def take(self):
        self.__is_empty = False

    def cancel(self):
        self.__is_empty = True

    def get_info(self):
        return f"{self.__row}:{self.__place}"
