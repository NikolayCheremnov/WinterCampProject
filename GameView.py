import arcade

from GameSettings import SPAWN_POINT, GRAVITY, SPEED, JUMP, LAVA_TIME


class GameView(arcade.View):

    def __init__(self, initial_view):
        # вызов конструктора базового класса
        super().__init__()
        # создание сцены
        self.scene = None
        # спрайт игрока
        self.player_sprite = None
        # физический движок
        self.engine = None
        # камера
        self.camera = None
        # начальный уровень лавы
        self.lava_level = 32
        # начальное окно для рестарта
        self.initial_view = initial_view
        # счет
        self.score = 0

    def setup(self):
        # 0. инициализация камеры
        self.camera = arcade.Camera(self.window.width, self.window.height)
        # 1. инициализация сцены
        self.scene = arcade.Scene()
        # 2. Добавление списки спрайтов на сцену
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Walls', use_spatial_hash=True)
        self.scene.add_sprite_list('Lava', use_spatial_hash=True)
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
        # запуск лавы
        arcade.schedule(self.add_lava, LAVA_TIME)

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
        # 1. обновление состояния движка
        self.engine.update()
        # 2. обновление камеры
        self.center_camera_to_player()
        # 3. проверка на столкновение с лавой
        lava_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene['Lava'])
        if len(lava_hit_list) != 0:
            self.restart()
        # 4. Обновление счета
        if self.player_sprite.center_y > self.score:
            self.score = self.player_sprite.center_y

    def on_draw(self):
        # отрисовка игры
        arcade.start_render()
        self.scene.draw()
        # активация камеры
        self.camera.use()
        # отрисовка счета
        arcade.draw_text(f'Высота: {self.score / 100} м.',
                         self.player_sprite.center_x - 32, self.player_sprite.center_y + 40,
                         arcade.color.BLACK, font_size=15)

    # вспомогательный метод центрирования камеры на игроке
    def center_camera_to_player(self):
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )

        if screen_center_y < 0:
            screen_center_y = 0

        player_centered = 0, screen_center_y
        self.camera.move_to(player_centered)

    # вспомогательный метод добавления лавы
    def add_lava(self, time):
        src = ':resources:images/tiles/lava.png'
        for x in range(0, 1250, 64):
            lava = arcade.Sprite(src, 0.5)
            lava.center_x = x
            lava.center_y = self.lava_level
            self.scene.add_sprite('Lava', lava)
        self.lava_level += 64

    # вспомогательный метод рестарта
    def restart(self):
        arcade.unschedule(self.add_lava)
        self.initial_view.add_score_message(f'Вы достигли высоту {self.score / 100} м.')
        self.window.show_view(self.initial_view)

