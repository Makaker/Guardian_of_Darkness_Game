import pygame
import random
from setting import *


class SplashScreen:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font('font/PixelifySans-SemiBold.ttf', 60)
        self.text_color = button_text_color
        self.show_splash = True  # Новый атрибут для контроля отображения заставки

        self.shake_intensity = 2  # Интенсивность тряски
        self.shake_offset_x = 0
        self.shake_offset_y = 0

        self.image_pers_screen = pygame.image.load('images/splash_screen/splash_2.png')
        self.image_pers_screen_rect = self.image_pers_screen.get_rect()

        self.image_spider = pygame.image.load('images/splash_screen/spider.png')
        self.image_spider_speed = 4
        self.image_spider_rect = self.image_spider.get_rect()
        self.image_spider_rect.centerx = 100
        self.image_spider_rect.centery = 70

    def init_image(self):
        self.image_font = self.font.render('Guardian of Darkness', True, self.text_color)

        # диапазон тряски от -5 до 5 рандомно
        self.shake_offset_x = random.uniform(-self.shake_intensity, self.shake_intensity)
        self.shake_offset_y = random.uniform(-self.shake_intensity, self.shake_intensity)

        self.image_pers_screen_rect.centerx = W // 2
        self.image_pers_screen_rect.top = 80

        self.image_spider_rect.centery += self.image_spider_speed

        self.rect_image_font = self.image_font.get_rect()
        self.rect_image_font.left = 280 + self.shake_offset_x
        self.rect_image_font.top = 350 + self.shake_offset_y

    def blit_splash_screen(self):
        self.init_image()  # обновляем позиции заставки каждую итерацию
        self.screen.blit(self.image_font, self.rect_image_font)
        self.screen.blit(self.image_pers_screen, self.image_pers_screen_rect)
        self.screen.blit(self.image_spider, self.image_spider_rect)
