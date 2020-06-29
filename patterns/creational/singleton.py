import sqlite3

"""
Singleton:
    - one and only one object created
    - access point for object that is global for program
    - concurrent access control

    i.e. Database object
"""


class Singleton(type):
    """
    Pros

    It's a true class
    Auto-magically covers inheritance
    Uses __metaclass__ for its proper purpose (and made me aware of it)

    Cons

    Are there any?
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


class MonostateSignleton:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


class Database(metaclass=Singleton):
    """
    When the web app wants to perform certain operations on the DB, it instantiates the
    database class multiple times, but only one object gets created. As there is only one
    object, calls to the database are synchronized. Additionally, this is inexpensive on
    system resources and we can avoid the situation of memory or CPU resource.

    Consider that instead of having one webapp, we have a clustered setup with multiple web
    apps but only one DB. Now, this is not a good situation for Singletons because, with every
    web app addition, a new Singleton gets created and a new object gets added that queries
    the database. This results in unsynchronized database operations and is heavy on
    resources. In such cases, database connection pooling is better than implementing
    Singletons.
    """

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is None:
            self.instantiate_connection()

        return self.cursor

    def instantiate_connection(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
