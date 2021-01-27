from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    mc.executeCommand("time add 50")
    time.sleep(0.05)