class BaseState:

    def enter(self, param=None):
        pass

    def exit(self):
        pass

    def update(self, dt):
        pass

    def draw(self) -> list:
        pass
