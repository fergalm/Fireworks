class SquareFirework():
    def __init__(self, surface):
        self.surface = surface

        x = min(surface.get_size())
        self.maxSize = random.gauss( int(.18*x), int(.125*x))

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
        msg="Firework at (%i,%i) with size %i" \
            %(self.xpos, self.ypos, self.maxSize)
        return msg

    def __repr__(self):
        return __str__()

    def draw(self):
        if self.outerRadius < self.maxSize:
            self.outerRadius += self.radiusStep
        else:
            self.innerRadius += self.radiusStep

        pos = [self.xpos, self.ypos]
        rect = pygame.Rect((left, top), (width, height)):
        self.surface.fill(elf.colour, rect)

        if self.innerRadius > 0:
            black = Color(0,0,0)
            pygame.draw.circle(self.surface, black, pos, self.innerRadius)

        if self.innerRadius > self.maxSize+1:
            self._isActive = False

    def isActive(self):
        return self._isActive

