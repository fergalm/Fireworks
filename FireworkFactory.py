
from RingFirework import RingFirework
from SquareFirework import SquareFirework

import random

class FireworkFactory():
    def __init__(self):
        pass

    def newFirework(self, pygameSurface, key=None):
        """Key can be used to pass the key pressed"""
        val = random.randrange(2)

        if val == 0:
            return RingFirework(pygameSurface)
        elif val == 1:
            return SquareFirework(pygameSurface)
