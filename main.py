from Sources.GameSettings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from Sources.MenuWindow import MenuWindow

if __name__ == '__main__':
    # test screen viewing
    window = MenuWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    window.run()
