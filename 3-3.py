from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random,time

while True:
    x,y,z = mc.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    y = y+30
    mc.spawnEntity(x+a,y,z+b,93)
    time.sleep(0.1)
    
# /kill @e[type=chicken]