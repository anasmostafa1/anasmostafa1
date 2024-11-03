from ursina import *
from ursina.prefabs.first_person_controller \
  import FirstPersonController
from random import *

app = Ursina()

ground = Entity(model= 'cube',
                texture= 'white_cube',
                collider= 'mesh',
                scale= (50,1, 10),
                z=-4,)

player = FirstPersonController(
  collider='box',
  jump_height=5,
  z=-4,
)

sky = Sky()
lvl = 1

blocks = []
directions = []
window.fullscreen = True
seed(3)
for i in range(10):
  r = uniform(-2,2)
  block = Entity(
    position=(r, 1+i , 3+i*5),
    model='cube',
    texture='white_cube',
    color=color.azure,
    scale=(3.5, 0.5, 3.5),
    collider='box',
  )
  blocks.append(block)
  if r < 0:
    directions.append(randint(2,4))
  else:
    directions.append(randint(-4,-2))


goal = Entity(
  color=color.gold,
  model='cube',
  texture='white_cube',
  position=(0,11,55),
  scale=(10,1,10),
  collider='box'
)
pillar = Entity(
  color=color.green,
  model='cube',
  position=(0,36,58),
  scale=(1,50,1)
)


jump = Audio(
  'jump.mp3',
  loop = False,
  autoplay = False
)

walk = Audio(
  'jump.mp3',
  loop = False,
  autoplay = False
)


def update():
  global lvl
  i = 0
  for block in blocks:
    block.x -= directions[i] * time.dt
    if abs(block.x) > 5:
      directions[i] *= -1
    if block.intersects().hit:
      player.x -= directions[i]*time.dt
    i = i + 1
  if player.z > 54 and lvl == 1:
    lvl = 2
    sky.texture = 'sky_sunset'
  walking = held_keys['a'] or \
          held_keys['d'] or \
          held_keys['w'] or \
          held_keys['s']
  if walking and player.grounded:
    if not walk.playing:
      walk.play()
  else:
    if walk.playing:
      walk.stop()


def input(key):
  if key == 'escape':
    quit()
  if key == 'space':
    if not jump.playing:
      jump.play()
  if key == 'r':
    player.position = Vec3(0,0,-4)

app.run()
