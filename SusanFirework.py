#Let your child maul your keyboard while fireworks explode on the screen
#$Id$
#Copyright (C) 2012  Fergal Mullally

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import random
import pygame
from pygame.color import Color
import math


class SusanFirework():
    #@TODO surface is set as part of init
    def __init__(self, surface, key=None):
        self.surface = surface

        x = float(min(surface.get_size()))
        x1 = int(.03*x)
        x2 = int(.05*x)
        x3 = int(.2*x)
        #Wouldn't Poisson be better?
        self.maxSize = random.randrange(x1 ,x2)
        self.bigRadius = random.randrange(x2,x3)

        self.innerRadius = 0
        self.outerRadius = 1
        speed = random.randrange(20, 30)
        self.radiusStep = int(self.maxSize/float(speed))

        red = random.randrange(64, 256, 64) #Off, on or half on
        green = random.randrange(64, 256, 64)
        blue = random.randrange(64, 256, 64)
        self.colour = Color(red, green, blue)

        (mxx, mxy) = surface.get_size()
        self.xpos = random.randrange(mxx)
        self.ypos = random.randrange(mxy)


        self._isActive = True

    def __str__(self):
        msg="Firework at (%i,%i) with size %i (%i %i %.3f)" \
            %(self.xpos, self.ypos, self.maxSize, self.innerRadius, self.outerRadius, self.radiusStep)
        return msg

    def __repr__(self):
        return __str__()

    def draw(self):

        R=self.bigRadius

        if self.outerRadius < self.maxSize:
            self.outerRadius += self.radiusStep
            #Don't let outerRadius get too big
            self.outerRadius = min(self.maxSize, self.outerRadius)
        else:
            self.innerRadius += self.radiusStep


        thetalist=[0,3.14/4,3.14/2,3*3.14/4,3.14,3*3.141/2,2*3.14]

        for i, theta in enumerate(thetalist):
            npos = [self.xpos+R*math.cos(theta), self.ypos+R*math.sin(theta)]
            pygame.draw.circle(self.surface, self.colour, npos, self.outerRadius)


        pos = [self.xpos , self.ypos]
        if self.innerRadius > 0:
            black = Color(0,0,0)
            pygame.draw.circle(self.surface, black, pos, self.innerRadius)

        if self.innerRadius > self.maxSize:
            self._isActive = False

    def isActive(self):
        return self._isActive
