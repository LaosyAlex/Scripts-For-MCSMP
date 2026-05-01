import minescript as mcs # type: ignore
import math
import time

def textPrint(text):
    try:
        text = str(text)
        with open(r"C:\Github\Scripts-For-MCSMP\log.log", "a") as f: #appending to a textfile
            f.write(f"{text}\n\n\n")
    except:
        with open(r"C:\Github\Scripts-For-MCSMP\log.log", "a") as f: #appending to a textfile
            f.write("Error when appending\n\n\n")

def viewEntityInformation(entity):
    try:
        info = (
            f"name={entity.name}, \n"
            f"type={entity.type}, \n"
            f"pos={entity.position}, \n"
            f"health={entity.health}"
        )

        nbt = str(entity.nbt)
        prettynbt = nbt.replace(",", ",\n").replace("{", "{\n").replace("}", "\n}")

        textPrint(f"{info}\n{prettynbt}")
    except:
        textPrint("Error in printing entity information")

def distanceBetween(pos1, pos2):
    return math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2+(pos1[2]-pos2[2])**2)

def findTargetSheep():
    player = mcs.player()
    tSheep = None
    entities = mcs.entities(nbt = True, name="Sheep")

    for e in entities:
        nbt = str(e.nbt)
        
        isAdult = "Age:-" not in nbt
        isNotSheared = "Sheared:0b" in nbt

        if isAdult and isNotSheared:
            if tSheep == None or distanceBetween(player.position, tSheep.position) > distanceBetween(player.position, e.position):
                tSheep = e

    return tSheep

def logAllEntities():
    entities = mcs.entities()
    for e in entities:
        textPrint(str(e))

def logAllItemEntities():
    entities = mcs.entities(type="entity.minecraft.item")
    for e in entities:
            textPrint(str(e))

def findTargetWool():
    player = mcs.player()
    tWool = None
    entities = mcs.entities(type="entity.minecraft.item")

    for e in entities:
        if "Wool" in e.name:
            if tWool == None or distanceBetween(player.position, tWool.position) > distanceBetween(player.position, e.position):
                tWool = e

    return tWool

def main():
    target = mcs.player_get_targeted_entity(nbt=True)
    viewEntityInformation(target)
    mcs.player_press_forward(True)
    mcs.player_press_use(True)
    while True:
        targetSheep = findTargetSheep()
        targetWool = findTargetWool()

        if targetWool != None:
            posW = targetWool.position
            mcs.player_look_at(posW[0],posW[1],posW[2])
        elif targetSheep != None:
            posT = targetSheep.position
            mcs.player_look_at(posT[0],posT[1],posT[2])
            


        

if __name__ == "__main__":
    open(r"C:\Github\Scripts-For-MCSMP\log.log", "w").close() #wipes previous log data
    main()
