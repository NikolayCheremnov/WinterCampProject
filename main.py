import arcade

# импорт настроек окна
from GameSettings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

# импорт окон
from InitialView import InitialView

if __name__ == '__main__':
    # 1. создание первого окна arcade
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # 2. создаем начальныфй экран
    view = InitialView()
    # 3. устанавливаем начальный экран
    window.show_view(view)
    # 4. запуск приложения
    arcade.run()
