class Actor:
    def __init__(self):
        self._busy = False

    def occupied(self):
        self.busy = True
        print('I am occupied!')

    def available(self):
        self.busy = False
        print('I am free!')

    @property
    def is_busy(self):
        return self._busy

    @is_busy.setter
    def is_busy(self, status):
        self._set_status(status)

    def _set_status(self, status):
        self._busy = status


class Agent:
    def __init__(self):
        self.actor = None

    def work(self):
        self.actor = Actor()
        if self.actor.is_busy:
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
