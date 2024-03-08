import pygame
from setting import *
from button import Button


class MainMenu:
    # Добавляем три наших кнопки из основного меню
    def __init__(self, screen):
        self.screen = screen
        self.rect_screen = self.screen.get_rect
        self.button_new_game = Button(self.screen, (W // 2) - 100, (H - (H - 100)), 'New game',
                                      'images/button/start1.png',
                                      'images/button/start2.png',
                                      'font/PixelifySans-SemiBold.ttf')
        self.button_load_game = Button(self.screen, (W // 2) - 100, (H - (H - 210)), 'Load game',
                                       'images/button/start1.png',
                                       'images/button/start2.png',
                                       'font/PixelifySans-SemiBold.ttf')
        self.button_exit_game = Button(self.screen, (W // 2) - 100, (H - (H - 320)), 'Exit game',
                                       'images/button/start1.png',
                                       'images/button/start2.png',
                                       'font/PixelifySans-SemiBold.ttf')
    # интересный момент - функция для возврата списка конопок
    def get_buttons(self):
        return [self.button_new_game, self.button_load_game, self.button_exit_game]

    # отрисовка кнопок по их состоянию
    def draw(self):
        # Метод для отрисовки текущего экрана (в данном случае, меню)
        self.screen.fill(bg_color_star)

        self.button_new_game.check_hover(pygame.mouse.get_pos())
        self.button_new_game.drow()

        self.button_load_game.check_hover(pygame.mouse.get_pos())
        self.button_load_game.drow()

        self.button_exit_game.check_hover(pygame.mouse.get_pos())
        self.button_exit_game.drow()
