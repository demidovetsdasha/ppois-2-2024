import unittest
from Theatre import Theatre
from Actor import Actor
from Director import Director
from Ticket import Ticket
from OrderService import OrderService
from Place import Place
from Performance import Performance
from DressingRoom import DressingRoom
from Stage import Stage


class TestDirector(unittest.TestCase):
    def setUp(self):
        self.director1 = Director("George Konevsky", 25)

    def test_directed_plays(self):
        performance = Performance("Harry Potter", ["11:30 11.04.2024"])
        self.director1.add_directed_play(performance)
        self.assertEqual(self.director1.directed_plays_count, 1)


class TestDressingRoom(unittest.TestCase):
    def setUp(self):
        self.dressing_room = DressingRoom()

    def test_dress_actor(self):
        actor = Actor("Ivan", 10)
        self.assertFalse(actor.has_suite)
        self.dressing_room.dress_actor(actor)
        self.assertTrue(actor.has_suite)


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place1 = Place(1, 4)

    def test_take_place(self):
        self.place1.take()
        self.assertFalse(self.place1.is_empty)

    def test_cancel_place(self):
        self.place1.cancel()
        self.assertTrue(self.place1.is_empty)


class TestStage(unittest.TestCase):
    def setUp(self):
        self.stage1 = Stage(15)

    def test_take_stage(self):
        self.stage1.take_stage()
        self.assertFalse(self.stage1.is_available())


    def test_make_stage_free(self):
        self.stage1.make_stage_free()
        self.assertTrue(self.stage1.is_available())


class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.actor1 = Actor('Лидия', 34)
        self.actor2 = Actor('Аркадий', 19)
        self.actor3 = Actor('Кристина', 22)
        self.director = Director('Райан', 55)
        self.performance = Performance('Лебединое озеро', ["10:00 10.10.2004"])

    def test_add(self):
        self.performance.add_actor(self.actor1, 'белый лебедь')
        self.performance.add_actor(self.actor2, 'принц')
        self.performance.add_actor(self.actor3, 'черный лебедь')
        self.assertEqual(self.performance.actors_count, 3)

    def test_remove(self):
        self.performance.add_actor(self.actor3, 'черный лебедь')
        self.assertEqual(self.performance.actors_count, 1)
        self.performance.remove_actor(self.actor3)
        self.assertEqual(self.performance.actors_count, 0)


class TestTicketAndOrderService(unittest.TestCase):

    def setUp(self):
        self.dates = ["11:11 11.04.2024", "12:10 12.05.2024"]
        self.performance = Performance('Сдача лабораторной', self.dates)
        self.performance.create_places(3, 3)
        self.stage = Stage(1)
        self.theatre = Theatre("Большой театр", "ул. Розовая, 31")
        self.theatre.add_performance(self.performance, self.stage)
        self.theatres: list = []
        self.theatres.append(self.theatre)
        self.order_service: OrderService = OrderService(self.theatres)

    def test_order(self):
        self.ticket: Ticket = self.order_service.order_ticket()
        self.assertEqual(self.ticket.performance_name, self.performance.name)


if __name__ == "__main__":
 unittest.main()