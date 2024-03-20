from Performance import Performance
from Theatre import Theatre
from Ticket import Ticket
from Place import Place


class OrderService:
    def __init__(self, theatres):
        self.__ticket_prices = [5, 20, 15]
        self.__theatres = theatres

    def show_theatres(self):
        for i in range(0, len(self.__theatres)):
            print(f"{i + 1}.{self.__theatres[i].name}")

    def __show_price(self):
        print("1. Детский\n2. Взрослый\n3. Студенческий")

    def __choose_theatre(self):
        print('Выберите театр:')
        self.show_theatres()
        index = int(input())
        return self.__theatres[index-1]

    def __choose_performance(self, theatre):
        print('Выберите спектакль:')
        theatre.show_afisha()
        index = int(input())
        return theatre.get_performance(index-1)

    def __choose_place(self, performance):
        print('Выберите место:')
        performance.show_places()
        index = int(input())
        return performance.get_place(index-1)

    def __choose_price(self):
        print('Выберите тип билета:')
        self.__show_price()
        index = int(input())
        return self.__ticket_prices[index-1]

    def __choose_date(self, performance):
        print('Выберите дату представления:')
        performance.show_dates()
        index = int(input())
        return performance.get_date(index - 1)

    def order_ticket(self):
        theatre: Theatre = self.__choose_theatre()
        performance: Performance = self.__choose_performance(theatre)
        place: Place = self.__choose_place(performance)
        price: int = self.__choose_price()
        date: str = self.__choose_date(performance)

        ticket: Ticket = Ticket(performance, place, price, date)

        return ticket

    def return_ticket(self, ticket):
        ticket.delete()
