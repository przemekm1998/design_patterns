from abc import abstractmethod, ABCMeta


class Trip(metaclass=ABCMeta):

    @abstractmethod
    def _set_transport(self):
        pass

    @abstractmethod
    def _day_1(self):
        pass

    @abstractmethod
    def _day_2(self):
        pass

    @abstractmethod
    def _return_home(self):
        pass

    def take_trip(self):
        self._set_transport()
        self._day_1()
        self._day_2()
        self._return_home()


class VeniceTrip(Trip):
    def _set_transport(self):
        print("Take a boat")

    def _day_1(self):
        print("Visiting Basilica")

    def _day_2(self):
        print("Visiting Palace")

    def _return_home(self):
        print("Get souvenirs and get back")


class MaldivesTrip(Trip):
    def _set_transport(self):
        print("On foot on any island")

    def _day_1(self):
        print("Enjoy marine")

    def _day_2(self):
        print("Water sports")

    def _return_home(self):
        print("Don't feel like leaving the beach")


class TravelAgency:

    def __init__(self):
        self._trip: Trip = VeniceTrip()

    @property
    def trip(self) -> Trip:
        return self._trip

    @trip.setter
    def trip(self, place: str):
        self._set_trip(place)

    def _set_trip(self, place: str):
        if place == 'historical':
            self._trip = VeniceTrip()
        elif place == 'beach':
            self._trip = MaldivesTrip()
        else:
            print("We don't have such offer, Venice is default")

    def arrange_trip(self):
        choice: str = input("What kind of place you'd like to go?")

        self.trip = choice
        self.trip.take_trip()


if __name__ == '__main__':
    agency = TravelAgency()
    agency.arrange_trip()
