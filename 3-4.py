#3-4
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollProjectileHits()    
    if len(hits) > 0 :
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        mc.player.setTilePos(x,y,z)
        mc.spawnEntity(x,y,z,99)
        
        

#當弓箭射到方塊的事件發生時
#把玩家傳送到弓箭的位置
#並且生成一隻鐵巨人(ID:99)
#檔名存成 practice2.py
