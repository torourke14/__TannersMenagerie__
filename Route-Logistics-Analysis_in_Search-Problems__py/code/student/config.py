configuration = {
"text_size": 300,
"tile_size": 80,
"type": "load", #random
"seed": None,
"file": "./student/map.txt",
"map_size": [12, 5],
"delay": 0.04,
"debugMap": True,
"debug": True,
"save": False, #True
"hazards": False,
"basicTile": "street",
"maxBags": 2,
"agent":{
    "graphics":{
        "default": "game/graphics/logistics/deliver103.jpg"
        },
    "id": "agent",
    "marker": 'A',
    "start": [0,0],
    },
"maptiles": {
    "street": {
        "graphics":{
            "default": "game/graphics/logistics/street101.jpg",
            "traversed": "game/graphics/logistics/street101Traversed.jpg"
            },
        "id":  "street",
        "marker": 'T',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "Hill": {
        "graphics":{
            "default": "game/graphics/terrains/Hills100.png",
            "traversed": "game/graphics/terrains/HillsTraversed100.png"
            },
        "id":  "hill",
        "marker": 'H',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 2},
        },
    "pizza": {
        "graphics":{
            "default": "game/graphics/logistics/pizza101.jpg",
            "traversed": "game/graphics/logistics/pizza101.jpg"
            },
        "id":  "pizza",
        "marker": 'Z',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "customer0": {
        "graphics":{
            "default": "game/graphics/logistics/customer100.png",
            "traversed": "game/graphics/logistics/customer0_Traversed.png"
            },
        "id":  "customer0",
        "marker": '0',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 0},
        },
    "customer1": {
        "graphics":{
            "default": "game/graphics/logistics/customer100_1.png",
            "traversed": "game/graphics/logistics/customer1_Traversed.png"
            },
        "id":  "customer1",
        "marker": '1',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 1},
        },
    "start": {
        "graphics":{
            "default": "game/graphics/logistics/base101.png",
            "traversed": "game/graphics/logistics/base101.png"
            },
        "id":  "start",
        "marker": 'W',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "building": {
        "graphics":{
            "default": "game/graphics/logistics/building102.jpg",
            "traversed": "game/graphics/logistics/building102.jpg"
            },
        "id":  "building",
        "marker": 'X',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "blocked": True},
        }
    }
}
