from Performance import Performance


class Ticket:
    def __init__(self, performance, seat_number, price, date):
        self.__performance: Performance = performance
        self.__performance.add_viewer()
        self.__seat_number: str = seat_number
        self.__price: float = price
        self.__date: str = date

    @property
    def performance_name(self):
        return self.__performance.name

    def delete(self):
        self.__performance.remove_viewer()
