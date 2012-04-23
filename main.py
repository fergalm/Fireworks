#Fireworks
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


import pygame
from pygame.locals import *
from FireworkFactory import FireworkFactory

#Todo:
#x Fix leftovers
#x Fix popping
#o An svnid tag equivalent

#Note this is development code, and not intended for general use
#It probably won't do anything bad to your computer, but I make
#no promises.
#Use [ESC] the [Y] to quit

def main():
    pygame.init()
    #Find screen size and pass to this function
    screenSize=pygame.display.list_modes()[0]
    window = pygame.display.set_mode(screenSize, FULLSCREEN)
    #window = pygame.display.set_mode((640,480))    #Useful for debugging
    pygame.display.set_caption('Fireworks!')

    surface = pygame.display.get_surface()

    j=0
    t1= 0
    flag, flag2 =True, False
    objList = []
    maxObjects = 40
    factory = FireworkFactory()
    while flag:
        eventList = pygame.event.get(KEYDOWN)
        pygame.event.get()  #Throw away everything else
        for e in eventList:
            if e.key == K_ESCAPE:
                flag2 = True
                t1 = pygame.time.get_ticks()
                font = pygame.font.SysFont("Courier New", 18)
                s = font.render("Hit [Y] to Quit", 1, pygame.color.Color(255, 255, 255))
                surface.blit(s , (100, 100))

            if flag2:
                #Quit if K_Y pressed within 5 seconds of flag2 being
                #raised, otherwise unset flag2
                if e.key == K_y:
                    flag = False
                elif pygame.time.get_ticks() - t1 > 5000:
                    flag2 = False

            if len(objList) < maxObjects:
                f = factory.newFirework(surface, e.key)
                objList.append(f)
                #print f
            else:
                print "Max objects (%i) exceeded" %(maxObjects)

        for i, obj in enumerate(objList):
            obj.draw()
            if not obj.isActive():
                objList.pop(i)


        pygame.display.flip()
        pygame.time.wait(40)
        #raw_input('%i: Hit RETURN' %(j))
        j+=1

    #Tidy up
    pygame.display.quit()

if __name__ == "__main__":
    main()
