from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from perlin_noise import PerlinNoise

app = Ursina()

sunset = (250, 214, 165)

grass_texture = load_texture('assets/grass_block.png')
arm_texture   = load_texture('assets/arm_texture.png')
sunset_texture = load_texture('funny.jpeg')

freq = 10
amp = 3
noise = PerlinNoise(octaves = 3, seed = 177698315)

block_pick = 1

Player = FirstPersonController()

def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

class Sky(Entity):
    def __init__(self, position=(5,2,5), pop = True, yooo = 150):
        super().__init__(
          parent = scene,
          model = 'sphere',
          position = position,
          color = color.cyan,
          scale = yooo,
          double_sided = pop
        )

class OtherSky(Entity):
    def __init__(self, position=(5,2,5), hehe = True, creativity = 140):
        super().__init__(
          parent = scene,
          model = 'sphere',
          position = position,
          texture = sunset_texture,
          scale = creativity,
          double_sided = hehe
        )
ded = Sky()

sky = ded


class Block(Entity):
	def __init__(Voxel, blook = color.green, doood = 'cube', lel = 'white_cube'):
		super().__init__(
			parent = camera.ui,
			model = doood,
			texture = lel,
            scale = .2,
            color = blook,
            rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.10))

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.6,-0.6))


class Voxel(Button):
    def __init__(self, position=(0,0,0), idk = color.color(0, 0, random.uniform(.9, 1.0)), wasd = grass_texture, idkwhattonamethis = 'assets/block', why = 0.5):
        super().__init__(
            parent = scene,
            position = position,
            model = idkwhattonamethis,
            origin_y = .5,
            color = idk,
            texture = wasd,
            highlight_color = color.lime,
            scale = why
        )

    def input(self, key):
        if self.hovered:

            if key == '8':
                otherSky = OtherSky(creativity = 160); sky = Sky(yooo = 140)
                ded = Sky()

            if key == '9':
                otherSky = OtherSky(creativity = 140); sky = Sky(yooo = 160)
                ded = OtherSky()

            if key == '1':
                block = Block(blook = color.green, lel = 'white_cube', doood= 'cube')

            if key == '2':
                block = Block(blook = color.gray, lel = 'white_cube', doood= 'cube')

            if key == '3':
                block = Block(blook = color.orange, lel = 'white_cube', doood= 'cube')

            if key == '4':
                block = Block(blook = color.red, lel = 'white_cube', doood= 'cube')


            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, wasd = 'white_cube', idkwhattonamethis = 'cube', why = 1, idk = color.green)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, wasd = 'white_cube', idkwhattonamethis = 'cube', why = 1, idk = color.gray)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, wasd = 'white_cube', idkwhattonamethis = 'cube', why = 1, idk = color.orange)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, wasd = 'white_cube', idkwhattonamethis = 'cube', why=1, idk = color.red)

            if key == 'right mouse down':
                destroy(self)


for z in range(20):
    for x in range(20):
         voxel = Voxel(position=(x,z))
         voxel.x = x
         voxel.z = z
         voxel.y = noise([z/freq * amp,z/freq * amp]) 

block = Block()
hand = Hand()

app.run()