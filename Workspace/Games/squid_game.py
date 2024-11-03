from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

window.borderless = False

app = Ursina()

window.fullscreen = True
window.color=color.black

player = FirstPersonController(
  collider='box')
player.cursor.color = color.rgba(255,0,0,100)
ground = Entity(
  model='plane',
  texture='grass',
  collider='box',
  scale=(30,0,5)
)

pill1 = Entity(
  model='cube',
  color=color.violet,
  scale=(0.4,0.1,53),
  z=28,x=-0.7
)
pill2 = duplicate(pill1,
                  x=-3.7)
pill3 = duplicate(pill1,
                  x=0.6)
pill4 = duplicate(pill1,
                  x=3.6)

blocks = []
for i in range(12):
  block = Entity(
    model='cube',collider='box',
    color = color.white33,
    position=(2,0.1,3+i*4),
    scale=(3,0.1,2.5)
  )
  block2 = duplicate(block,
                     x=-2.2)
  blocks.append(
    (block,block2,randint(0,10)>7,
     randint(0,10)>7)
  )
goal = Entity(
  color=color.brown,
  model='cube',
  z=55,
  scale=(10,1,10),
  collider='box',
)
pillar = Entity(
  color=color.gold,
  model='cube',
  z=58,
  scale=(2,40,2
         ),y=20,
  collider='box',
)

def update():
  for block1,block2,k,n in blocks:
    for x,y in [(block1,k),
                (block2,n)]:
      if x.intersects() and y:
        invoke(destroy,x,
               delay=.01)
        x.fade_out(duration=.01)
def input(key):
  if key == 'r':
    player.position = (0,0,0)
  if key =='escape':
    quit()

app.run()
