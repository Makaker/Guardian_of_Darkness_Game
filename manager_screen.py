import pygame
from main_menu import MainMenu
from splash_screen import SplashScreen
import time
from setting import *
from pre_history import PreHistory


class ManagerScreen:
    '''Класс для отрисовки рабочего экрана: заставка, меню и тд'''

    def __init__(self, screen, event_star_game = None):
        self.screen = screen
        self.screen_rect = self.screen.get_rect
        self.event_start_new_game = event_star_game

        # текущий экран
        self.current_screen = None

        self.star_splash_screen = time.time()
        self.splash_screen = SplashScreen()
        self.main_menu = MainMenu(screen)
        self.pre_history = PreHistory(screen)

        self.sound = pygame.mixer.Sound('sound/splash_screen/skrip-dvernoy-zavesyi-26762.wav')
        self.fl_sound = False

    def switch_screen(self, new_screen):
        # Метод для смены текущего экрана
        self.current_screen = new_screen

    def update(self):
        # Обновление текущего экрана
        if self.current_screen:
            self.current_screen.update()

    def set_splash_screen(self, splash_screen):
        # Метод для установки экрана заставки
        self.switch_screen(splash_screen)

    def set_pre_history_screen(self, pre_history):
        self.switch_screen(pre_history)

    # метод для выбора экрана
    def screen_selection(self):
        if self.splash_screen.show_splash:  # Проверка наличия заставки
            self.splash_screen.blit_splash_screen()
            if not self.fl_sound:
                self.sound.play()
                self.fl_sound = True

            if self.splash_screen.image_spider_rect.bottom >= H:
                self.fl_sound = False
                self.set_splash_screen(self.main_menu)
                self.splash_screen.show_splash = False

        # if self.event_start_new_game:
        #     print(self.event_start_new_game)
        #     self.set_splash_screen(self.pre_history)
        #     # self.event_start_new_game = False

    # Отрисовка текущего экрана
    def draw(self):
        # вызов функции для перехода меню
        self.screen_selection()
        if self.current_screen:
            self.current_screen.draw()



