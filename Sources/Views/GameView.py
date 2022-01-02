import arcade

from Sources.GameSettings import CHARACTER_SCALING, TILE_SCALING


class GameView(arcade.View):

    """
        Main Game view
    """

    def __init__(self):
        # call super method
        super().__init__()

        # scene
        self.scene = None

        # special variable for player sprite
        self.player_sprite = None

    def setup(self):
        """
            Setup game here: you need call this method before game has been run
        """
        # Initialize Scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # player setting up
        image_source = ':resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png'
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)

    def on_draw(self):
        """
            Screen rendering
        """

        # clear screen
        arcade.start_render()

        # Draw our Scene
        self.scene.draw()
