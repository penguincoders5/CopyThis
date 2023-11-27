#Fruit.py
import pygame, math

GRAVITY = 0.05
LOSS = 1.5

FLOOR = 450

SIZES = {
    1:10,
    2:25,
    3:30,
    4:40,
    5:50
}
COLORS = {
    1: (0, 255, 255),
    2: (255, 0, 255),
    3: (118, 167, 219),
    4: (78, 242, 102),
    5: (242, 187, 78)
}

class Fruit:
    def __init__(self, screen, pos, id):
        self.x = pos[0]
        self.y = 0
        self.id = id
        self.screen = screen
        self.c = (255, 255, 0)
        self.r = SIZES[id]
        self.yspeed = 0
        self.xspeed = 0
        self.update()

    def update(self):
        self.yspeed += GRAVITY


        self.collision()
        self.y += self.yspeed
        self.x += self.xspeed
        pygame.draw.circle(self.screen, self.c, (self.x, self.y), self.r, 0)

    def collision(self):
        if self.y + self.r > FLOOR:
            self.yspeed *= -1
            self.yspeed += LOSS
            self.yspeed = min(0, self.yspeed)


    def ballCollision(self, circle):
        distance = math.sqrt((circle.x - self.x)**2 + (circle.y - self.y)**2)
        if distance <= self.r + circle.r:
            if self.id == circle.id:
                self.id += 1
                self.c = COLORS[self.id]
                self.r = SIZES[self.id]
                return True


