import arcade

from Sources.Views.MainMenuView import MainMenuView


class InitialView(arcade.View):
    """ Initial view screen """

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        # reseting
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ View drawing """
        arcade.start_render()
        arcade.draw_text("Welcome to <GAME NAME>", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press any key to continue ...", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        menu_view = MainMenuView()
        # need setup menu window here
        self.window.show_view(menu_view)

