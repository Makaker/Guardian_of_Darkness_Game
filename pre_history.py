import pygame
from setting import *


class PreHistory:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(('font/PixelifySans-SemiBold.ttf'), 17)
        self.background = pygame.surface.Surface(((W//2), (H)))
        self.background_rect = self.background.get_rect()
        self.background_rect.left = 280
        self.background_rect.top = 0
        self.background_text = self.font.render('Віддавна світ охопила вічна боротьба між світлом і темрявою. '
                                                'Одного разу самотній мисливець на вампірів виявився на '
                                                'кладовищі, яке стало місцем, де зловісні сили '
                                                'випускають темряву.', True, button_text_color)
        self.background_text_rect = self.background_text.get_rect()
        self.background_text_rect.x = 250
        self.background_text_rect.y = 200

    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.background_text, self.background_text_rect)

