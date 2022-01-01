import arcade
import arcade.gui


class MainMenuView(arcade.View):
    """ Initial view screen """

    def __init__(self):
        super().__init__()

        # UI manger
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        # creating buttons
        start_button = arcade.gui.UIFlatButton(text='Start Game', width=200)
        about_button = arcade.gui.UIFlatButton(text='About', width=200)
        exit_button = arcade.gui.UIFlatButton(text='Exit', width=200)

        # handlers binding
        exit_button.on_click = self.on_exit_button_click

        # buttons box layout
        box = arcade.gui.UIBoxLayout()
        box.add(start_button.with_space_around(bottom=20))
        box.add(about_button.with_space_around(bottom=20))
        box.add(exit_button.with_space_around(bottom=20))

        # add box to UI manager
        self.uimanager.add(arcade.gui.UIAnchorWidget(anchor_x='center_x', anchor_y='center_y', child=box))

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.PALE_TURQUOISE)

    def on_draw(self):
        """ View drawing """
        arcade.start_render()
        # title
        arcade.draw_text("<GAME NAME>", self.window.width / 2, self.window.height - 100,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        # buttons drawing
        self.uimanager.draw()

    """
        Buttons handlers
    """

    def on_exit_button_click(self, event):
        # 1. creating message box
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=200,
            message_text='You really want to exit?',
            callback=self.on_message_box_close,
            buttons=["Yes", "No"]
        )
        # 2. add this to UI
        self.uimanager.add(message_box)

    def on_message_box_close(self, reply):
        # exit only if user want it
        if reply == 'Yes':
            arcade.exit()
