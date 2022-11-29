
import math

class EpicItem:
    def __init__(
            self, materialType, 
            uc1t, uc1nt,
            uc2t, uc2nt,
            uc3t, uc3nt,
            r1t, r1nt,
            r2t, r2nt,
            r3t, r3nt,
            e1t, e1nt,
            e2t, e2nt,
            e3t, e3nt,
            copper, ds, glit
        ):
        self.materialType = materialType

        self.uc1t = uc1t
        self.uc2t = uc2t
        self.uc3t = uc3t
        self.uc1nt = uc1nt
        self.uc2nt = uc2nt
        self.uc3nt = uc3nt
        
        self.r1t = r1t
        self.r2t = r2t
        self.r3t = r3t
        self.r1nt = r1nt
        self.r2nt = r2nt
        self.r3nt = r3nt
        
        self.e1t = e1t
        self.e2t = e2t
        self.e3t = e3t
        self.e1nt = e1nt
        self.e2nt = e2nt
        self.e3nt = e3nt

        self.uncommon_material_1 = int(uc1t) + int(uc1nt)
        self.uncommon_material_2 = int(uc2t) + int(uc2nt)
        self.uncommon_material_3 = int(uc3t) + int(uc3nt)

        self.rare_material_1 = int(r1t) + int(r1nt)
        self.rare_material_2 = int(r2t) + int(r2nt)
        self.rare_material_3 = int(r3t) + int(r3nt)

        self.epic_material_1 = int(e1t) + int(e1nt)
        self.epic_material_2 = int(e2t) + int(e2nt)
        self.epic_material_3 = int(e3t) + int(e3nt)

        self.copper = copper
        self.darksteel = ds
        self.glittering = glit
    
        self.inventory = {
            "uncommon_material_1": int(uc1t) + int(uc1nt),
            "uncommon_material_2": int(uc2t) + int(uc2nt),
            "uncommon_material_3": int(uc3t) + int(uc3nt),
            "rare_material_1": int(r1t) + int(r1nt),
            "rare_material_2": int(r2t) + int(r2nt),
            "rare_material_3": int(r3t) + int(r3nt),
            "epic_material_1": int(e1t) + int(e1nt),
            "epic_material_2": int(e2t) + int(e2nt),
            "epic_material_3": int(e3t) + int(e3nt),
            "copper": copper,
            "darksteel": ds,
            "glittering": glit
        }

        self.total_needed_copper = 0
        self.total_needed_darksteel = 0
        self.total_needed_glittering = 0

        self.copper_difference = 0
        self.darksteel_difference = 0
        self.glittering_difference = 0

    def TurnAllMaterialsToEpic(self):
        for i in range(3):
            count = i + 1

            # Uncommon -> Rare
            ucToRare = self.inventory[f"uncommon_material_{count}"] / 10
            self.total_needed_copper += ucToRare * 2000
            self.total_needed_darksteel += ucToRare * 1000
            self.total_needed_glittering += ucToRare * 2
            self.inventory[f"uncommon_material_{count}"] = self.inventory[f"uncommon_material_{count}"] % 10
            self.inventory[f"rare_material_{count}"] += ucToRare

            # Rare -> Epic
            rareToEpic = self.inventory[f"rare_material_{count}"] / 10
            self.total_needed_copper += rareToEpic * 20000
            self.total_needed_darksteel += rareToEpic * 5000
            self.total_needed_glittering += rareToEpic * 25
            self.inventory[f"rare_material_{count}"] = self.inventory[f"rare_material_{count}"] % 10
            self.inventory[f"epic_material_{count}"] += rareToEpic

        self.copper_difference = int(self.total_needed_copper - self.inventory["copper"])
        self.darksteel_difference = int(self.total_needed_darksteel - self.inventory["darksteel"])
        self.glittering_difference = int(self.total_needed_glittering - self.inventory["glittering"])

def updateInputBoxes(window, outerData, materialType):
    try:
        data = outerData[materialType]
    except:
        data = {}
    if not data == {}:
        for i in range(3):
            window[f"MATERIAL{i+1}_UC_TRADABLE"].update(data[f"uc{i+1}t"])
            window[f"MATERIAL{i+1}_UC_NOT_TRADABLE"].update(data[f"uc{i+1}nt"])

            window[f"MATERIAL{i+1}_RARE_TRADABLE"].update(data[f"r{i+1}t"])
            window[f"MATERIAL{i+1}_RARE_NOT_TRADABLE"].update(data[f"r{i+1}nt"])

            window[f"MATERIAL{i+1}_EPIC_TRADABLE"].update(data[f"e{i+1}t"])
            window[f"MATERIAL{i+1}_EPIC_NOT_TRADABLE"].update(data[f"e{i+1}nt"])

            window["COPPER"].update(data["copper"])
            window["DARKSTEEL"].update(data["darksteel"])
            window["GLITTERING_POWDER"].update(data["glittering"])
        
    else:
        for i in range(3):
            window[f"MATERIAL{i+1}_UC_TRADABLE"].update(0)
            window[f"MATERIAL{i+1}_UC_NOT_TRADABLE"].update(0)

            window[f"MATERIAL{i+1}_RARE_TRADABLE"].update(0)
            window[f"MATERIAL{i+1}_RARE_NOT_TRADABLE"].update(0)

            window[f"MATERIAL{i+1}_EPIC_TRADABLE"].update(0)
            window[f"MATERIAL{i+1}_EPIC_NOT_TRADABLE"].update(0)

            window["COPPER"].update(0)
            window["DARKSTEEL"].update(0)
            window["GLITTERING_POWDER"].update(0)
    return window