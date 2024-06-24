from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import random
import math
import glob
from itertools import cycle

window.borderless = False
window.title = 'Pinecraft'

app = Ursina()

Sky(texture='sky_sunset')

p = FirstPersonController()

hand = Entity(
    parent=camera.ui,
    model='cube',
    texture="white_cube",
    scale=0.7,
    rotation=Vec3(-10, -10, 5),
    position=Vec2(0.6,0.6)
)

p.gravity = 0.4

p.cursor.color = color.white33
positions = []
class Voxel(Button):
    def __init__(self, position=(0, 0, 0),vtexture='white_cube',model='cube', vcolor=color.white, scale=1):
        if vcolor:
            super().__init__(
                    parent=scene,
                    position=position,
                    model=model,
                    origin_y=.5,
                    texture=vtexture,
                    color=vcolor,
                    scale=scale,
                    collider='mesh',
                )
noise = PerlinNoise (octaves=3,seed=random.randint(1,1000000))

for z in range(40):
    for x in range(40):
        y = noise([x * .02,z * .02])
        y = math.floor(y * 7.5)
        voxel = Voxel(position=(x, y, z), model='assets/Grass_Block', vtexture='assets/Grass_Block_TEX',scale=0.5)
        if y == 0:
            positions += (x, y, z)
            
birds = Audio('assets/birds.mp3', loop=True, autoplay=True, volume=8)

textures = cycle(glob.glob('assets/*.png')+glob.glob('assets/*.jpg'))
vtexture = next(textures)
def update():
    hand.texture = vtexture
    hand.model = 'assets/Grass_Block'
    hand.scale = 0.2
    hand.texture = vtexture
    if held_keys['f']:
        p.y += 1 * time.dt * 5
        p.gravity = 0
    if held_keys['left mouse']:
        hand.position = Vec2(0.55, -0.55)
    elif held_keys['right mouse']:
        hand.position = Vec2(0.55, -0.55)
    else:
        hand.position = Vec2(0.6, -0.6)
def input(key):
    global textures,vtexture
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=20)
        if hit_info.hit:
            a = Audio('sine', loop=False, autoplay=True, volume=3)
            if vtexture == 'assets/Grass_Block_TEX':
                Voxel(position=hit_info.entity.position + hit_info.normal, model='assets/Grass_Block', vtexture=vtexture,scale=0.5)
            else:
                 Voxel(position=hit_info.entity.position + hit_info.normal, model='assets/Grass_Block', vtexture=vtexture,scale=0.5)
            
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
        
        a = Audio('sine', loop=False,pitch=0.6, autoplay=True, volume=3)
    if key == 'g':
        vtexture = next(textures)
    if key == 't':
        a = Audio('assets/teleport.mp3', loop=False, autoplay=True, volume=3)
        p.position = random.choice(positions)
        p.y = 0
    if key == 'h':
        p.gravity = 0.4
    if key == 'escape':
        quit()    

app.run()
