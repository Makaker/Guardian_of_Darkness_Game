import pygame
from button import *
from main_menu import MainMenu
from manager_screen import ManagerScreen
from pre_history import PreHistory


class EventManagement:
    '''отслеживает все события'''
    def __init__(self, screen, buttons):
        self.buttons = buttons  # cписок кнопок
        self.screen = screen
        self.sound_button = pygame.mixer.Sound('sound/button/botton_down2.wav') # звук при нажатии
        self.main_menu = MainMenu(self.screen)
        self.start_new_game = False  # переменная для сигнала о начале новой игры
        self.new_game_button_pressed = False  # Новая переменная для отслеживания нажатия на кнопку "New game"
        self.manager_screen = ManagerScreen(screen, self.start_new_game)
        self.pre_history = PreHistory(screen)

    def main_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # отслеживание событий при нажатой левой клавиши мыши
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # принимаем кнопки и отслеживаем их состояние
                for button in self.buttons:
                    # приверяем наведение мыши на кнопку с кординатыми
                    if button.check_hover(pygame.mouse.get_pos()):
                        # если совпадает, запуск музыки
                        self.sound_button.play()
                    # запускаем метод наведения на кнопку и проверяем , запускаем мелодию, делаем задержку и выходим
                    if button.check_exit(pygame.mouse.get_pos()):
                        self.sound_button.play()
                        pygame.time.delay(int(self.sound_button.get_length() * 1000))
                        pygame.quit()
                        exit()
                        # если наведено на новую игру
                    if button.check_new_game(pygame.mouse.get_pos()):
                        self.start_new_game = True
                        self.new_game_button_pressed = True  # Установка си
        # Сброс флага нажатия кнопки "New game" после обработки событий
        if self.new_game_button_pressed:
            self.new_game_button_pressed = False

        if self.start_new_game:
            # Обработка события начала новой игры
            self.manager_screen.set_splash_screen(
                self.pre_history)  # Здесь вы можете изменить на экран предистории или другой
            print('!!!!!!!!!!!!!!')
            self.start_new_game = False  # Сброс флага начала новой игры


    def play_button_sound(self):
        self.sound_button.play()
