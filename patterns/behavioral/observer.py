from abc import ABCMeta, abstractmethod


class NewPublisher:
    def __init__(self):
        self.__subscribers = list()
        self.__latest_news = None

    @property
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        self.__subscribers.pop()

    @property
    def news(self):
        return self.__latest_news

    @news.setter
    def news(self, new_news):
        self._set_news(new_news)

    def _set_news(self, news):
        self.__latest_news = news

    def notify_subscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, new_publisher):
        self._set_publisher(new_publisher)

    def _set_publisher(self, new_publisher):
        self.__publisher = new_publisher
        self.__publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.news)


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, new_publisher):
        self._set_publisher(new_publisher)

    def _set_publisher(self, new_publisher):
        self.__publisher = new_publisher
        self.__publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.news)


if __name__ == '__main__':
    news_publisher = NewPublisher()

    subscribers = [SMSSubscriber, EmailSubscriber]
    for Subscriber in subscribers:
        Subscriber(news_publisher)
    print(news_publisher.subscribers)

    news_publisher.news = 'Hello world'
    news_publisher.notify_subscribers()