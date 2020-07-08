from typing import List


class ComputerState:
    name: str = 'state'
    allowed: List[str] = list()

    def switch(self, state: 'ComputerState'):
        if state.name in self.allowed:
            print(f'Current: {self.name} -> {state.name}')
            self.__class__ = state
        else:
            print('Not possible')

    def __str__(self) -> str:
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspended']


class Suspended(ComputerState):
    name = 'suspended'
    allowed = ['on']
