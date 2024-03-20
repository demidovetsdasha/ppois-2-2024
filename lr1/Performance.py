from Audience import Audience
from Place import Place


class Performance:
    def __init__(self, name, dates):
        self.__name: str = name
        self.__audience: Audience = Audience()
        self.__actors_group: dict = {}
        self.__places: list = []
        self.__dates: list[str] = dates

    @property
    def name(self):
        return self.__name

    @property
    def audience_count(self):
        return self.__audience.count

    @property
    def actors_count(self):
        return len(self.__actors_group)

    def __play(self):
        for actor, role in self.__actors_group.items():
            actor.play(role)

    def start(self):
        self.__play()
        self.__audience.rest()
        self.__play()
        print('The end.')

    def add_actor(self, actor, role):
        self.__actors_group[actor] = role

    def remove_actor(self, actor):
        self.__actors_group.pop(actor)

    def add_viewer(self):
        self.__audience.add()

    def remove_viewer(self):
        self.__audience.remove()

    def get_place(self, index):
        self.__places[index].take()
        return self.__places[index].get_info()

    def get_date(self, index):
        return self.__dates[index]

    def create_places(self, row : int, column : int):
        for i in range(0, row):
            for j in range(0, column):
                place = Place(i+1, j+1)
                self.__places.append(place)

    def show_places(self):
        for place in self.__places:
            print(place.get_info())

    def show_dates(self):
        for date in self.__dates:
            print(date)
