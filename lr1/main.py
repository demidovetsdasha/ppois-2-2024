from Theatre import Theatre
from Actor import Actor
from Director import Director
from OrderService import OrderService
from Performance import Performance
from DressingRoom import DressingRoom
from Stage import Stage


def show_menu_positions():
    print("1.Add theatre")
    print("2.Add performance")
    print("3.Add actor")
    print("4.Buy ticket")
    print("5.Start performance")

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
                stage: Stage = Stage(input("Input № of stage: "))
                name = input("Input performance name: ")
                dates: list = []
                count = int(input("How many times it will be shown? "))
                for i in range(0, count):
                    dates.append(input("Input performance's date (hh:mm dd.mm.yyyy): "))
                performance: Performance = Performance(name, dates)
                performance.create_places(3, 3)
                director: Director = Director(input("Input director name: "), int(input("Input his experience years: ")))
                director.add_directed_play(performance)
                booking.show_theatres()
                index = int(input("Choose theatre for this performance: "))
                theatres[index-1].add_performance(performance, stage)
                performances.append(performance)
            case "3":
                for performance in performances:
                    print(performance.name)

                index = int(input("For which performance? "))
                actor: Actor = Actor(input("Input actor name: "), int(input("Input his age: ")))
                dressing_room.dress_actor(actor)
                role = input("Input his role: ")
                performances[index-1].add_actor(actor, role)
            case "4":
                tickets.append(booking.order_ticket())
            case "5":
                for theatre in theatres:
                    print(theatre.name)

                index = int(input("Choose theatre: ")) - 1
                theatres[index].start_performance()

        print("\033[H\033[J")
        # os.system("clear")

main()