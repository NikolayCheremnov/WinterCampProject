import arcade

from GameSettings import SPAWN_POINT, GRAVITY, SPEED, JUMP


class GameView(arcade.View):

    def __init__(self):
        # вызов конструктора базового класса
        super().__init__()
        # создание сцены
        self.scene = None
        # спрайт игрока
        self.player_sprite = None
        # физический движок
        self.engine = None

    def setup(self):
        # 1. инициализация сцены
        self.scene = arcade.Scene()
        # 2. Добавление списки спрайтов на сцену
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Walls', use_spatial_hash=True)
        # 3. текстурируем игрока
        src = ':resources:images/animated_characters/male_adventurer/maleAdventurer_fall.png'
        self.player_sprite = arcade.Sprite(src, 1)
        self.player_sprite.center_x = SPAWN_POINT[0]
        self.player_sprite.center_y = SPAWN_POINT[1]
        self.scene.add_sprite('Player', self.player_sprite)
        # 4. добавление земли
        src = ':resources:images/tiles/grassMid.png'
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(src, 0.5)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite('Walls', wall)
        # 5. добавление стенок
        src = ':resources:images/tiles/brickTextureWhite.png'
        for y in range(0, 1000, 64):
            # левая стенка
            wall_1 = arcade.Sprite(src, 0.5)
            wall_1.center_x = 0
            wall_1.center_y = y
            # правая стенка
            wall_2 = arcade.Sprite(src, 0.5)
            wall_2.center_x = self.window.width
            wall_2.center_y = y
            # добавление на сцену
            self.scene.add_sprite('Walls', wall_1)
            self.scene.add_sprite('Walls', wall_2)

        # инициализация физического движка
        self.engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY,
            walls=self.scene['Walls'])

    def on_key_press(self, key, modifiers):
        # 1. обработка ходьбы
        if key == arcade.key.A:
            self.player_sprite.change_x = -SPEED
        if key == arcade.key.D:
            self.player_sprite.change_x = SPEED
        # 2. добавление прыжка
        if key == arcade.key.SPACE and self.engine.can_jump():
            self.player_sprite.change_y = JUMP
        # 3. строительство
        src = ':resources:images/enemies/slimeBlock.png'
        # 3.1 строительство под себя
        if key == arcade.key.S:
            box = arcade.Sprite(src, 0.5)
            box.center_x = self.player_sprite.center_x
            box.center_y = self.player_sprite.center_y - 70
            self.scene.add_sprite('Walls', box)
        # 3.2. строительство влево
        if key == arcade.key.Q:
            box = arcade.Sprite(src, 0.5)
            box.center_x = self.player_sprite.center_x - 70
            box.center_y = self.player_sprite.center_y
            self.scene.add_sprite('Walls', box)
        # 3.3. строительство вправо
        if key == arcade.key.E:
            box = arcade.Sprite(src, 0.5)
            box.center_x = self.player_sprite.center_x + 70
            box.center_y = self.player_sprite.center_y
            self.scene.add_sprite('Walls', box)

    def on_key_release(self, key, modifiers):
        # 1. обработка ходьбы
        if key == arcade.key.A:
            self.player_sprite.change_x = 0
        if key == arcade.key.D:
            self.player_sprite.change_x = 0
        # 2. добавление прыжка
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = 0

    def on_update(self, delta_time):
        self.engine.update()

    def on_draw(self):
        # отрисовка игры
        arcade.start_render()
        self.scene.draw()