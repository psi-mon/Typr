class Typr():
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        try:
          key = self.screen.getkey()
          self.state.get_event(key)
        except:
            pass
            
    def flip_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update()

    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        self.screen.nodelay(True)
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()


        
