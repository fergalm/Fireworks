
import pygame
from pygame.locals import *
import Firework 


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
    maxObjects = 20
    while flag:
        eventList = pygame.event.get(KEYDOWN)
        pygame.event.get()  #Throw away everything else
        #print "Eventlist",
        #print eventList
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
                f = Firework.RingFirework(surface)
                objList.append(f)
            else:
                print "Max objects exceeded"

        #print "%i new fireworks => %i objects" %(len(eventList), len(objList))
        #Update fireworks
        deadList = range(len(objList))
        for i, obj in enumerate(objList):
            obj.draw()
            if obj.isActive():
                deadList[i] = 0
            else:
                deadList[i] = 1

        #Delete dead fireworks
        #print deadList
        for i in range(len(deadList)):
            if deadList[i]>0:
                objList.pop(i)
                i=0
                break #Only remove one object at a time
        #print "Object list now has %i obj" %(len(objList))

        
        pygame.display.flip()        
        pygame.time.wait(40)
        #raw_input('%i: Hit RETURN' %(j))
        j+=1

    #Tidy up
    pygame.display.quit()

if __name__ == "__main__":
    main()
