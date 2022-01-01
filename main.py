import arcade

from Sources.GameSettings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from Sources.Views.InitialView import InitialView

if __name__ == '__main__':
    # test screen viewing
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = InitialView()
    window.show_view(view)
    arcade.run()
