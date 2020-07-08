from abc import ABCMeta, abstractmethod
from typing import List, TypeVar


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class NewPublisher:
    def __init__(self):
        self.__subscribers: List[Subscriber] = list()
        self.__latest_news: str = ''

    @property
    def subscribers(self) -> List[str]:
        subscribers_list: List[str]
        subscribers_list = [type(x).__name__ for x in self.__subscribers]

        return subscribers_list

    def attach(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        self.__subscribers.pop()

    @property
    def news(self) -> str:
        return self.__latest_news

    @news.setter
    def news(self, new_news: str):
        self._set_news(new_news)

    def _set_news(self, news: str):
        self.__latest_news = news

    def notify_subscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()


class SMSSubscriber(Subscriber):
    def __init__(self, publisher: NewPublisher):
        self.publisher: NewPublisher = publisher

    @property
    def publisher(self) -> NewPublisher:
        return self.__publisher

    @publisher.setter
    def publisher(self, new_publisher: NewPublisher):
        self._set_publisher(new_publisher)

    def _set_publisher(self, new_publisher: NewPublisher):
        self.__publisher = new_publisher
        self.__publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.news)


class EmailSubscriber(Subscriber):
    def __init__(self, publisher: NewPublisher):
        self.publisher: NewPublisher = publisher

    @property
    def publisher(self) -> NewPublisher:
        return self.__publisher

    @publisher.setter
    def publisher(self, new_publisher: NewPublisher):
        self._set_publisher(new_publisher)

    def _set_publisher(self, new_publisher: NewPublisher):
        self.__publisher = new_publisher
        self.__publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.news)


if __name__ == '__main__':
    news_publisher = NewPublisher()

    S = TypeVar(Subscriber)
    subscribers: List[S] = [SMSSubscriber, EmailSubscriber]
    for Subscriber in subscribers:
        Subscriber(news_publisher)
    print(news_publisher.subscribers)

    news_publisher.news = 'Hello world'
    news_publisher.notify_subscribers()
