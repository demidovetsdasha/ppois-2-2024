class Stage:
    def __init__(self, stage_number):
        self.__stage_number: int = stage_number
        self.__is_taken: bool = False

    @property
    def number(self):
        return self.__stage_number

    def is_available(self):
        return self.__is_taken is False

    def take_stage(self):
        self.__is_taken = True

    def make_stage_free(self):
        self.__is_taken = False

    def practice(self):
        self.take_stage()
        print("practicing now~~")
        self.make_stage_free()
