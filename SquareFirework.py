import random
import pygame
from pygame.color import Color


class SquareFirework():
    def __init__(self, surface):
        self.surface = surface

        x = min(surface.get_size())
        self.maxSize = random.randrange( int(.18*x), int(.25*x))

        self.innerRadius = 0
        self.outerRadius = 1
        speed = random.randrange(20, 30)
        self.radiusStep = int(self.maxSize/float(speed))

        red = random.randrange(64, 256, 64)
        green = random.randrange(64, 256, 64)
        blue = random.randrange(64, 256, 64)
        self.colour = Color(red, green, blue)
        self.colour = Color(255, 20, 147)   #Deep pink

        (mxx, mxy) = surface.get_size()
        self.xpos = random.randrange(mxx) - .5*self.maxSize
        self.ypos = random.randrange(mxy) - .5*self.maxSize
        self._isActive = True

    def __str__(self):
        msg="Square at (%i,%i) with size %i" \
            %(self.xpos, self.ypos, self.maxSize)
        return msg

    def __repr__(self):
        return __str__()

    def draw(self):
        if self.outerRadius < self.maxSize:
            self.outerRadius += self.radiusStep
        else:
            self.innerRadius += self.radiusStep

        size = self.outerRadius
        left = self.xpos - .5*size
        top = self.ypos - .5*size

        rect = pygame.Rect((left, top), (size, size))

        self.surface.fill(self.colour, rect)

        if self.innerRadius > 0:
            size = self.innerRadius
            left = self.xpos - .5*size
            top = self.ypos - .5*size
            rect = pygame.Rect((left, top), (size, size))
            black= Color(0,0,0)
            self.surface.fill(black, rect)

        if self.innerRadius > self.maxSize+1:
            self._isActive = False

    def isActive(self):
        return self._isActive

