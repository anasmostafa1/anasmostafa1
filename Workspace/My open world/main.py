from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
import random

window.borderless = False

app = Ursina()

# Create a sky
Sky(texture='sky_sunset')

# Set up the ground
ground = Entity(model='cube', color=color.white, texture='images/ground.png', z=-0.1, y=-1, origin_y=0.5, scale=(1000, 10, 10), collider='box', ignore=True)

# Create the player
player = PlatformerController2d(texture='images/girl.png',model='quad', double_sided=True, origin_y=-0.5 ,color=color.white, scale=(2, 4), position=(0, 0, -3))
player.x = 1
player.y = raycast(player.world_position, player.down).world_point[1] + 0.01

# Set up camera follow
camera.add_script(SmoothFollow(target=player, offset=[0, 5, -30], speed=4))

# Generate trees
for _ in range(100):
    tree = Entity(scale=8, model='quad', texture='images/tree.png', position=(random.randint(-500, 500), 3, 1))

# Generate rocks
for z in range(15):
    house = Entity(scale=4, model='quad', collider='box', texture='images/rock.png', position=(random.randint(-500, 500), 1, -1))

# Generate houses
for z in range(25):
    house = Entity(scale=8, model='quad', texture='images/home.png', position=(random.randint(-500, 500), 3, -2))

# Input bindings
input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')

# Enable Noclip mode for testing
from ursina.scripts.noclip_mode import NoclipMode2d
player.add_script(NoclipMode2d())

app.run()
