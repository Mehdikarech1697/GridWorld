import numpy as np
from collections import defaultdict


class QLearning:
    # To Do: Fill in from here !
    def __init__(self, actions):
        self.actions = actions
        
    def get_action(self, state):
        next_action = np.random.choice(self.actions)
        return next_action
