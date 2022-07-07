class BaseState():
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.persist = {}

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass
