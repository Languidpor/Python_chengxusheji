import pygame
class Picture:
    def __init__(self):
        self.p1 = pygame.image.load("image/1.png")
        self.p1 = pygame.transform.scale(self.p1, (25, 25))
        self.p2 = pygame.image.load("image/2.png")
        self.p2 = pygame.transform.scale(self.p2, (25, 25))
        self.p3 = pygame.image.load("image/3.png")
        self.p3 = pygame.transform.scale(self.p3, (25, 25))
        self.boom = pygame.image.load("image/红色炸弹.png")
        self.boom=  pygame.transform.scale(self.boom, (25, 25))
        self.fugai = pygame.image.load("image/覆盖.png")
        self.fugai = pygame.transform.scale(self.fugai, (25, 25))
        self.sign = pygame.image.load("image/旗子.png")
        self.sign = pygame.transform.scale(self.sign, (25, 25))






