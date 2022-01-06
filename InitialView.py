import arcade

from GameView import GameView


class InitialView(arcade.View):

    def on_show(self):
        # 1. установка фонового цвета начального экрана
        arcade.set_background_color(arcade.csscolor.AQUA)
        # 2. сброс настроек при перезапуске
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        # 1. рисуем экран
        arcade.start_render()
        # 2. приветственное сообщение
        arcade.draw_text('Добро пожаловать в нашу игру!',
                         self.window.width / 2, self.window.height / 2,
                         arcade.color.DRAB, font_size=24,
                         anchor_x="center")
        # вторая надпись
        arcade.draw_text('Нажмите любую клавишу чтобы начать',
                         self.window.width / 2, self.window.height / 2 - 100,
                         arcade.color.DRAB, font_size=17,
                         anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        # запуск игры
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
