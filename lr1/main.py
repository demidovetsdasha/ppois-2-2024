from Theatre import Theatre
from Actor import Actor
from Director import Director
from OrderService import OrderService
from Performance import Performance
from DressingRoom import DressingRoom
from Stage import Stage


def show_menu_positions():
    print("Available operations:")
    print("1.Add theatre")
    print("2.Add performance")
    print("3.Add actor")
    print("4.Practice before performance")
    print("5.Buy ticket")
    print("6.Start performance")

def show_price():
    print("1. Children\n2. Adult\n3. Student")

def show(spisok):
    index: int = 1
    for item in spisok:
        print(f'{index}. {item.name}')
        index += 1

def is_empty(spisok : list):
    return len(spisok) == 0

def choose_theatre(theatres):
    print('Choose theatre:')
    show(theatres)                                  
    index = int(input())
    return theatres[index - 1]

def choose_performance(theatre):
    print('Choose performance:')
    theatre.show_afisha()
    index = int(input())
    return theatre.get_performance(index - 1)

def choose_place(performance):
    print('Choose place:')
    performance.show_places()
    index = int(input())
    return performance.get_place(index - 1)

def choose_price():
    print('Choose type of ticket:')
    show_price()
    index = int(input())
    ticket_prices = [5, 20, 15]
    return ticket_prices[index - 1]

def choose_date(performance):
    print("Choose performance's date:")
    performance.show_dates()
    index = int(input())
    return performance.get_date(index - 1)


def main():
    theatres: list = []
    tickets: list = []
    performances: list = []
    booking: OrderService = OrderService(theatres)
    dressing_room = DressingRoom()

    while(True):
        show_menu_positions()
        match input():
            case "1":
                theatre: Theatre = Theatre(input("Input name: "), input("Input location: "))
                theatres.append(theatre)
            case "2":
                if is_empty(theatres):
                    print("\033[H\033[J")
                    continue 

                stage: Stage = Stage(input("Input № of stage: "))
                name = input("Input performance name: ")
                dates: list = []
                try:
                    count = int(input("How many times it will be shown? "))
                except ValueError:
                    count = 1

                for i in range(0, count):
                    dates.append(input("Input performance's date (hh:mm dd.mm.yyyy): "))
                performance: Performance = Performance(name, dates)
                performance.create_places(3, 3)
                director: Director = Director(input("Input director name: "), int(input("Input his experience years: ")))
                director.add_directed_play(performance)

                show(theatres)
                try:
                    index = int(input("Choose theatre for this performance: "))
                except ValueError:
                    index = 1
                theatres[index-1].add_performance(performance, stage)
                performances.append(performance)
            case "3":
                if is_empty(theatres):
                    print("\033[H\033[J")
                    continue 

                if is_empty(performances):
                    print("\033[H\033[J")
                    continue 

                show(performances)
                try:
                    index = int(input("Choose performance: "))
                except ValueError:
                    index = 1

                actor: Actor = Actor(input("Input actor name: "), int(input("Input his/her age: ")))
                dressing_room.dress_actor(actor)
                role = input("Input his/her role: ")
                performances[index-1].add_actor(actor, role)
            case "4":
                if is_empty(theatres):
                    continue 

                if is_empty(performances):
                    continue

                show(theatres)
                try:
                    index_theatre = int(input("Choose theatre: ")) - 1
                except ValueError:
                    index_theatre = 1

                show(performances)
                try:
                    index_performance = int(input("Choose performance: ")) - 1
                except ValueError:
                    index_performance = 1

                theatres[index_theatre].get_stage(theatres[index_theatre].performances[index_performance]).practice()
            case "5":
                if is_empty(theatres):
                    print("\033[H\033[J")
                    continue 

                if is_empty(performances):
                    print("\033[H\033[J")
                    continue

                theatre_index: int = choose_theatre(theatres)
                performance_index: int = choose_performance(theatres[theatre_index])
                place_index: int = choose_place(performances[performance_index])
                price_index: int = choose_price()
                date_index: int = choose_date(performances[performance_index])

                tickets.append(booking.order_ticket(theatre_index, performance_index, place_index, price_index, date_index))
            case "6":
                if is_empty(theatres):
                    print("\033[H\033[J")
                    continue

                show(theatres)
                try:
                    index = int(input("Choose theatre: ")) - 1
                except ValueError:
                    index = 1

                theatres[index].start_performance()

        print("\033[H\033[J")


main()
