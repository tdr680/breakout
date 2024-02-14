import pygame as pg
from game.state.base import BaseState


class StateMachine:

    def __init__(self, states=None):
        self.states = states or {}
        self.current = BaseState()

    def update(self, dt):
        self.current.update(dt)

    def draw(self) -> list:
        return self.current.draw()

    def change(self, state, param=None):
        assert self.states[state]
        self.current.exit()
        self.current = self.states[state]
        self.current.enter(param)
