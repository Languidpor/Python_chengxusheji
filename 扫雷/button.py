import pygame


class Button:
        """生成图形的类"""

        def __init__(self, screen, message):
                self.screen = screen
                self.message = message
                self.screen_rect = self.screen.get_rect()
                self.font = pygame.font.SysFont(None, 48)
                self.font_color = (0, 70, 0)
                self.image = self.font.render(self.message, True, self.font_color, None)
                self.image_rect = self.image.get_rect()
                self.image_rect.center = self.screen_rect.center

        def place(self, x, y):
                self.image_rect.x = x
                self.image_rect.y = y

        def display(self):
                self.screen.blit(self.image, self.image_rect)
