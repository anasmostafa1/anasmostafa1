from ursina import *
from random import randint


app = Ursina(forced_aspect_ratio=.8)
camera.orthographic = 1
camera.fov = 20
bg = Entity(model='quad', scale=(30, 50), texture='grass', color=hsv(0,0,.2))
player = Entity(model=Circle(3), color=color.azure, speed=8, y=-.4, z=-1,collider="box")
player.bullet_renderer = Entity(model=Mesh(mode='point', thickness=.15), color=color.yellow)

scene.fog_density = (10,50)
ec = EditorCamera(rotation_x=-20)

def shoot():
    player.bullet_renderer.model.vertices.append(player.position)

shoot_cooldown = .1
shoot_sequence = Sequence(Func(shoot), Wait(shoot_cooldown), loop=True)

def update():
    move_direction = Vec2(held_keys['d']-held_keys['a'], held_keys['w']-held_keys['s']).normalized()
    player.position += move_direction * player.speed * time.dt
    bg.texture_offset += Vec2(0, time.dt)

    for i, bullet in enumerate(player.bullet_renderer.model.vertices):
        player.bullet_renderer.model.vertices[i] += Vec3(0, time.dt * 10, 0)
        for enemy in enemies:
            if distance_2d(bullet, enemy) < .5:
                enemy.hp -= 1
                enemy.blink(color.white)
                if enemy.hp <= 0:
                    dust = Entity(model=Circle(), scale=.5, color=color.orange  , position=enemy.position)
                    dust.animate_scale(5, duration=.3, curve=curve.linear)
                    dust.fade_out(duration=.2)
                    enemies.remove(enemy)
                    destroy(enemy)
                    player.bullet_renderer.model.vertices.remove(bullet)
                    print('a')

    if len(player.bullet_renderer.model.vertices):
        player.bullet_renderer.model.vertices = player.bullet_renderer.model.vertices[-100:]  # max bullets

    player.bullet_renderer.model.generate()

def input(key):
    if key == 'space':
        shoot_sequence.start()
    if key == 'space up':
        shoot_sequence.paused = True

enemies = []

def spawn_enemy():
    x_pos = randint(-5, 5)  # Random x position
    enemy = Entity(model=Circle(3), rotation_z=180, position=(x_pos, 16), color=color.red, z=-1, speed=3, hp=1, collider="box")
    enemies.append(enemy)
    invoke(spawn_enemy, delay=0.5)  # Spawn a new enemy every 2 seconds

def enemy_update():
    for e in enemies:
        e.position += e.up * e.speed * time.dt

enemy_handler = Entity(update=enemy_update)

spawn_enemy()  # Start spawning enemies

app.run()
