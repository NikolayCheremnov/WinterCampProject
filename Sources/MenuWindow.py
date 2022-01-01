import arcade


class MenuWindow(arcade.Window):
    """
        Application class for menu viewing and some info about game.
    """

    def __init__(self, screen_width, screen_height, screen_title, bgcolor=arcade.csscolor.CORNFLOWER_BLUE):
        super().__init__(screen_width, screen_height, screen_title)
        arcade.set_background_color(bgcolor)

    def setup(self):
        # Set up the game here. Call this function to restart the game.
        pass

    def on_draw(self):
        # Render the screen.
        arcade.start_render()

        # Code to draw the screen goes here
