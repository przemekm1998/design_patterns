from abc import ABCMeta, abstractmethod


class Client:
    def __init__(self):
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.pay()

    def __del__(self):
        if self.is_purchased:
            print('Payment completed')
        else:
            print('Not enough cash')


class Payment(metaclass=ABCMeta):
    """ Payment has the do_pay() method that needs to be implemented by the Proxy and
    RealSubject. """

    @abstractmethod
    def pay(self):
        pass


class BankTransfer(Payment):
    """ Bank has multiple methods to process the payment. The setCard() method is
    used by the Proxy to send the debit card details to the bank."""

    def __init__(self):
        self._card = None
        self.account = None

    @property
    def __account(self):
        self.account = self.card
        return self.account

    def __has_funds(self):
        print('Checking if user has funds')
        return True

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, new_card):
        self._set_card(new_card)

    def _set_card(self, new_card):
        self._card = new_card

    def pay(self):
        if self.__has_funds():
            print('Payment in process')
            return True
        else:
            print('Not enough funds')
            return False


class DebitCard(Payment):
    """ The DebitCard class is the Proxy here. When You wants to make a payment, it
     calls the do_pay() method. This is because You doesn’t want go to the bank to
     withdrawmoney and pay the merchant. """

    def __init__(self):
        self.bank = BankTransfer()

    def pay(self):
        card = input('Proxy:: Put in card number: ')
        self.bank.card = card
        return self.bank.pay()


if __name__ == '__main__':
    client = Client()
    client.make_payment()
