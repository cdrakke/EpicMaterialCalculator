import PySimpleGUI as sg, json, time
from layouts import layout, BODYFONT, HEADFONT
from utils import EpicItem, updateInputBoxes
from datastore import DataManager

# DATA MANAGER
dataManager = DataManager()

# WINDOW CUSTOMIZATION
window = sg.Window('Mir4 Epic Calculator', layout, finalize=True)

# MAIN LOOP
while True:
    data = dataManager.readData()
    event, values = window.read()

    if event == "TYPE_BUTTON":
        window["UC_MATERIAL1"].update("[UC] Steel: ")
        window["UC_MATERIAL2"].update("[UC] E.M. Orb: ")
        window["UC_MATERIAL3"].update("[UC] M.S. Stone: ")

        window["RARE_MATERIAL1"].update("[R] Steel: ")
        window["RARE_MATERIAL2"].update("[R] E.M. Orb: ")
        window["RARE_MATERIAL3"].update("[R] M.S. Stone: ")

        window["EPIC_MATERIAL1"].update("[E] Steel: ")
        window["EPIC_MATERIAL2"].update("[E] E.M. Orb: ")
        window["EPIC_MATERIAL3"].update("[E] M.S. Stone: ")

        window = updateInputBoxes(window, data, "Scale")

    elif event == "TYPE_BUTTON0":
        window["UC_MATERIAL1"].update("[UC] Steel: ")
        window["UC_MATERIAL2"].update("[UC] Quintessence: ")
        window["UC_MATERIAL3"].update("[UC] E. Bauble: ")

        window["RARE_MATERIAL1"].update("[R] Steel: ")
        window["RARE_MATERIAL2"].update("[R] Quintessence: ")
        window["RARE_MATERIAL3"].update("[R] E. Bauble: ")

        window["EPIC_MATERIAL1"].update("[E] Steel: ")
        window["EPIC_MATERIAL2"].update("[E] Quintessence: ")
        window["EPIC_MATERIAL3"].update("[E] E. Bauble: ")

        window = updateInputBoxes(window, data, "Leather")

    elif event == "TYPE_BUTTON1":
        window["UC_MATERIAL1"].update("[UC] Platinum: ")
        window["UC_MATERIAL2"].update("[UC] I. Fragment: ")
        window["UC_MATERIAL3"].update("[UC] Anima Stone: ")

        window["RARE_MATERIAL1"].update("[R] Platinum: ")
        window["RARE_MATERIAL2"].update("[R] I. Fragment: ")
        window["RARE_MATERIAL3"].update("[R] Anima Stone: ")

        window["EPIC_MATERIAL1"].update("[E] Platinum: ")
        window["EPIC_MATERIAL2"].update("[E] I. Fragment: ")
        window["EPIC_MATERIAL3"].update("[E] Anima Stone: ")

        window = updateInputBoxes(window, data, "Horn")

    elif event == "Calculate":
        if values["TYPE_BUTTON"] == False and values["TYPE_BUTTON0"] == False and values["TYPE_BUTTON1"] == False:
            sg.Popup("Please select a crafting material type first.", keep_on_top=True)
        else:
            materialType = ""
            if values["TYPE_BUTTON"] == True:
                materialType = "Scale"
                material1 = "Steel: "
                material2 = "E.M. Orb: "
                material3 = "M.S. Stone: "
            elif values["TYPE_BUTTON0"] == True:
                materialType = "Leather"
                material1 = "Steel: "
                material2 = "Quintessence: "
                material3 = "E. Bauble: "
            elif values["TYPE_BUTTON1"] == True:
                materialType = "Horn"
                material1 = "Platinum: "
                material2 = "I. Fragment: "
                material3 = "Anima Stone: "
            epicItem = EpicItem(
                materialType,
                int(values["MATERIAL1_UC_TRADABLE"]),
                int(values["MATERIAL1_UC_NOT_TRADABLE"]),
                int(values["MATERIAL2_UC_TRADABLE"]),
                int(values["MATERIAL2_UC_NOT_TRADABLE"]),
                int(values["MATERIAL3_UC_TRADABLE"]),
                int(values["MATERIAL3_UC_NOT_TRADABLE"]),
                int(values["MATERIAL1_RARE_TRADABLE"]),
                int(values["MATERIAL1_RARE_NOT_TRADABLE"]),
                int(values["MATERIAL2_RARE_TRADABLE"]),
                int(values["MATERIAL2_RARE_NOT_TRADABLE"]),
                int(values["MATERIAL3_RARE_TRADABLE"]),
                int(values["MATERIAL3_RARE_NOT_TRADABLE"]),
                int(values["MATERIAL1_EPIC_TRADABLE"]),
                int(values["MATERIAL1_EPIC_NOT_TRADABLE"]),
                int(values["MATERIAL2_EPIC_TRADABLE"]),
                int(values["MATERIAL2_EPIC_NOT_TRADABLE"]),
                int(values["MATERIAL3_EPIC_TRADABLE"]),
                int(values["MATERIAL3_EPIC_NOT_TRADABLE"]),
                int(values["COPPER"]),
                int(values["DARKSTEEL"]),
                int(values["GLITTERING_POWDER"])
            )
            epicItem.TurnAllMaterialsToEpic()
            dataManager.saveData(epicItem.__dict__)

            resultLayout = [
                [sg.Text(f"[E] {material1}: {int(epicItem.inventory['epic_material_1'])}", key="EPIC_RESULT_MATERIAL1", font=BODYFONT, justification='center')],
                [sg.Text(f"[E] {material2}: {int(epicItem.inventory['epic_material_2'])}", key="EPIC_RESULT_MATERIAL2", font=BODYFONT, justification='center')],
                [sg.Text(f"[E] {material3}: {int(epicItem.inventory['epic_material_3'])}", key="EPIC_RESULT_MATERIAL3", font=BODYFONT, justification='center')],
                [sg.Text(f"Needed Copper: {int(epicItem.copper_difference)}", key="NEEDED_COPPER", font=BODYFONT, justification='center')],
                [sg.Text(f"Needed Darksteel: {int(epicItem.darksteel_difference)}", key="NEEDED_DARKSTEEL", font=BODYFONT, justification='center')],
                [sg.Text(f"Needed Glittering: {int(epicItem.glittering_difference)}", key="NEEDED_GLITTERING", font=BODYFONT, justification='center')]
            ]

            window2 = sg.Window('Results', resultLayout, finalize=True)
            while True:
                event2, values2 = window2.read()

                if event2 == sg.WIN_CLOSED or event2 == 'Exit':
                    break

            window2.close()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

# WINDOW CLOSE
window.close()