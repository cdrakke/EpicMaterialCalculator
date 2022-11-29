from unittest import result
import PySimpleGUI as sg

# THEMES & FONTS
sg.theme('DarkBlue')
HEADFONT = ("Verdana", 20)
BODYFONT = ("Consolas", 12)

# LAYOUTS
headColumn = [
    [sg.Text("Mir4 Epic Calculator by Drekyz", justification="center", font=HEADFONT)],
]

headerSelector = [
    [
        sg.Text("Select a material type to craft.", justification='center')
    ],
    [
        sg.Radio("Scale", "TYPE_BUTTON", default=False, key="TYPE_BUTTON", enable_events=True),
        sg.Radio("Leather", "TYPE_BUTTON", default=False, key="TYPE_BUTTON", enable_events=True),
        sg.Radio("Horn", "TYPE_BUTTON", default=False, key="TYPE_BUTTON", enable_events=True)
    ]
]

material1UCColumn = [
    [
        sg.Text("MATERIAL 1: ", key="UC_MATERIAL1", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL1_UC_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL1_UC_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material2UCColumn = [
    [
        sg.Text("MATERIAL 2: ", key="UC_MATERIAL2", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL2_UC_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL2_UC_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material3UCColumn = [
    [
        sg.Text("MATERIAL 3: ", key="UC_MATERIAL3", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL3_UC_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL3_UC_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material1RAREColumn = [
    [
        sg.Text("MATERIAL 1: ", key="RARE_MATERIAL1", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL1_RARE_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL1_RARE_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material2RAREColumn = [
    [
        sg.Text("MATERIAL 2: ", key="RARE_MATERIAL2", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL2_RARE_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL2_RARE_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material3RAREColumn = [
    [
        sg.Text("MATERIAL 3: ", key="RARE_MATERIAL3", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL3_RARE_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL3_RARE_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material1EPICColumn = [
    [
        sg.Text("MATERIAL 1: ", key="EPIC_MATERIAL1", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL1_EPIC_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL1_EPIC_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material2EPICColumn = [
    [
        sg.Text("MATERIAL 2: ", key="EPIC_MATERIAL2", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL2_EPIC_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL2_EPIC_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

material3EPICColumn = [
    [
        sg.Text("MATERIAL 3: ", key="EPIC_MATERIAL3", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="MATERIAL3_EPIC_TRADABLE", size=(15, 1), justification="center"),
        sg.InputText(key="MATERIAL3_EPIC_NOT_TRADABLE", size=(15, 1), justification="center")
    ]
]

copperColumn = [
    [
        sg.Text("Copper: ", key="COPPER_TEXT", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="COPPER", size=(15, 1), justification="center"),
    ]
]

darksteelColumn = [
    [
        sg.Text("Darksteel: ", key="DARKSTEEL_TEXT", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="DARKSTEEL", size=(15, 1), justification="center"),
    ]
]

glitteringColumn = [
    [
        sg.Text("Glitt. Powder: ", key="GLITTERING_POWDER_TEXT", font=BODYFONT, size=(20, 1)), 
        sg.InputText(key="GLITTERING_POWDER", size=(15, 1), justification="center"),
    ]
]
buttonColumn = [
    [
        sg.Button("Calculate")
    ]
]

layout = [
    # HEADERS
    #[sg.Column(headColumn, justification='center')],
    [sg.Column(headerSelector, justification='center')],
    #[sg.Column(resultColumn, justification='center')],
    # UC
    [
        sg.Column(
                [
                    [sg.Text("Uncommon materials you have.")]
                ], justification='center'
            )
    ],
    [sg.Column(material1UCColumn, justification='center')],
    [sg.Column(material2UCColumn, justification='center')],
    [sg.Column(material3UCColumn, justification='center')],
    # RARE
    [
        sg.Column(
                [
                    [sg.Text("Rare materials you have.")]
                ], justification='center'
            )
    ],
    [sg.Column(material1RAREColumn, justification='center')],
    [sg.Column(material2RAREColumn, justification='center')],
    [sg.Column(material3RAREColumn, justification='center')],
    # EPIC
    [
        sg.Column(
                [
                    [sg.Text("Epic materials you have.")]
                ], justification='center'
            )
    ],
    [sg.Column(material1EPICColumn, justification='center')],
    [sg.Column(material2EPICColumn, justification='center')],
    [sg.Column(material3EPICColumn, justification='center')],
    # CURRENCIES
    [
        sg.Column(
                [
                    [sg.Text("Currencies you currently have.")]
                ], justification='center'
            )
    ],
    [sg.Column(copperColumn, justification='center')],
    [sg.Column(darksteelColumn, justification='center')],
    [sg.Column(glitteringColumn, justification='center')],
    [sg.Column(buttonColumn, justification='center')]
]