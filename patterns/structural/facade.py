class EventManager:

    def __init__(self):
        print('Event Manager: Let me talk to the folds\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier:
    def __init__(self):
        print('Arranging hotel for marriage? --\n')

    def __is_available(self):
        print('Is the hotel free for the event?\n')
        return True

    def book_hotel(self):
        if self.__is_available():
            print('Registered the booking\n')


class Florist:
    def __init__(self):
        print('Flower decoration\n')

    def set_flower_requirements(self):
        print('Roses will be used for decorations')


class Caterer:
    def __init__(self):
        print('Food arrangements for event')

    def set_cuisine(self):
        print('Chinese food')


class Musician:
    def __init__(self):
        print('Musical arrangements')

    def set_music_type(self):
        print('Jazz and classical will be played')


class Client:
    def __init__(self):
        print('I want to arrange marriage')

    def ask_event_manager(self):
        print("Let's contact event manager!")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('Thanks event manager')


client = Client()
client.ask_event_manager()