import random

class Resource:
    ORE = "Ore"
    ENERGY = "Energy"
    CREDITS = "Credits"
    INFLUENCE = "Influence"
    ALL = [ORE, ENERGY, CREDITS, INFLUENCE]

FACTIONS = {
    "Sharnak Imperium": {"convert": (Resource.CREDITS, Resource.ORE), "discount": {"Weapons": Resource.ORE}, "bonus": "AttackReroll"},
    "The Conversation": {"convert": [(Resource.INFLUENCE, Resource.CREDITS), (Resource.CREDITS, Resource.INFLUENCE)], "upkeep": {Resource.CREDITS: 1, Resource.INFLUENCE: 1}, "discount": {"Engines": Resource.ORE, "Command": Resource.CREDITS}, "bonus": "DefenseReroll"},
    "Wulfram Collective": {"convert": (Resource.ORE, Resource.INFLUENCE), "upkeep": {Resource.INFLUENCE: 1}, "bonus": "AttackReroll"},
    "Rim Worlds Combine": {"convert": (Resource.ORE, Resource.CREDITS), "upkeep": {Resource.CREDITS: 1, Resource.ORE: 1}, "bonus": "ExploreReroll"},
    "The Aiiji": {"convert": [(Resource.INFLUENCE, Resource.CREDITS), (Resource.CREDITS, Resource.ORE)], "upkeep": {Resource.CREDITS: 2}, "discount": {"Command": Resource.INFLUENCE}, "bonus": "GeneralReroll"},
    "Altair Divide": {"convert": [(Resource.ORE, Resource.INFLUENCE), (Resource.INFLUENCE, Resource.CREDITS)], "discount": {"Weapons": Resource.ENERGY}, "bonus": "PreventReroll"},
    "Gaian Empire": {"convert": (Resource.CREDITS, Resource.INFLUENCE), "discount": {"Shields": Resource.ENERGY}, "bonus": "DefenseReroll"},
    "Purist Hegemony": {"convert": (Resource.INFLUENCE, Resource.ORE), "discount": {"Command": Resource.ENERGY}, "bonus": "DefensePlusOne"}
}

TECH_TREES = {
    "Wanderer-A": {
        "Weapons": [
            {"name": "Rail gun", "bonus": 1, "cost": {}},
            {"name": "Gauss Missile", "bonus": 3, "cost": {Resource.CREDITS: 1, Resource.ENERGY: 1, Resource.ORE: 3}},
            {"name": "Fusion Cannon", "bonus": 5, "cost": {Resource.CREDITS: 2, Resource.ENERGY: 2, Resource.ORE: 2}},
            {"name": "Antimatter Cannon", "bonus": 6, "cost": {Resource.CREDITS: 4, Resource.ENERGY: 3, Resource.ORE: 1}}
        ],
        "Shields": [
            {"name": "Force Shield", "bonus": 1, "cost": {}},
            {"name": "Phase Shield", "bonus": 2, "cost": {Resource.CREDITS: 3, Resource.ENERGY: 1}},
            {"name": "Nano-Hull", "bonus": 3, "cost": {Resource.CREDITS: 4, Resource.ENERGY: 2}},
            {"name": "Nano-Cloud", "bonus": 5, "cost": {Resource.CREDITS: 6, Resource.ENERGY: 3}}
        ],
        "Engines": [
            {"name": "Fusion Drive", "dist": 3, "energy_cost": 2, "cost": {}},
            {"name": "Tachyon Drive", "dist": 3, "energy_cost": 1, "cost": {Resource.CREDITS: 3, Resource.ORE: 1}},
            {"name": "Ehrenhaft Drive", "dist": 5, "energy_cost": 1, "cost": {Resource.CREDITS: 3, Resource.ORE: 2}},
            {"name": "Stellar Drive", "dist": 5, "energy_cost": 1, "cost": {Resource.CREDITS: 4, Resource.ORE: 3}}
        ],
        "Command": [
            {"name": "Navicomm", "bonus": 0, "cost": {}},
            {"name": "Veteran Captain", "bonus": 1, "infl_cost": 1, "cost": {Resource.CREDITS: 2, Resource.ENERGY: 2, Resource.INFLUENCE: 1}},
            {"name": "Drone AI", "bonus": "Reroll", "energy_cost": 1, "cost": {Resource.CREDITS: 3, Resource.ENERGY: 2, Resource.INFLUENCE: 2}},
            {"name": "Shipmind", "bonus": "DoubleReroll", "energy_cost": 1, "cost": {Resource.CREDITS: 4, Resource.ENERGY: 2, Resource.INFLUENCE: 2}}
        ]
    },
    "Raider-B": {
        "Weapons": [
            {"name": "Rail gun", "bonus": 2, "cost": {}},
            {"name": "Gauss Missile", "bonus": 4, "cost": {Resource.CREDITS: 3, Resource.ENERGY: 1, Resource.ORE: 3}},
            {"name": "Fusion Cannon", "bonus": 6, "cost": {Resource.CREDITS: 3, Resource.ENERGY: 2, Resource.ORE: 3}},
            {"name": "Antimatter Cannon", "bonus": 7, "cost": {Resource.CREDITS: 3, Resource.ENERGY: 3, Resource.ORE: 3}}
        ],
        "Shields": [
            {"name": "Force Shield", "bonus": 2, "cost": {}},
            {"name": "Phase Shield", "bonus": 3, "cost": {Resource.CREDITS: 3, Resource.ENERGY: 1}},
            {"name": "Nano-Hull", "bonus": 5, "cost": {Resource.CREDITS: 4, Resource.ENERGY: 2}},
            {"name": "Nano-Cloud", "bonus": 6, "cost": {Resource.CREDITS: 6, Resource.ENERGY: 3}}
        ],
        "Engines": [
            {"name": "Fusion Drive", "dist": 3, "energy_cost": 2, "cost": {}},
            {"name": "Tachyon Drive", "dist": 3, "energy_cost": 1, "cost": {Resource.CREDITS: 3, Resource.ORE: 1}},
            {"name": "Ehrenhaft Drive", "dist": 5, "energy_cost": 1, "cost": {Resource.CREDITS: 3, Resource.ORE: 2}},
            {"name": "Stellar Drive", "dist": 5, "energy_cost": 1, "cost": {Resource.CREDITS: 4, Resource.ORE: 3}}
        ],
        "Command": [
            {"name": "Navicomm", "bonus": 0, "cost": {}},
            {"name": "Veteran Captain", "bonus": 1, "infl_cost": 1, "cost": {Resource.CREDITS: 3, Resource.ENERGY: 3, Resource.INFLUENCE: 2}},
            {"name": "Drone AI", "bonus": "Reroll", "energy_cost": 1, "cost": {Resource.CREDITS: 4, Resource.ENERGY: 3, Resource.INFLUENCE: 2}},
            {"name": "Shipmind", "bonus": "DoubleReroll", "energy_cost": 1, "cost": {Resource.CREDITS: 4, Resource.ENERGY: 4, Resource.INFLUENCE: 3}}
        ]
    }
}

EXTENSION_NAMES = {
    1: "Orbital Bombardment Array", 2: "Command Carrier Bay", 3: "Ablative Hull Plating",
    4: "Precision Targeting AI", 5: "EMP Pulse Caster", 6: "Quantum Slipstream Drive",
    7: "Deep Space Sensors", 8: "Tractor Beam", 9: "Diplomatic Envoy Protocol",
    10: "Scavenger Harvesters", 11: "Advanced Logistics Hub", 12: "Terraforming Charges",
    13: "Galactic Broadcast Node", 14: "Stealth Recon Uplink", 15: "Mobile Command Center"
}

TACTIC_NAMES = {
    1: "Emergency Thrusters", 2: "Shield Overload", 3: "Experimental Ordnance",
    4: "Bypass Codes", 5: "Flanking Maneuver", 6: "Sabotage", 7: "Point Defense Grid",
    8: "Kamikaze Protocol", 9: "Industrial Espionage", 10: "Trade Network Hack",
    11: "Smuggler's Route", 12: "Deep Cover Agent", 13: "Rapid Deployment",
    14: "Ghost Fleet", 15: "Resource Transmutation", 16: "Astrogation Master",
    17: "Distress Beacon", 18: "Anomalous Field", 19: "Diplomatic Backchannels",
    20: "Aggressive Terraforming", 21: "Veto Power", 22: "Bribery",
    23: "Political Assassination", 24: "Filibuster Delay", 25: "Blackmail"
}

AGENDAS = {
    # Resolutions (FOR/AGAINST)
    1: {"name": "Wormhole Tolls", "type": "RESOLUTION", "desc": "For: Spacewarp costs 1 Credit. Against: Discard 1 Energy.", "effect": lambda sim, choice: sim.apply_resolution(1, choice)},
    2: {"name": "Demilitarized Zones", "type": "RESOLUTION", "desc": "For: Cannot attack with 0 Influence. Against: No effect.", "effect": lambda sim, choice: sim.apply_resolution(2, choice)},
    3: {"name": "Arms Trade", "type": "RESOLUTION", "desc": "For: Gain 2 Ore. Against: Next ship half cost.", "effect": lambda sim, choice: sim.apply_resolution(3, choice)},
    4: {"name": "Technological Subsidies", "type": "RESOLUTION", "desc": "For: Next tech -1 cost. Against: 3+ Techs lose 1 Energy.", "effect": lambda sim, choice: sim.apply_resolution(4, choice)},
    5: {"name": "Imperial Taxation", "type": "RESOLUTION", "desc": "For: Lose 2 Credits or destroy 1 ship. Against: Start Player lose 3 Credits.", "effect": lambda sim, choice: sim.apply_resolution(5, choice)},
    6: {"name": "Economic Stimulus", "type": "RESOLUTION", "desc": "For: Gain 2 Credits, 1 Energy. Against: No effect.", "effect": lambda sim, choice: sim.apply_resolution(6, choice)},
    7: {"name": "Deforestation Acts", "type": "RESOLUTION", "desc": "For: Farming Worlds +1 Ore, -1 Credit. Against: Farming controllers gain 1 Influence.", "effect": lambda sim, choice: sim.apply_resolution(7, choice)},
    8: {"name": "Mining Regulations", "type": "RESOLUTION", "desc": "For: Mining Worlds -1 Ore upkeep. Against: Most Mining Worlds lose 2 Ore.", "effect": lambda sim, choice: sim.apply_resolution(8, choice)},
    9: {"name": "Xenobiology Grants", "type": "RESOLUTION", "desc": "For: Xeno/Elder controllers gain 2 Energy. Against: Xeno gain +1 Def.", "effect": lambda sim, choice: sim.apply_resolution(9, choice)},
    10: {"name": "Strict Borders", "type": "RESOLUTION", "desc": "For: Ships give +2 Def to planets. Against: Clear Spacewarps.", "effect": lambda sim, choice: sim.apply_resolution(10, choice)},
    11: {"name": "Fleet Restrictions", "type": "RESOLUTION", "desc": "For: Max fleet 3 ships. Against: No effect.", "effect": lambda sim, choice: sim.apply_resolution(11, choice)},
    12: {"name": "Shield Harmonization", "type": "RESOLUTION", "desc": "For: DEF Tech +1 tier. Against: No effect.", "effect": lambda sim, choice: sim.apply_resolution(12, choice)},
    13: {"name": "Accelerated Deployment", "type": "RESOLUTION", "desc": "For: Spawn anywhere. Against: Build costs +1 Ore.", "effect": lambda sim, choice: sim.apply_resolution(13, choice)},
    14: {"name": "Peace Accords", "type": "RESOLUTION", "desc": "For: No combat next round. Against: Most votes lose 1 ship.", "effect": lambda sim, choice: sim.apply_resolution(14, choice)},
    15: {"name": "War Effort", "type": "RESOLUTION", "desc": "For: Spend 2 Credits for +1 Attack. Against: Discard 1 Ore/Energy.", "effect": lambda sim, choice: sim.apply_resolution(15, choice)},
    16: {"name": "Resource Scarcity", "type": "RESOLUTION", "desc": "For: Only HW yields next round. Against: No effect.", "effect": lambda sim, choice: sim.apply_resolution(16, choice)},
    17: {"name": "Colonial Tax", "type": "RESOLUTION", "desc": "For: Colony Moons yield 1 Credit (not Inf). Against: Destroy all Colony Moons.", "effect": lambda sim, choice: sim.apply_resolution(17, choice)},
    18: {"name": "Void Research", "type": "RESOLUTION", "desc": "For: Reveal gives 1 Energy. Against: Unknown planets +1 Def.", "effect": lambda sim, choice: sim.apply_resolution(18, choice)},
    19: {"name": "Expansion Initiative", "type": "RESOLUTION", "desc": "For: Settlement costs -1 resource. Against: Settlement costs +1.", "effect": lambda sim, choice: sim.apply_resolution(19, choice)},
    20: {"name": "Diplomatic Immunity", "type": "RESOLUTION", "desc": "For: Cannot attack HW/Elder. Against: No effect.", "effect": lambda sim, choice: sim.apply_resolution(20, choice)},
    # Elections (ELECT PLAYER/PLANET)
    21: {"name": "Galactic Treasurer", "type": "ELECT_PLAYER", "desc": "Elected gain 3 Credits per upkeep.", "effect": lambda sim, p: sim.apply_election(21, p)},
    22: {"name": "Supreme Commander", "type": "ELECT_PLAYER", "desc": "Elected ships +1 Attack.", "effect": lambda sim, p: sim.apply_election(22, p)},
    23: {"name": "Minister of Science", "type": "ELECT_PLAYER", "desc": "Elected unlock 1 tech for free.", "effect": lambda sim, p: sim.apply_election(23, p)},
    24: {"name": "Head of Diplomacy", "type": "ELECT_PLAYER", "desc": "Elected gain 2 Influence, HW counts as 3 votes.", "effect": lambda sim, p: sim.apply_election(24, p)},
    25: {"name": "Outcast", "type": "ELECT_PLAYER", "desc": "Elected cannot vote next 2 councils.", "effect": lambda sim, p: sim.apply_election(25, p)},
    26: {"name": "Imperial Sanctions", "type": "ELECT_PLAYER", "desc": "Elected lose half resources.", "effect": lambda sim, p: sim.apply_election(26, p)},
    27: {"name": "Architect of Ruin", "type": "ELECT_PLAYER", "desc": "Elected destroy 1 adjacent opponent ship.", "effect": lambda sim, p: sim.apply_election(27, p)},
    28: {"name": "Vanguard", "type": "ELECT_PLAYER", "desc": "Elected gain 1 Victory Point.", "effect": lambda sim, p: sim.apply_election(28, p)},
    29: {"name": "Public Enemy", "type": "ELECT_PLAYER", "desc": "Attacking elected ship gives 1 Influence.", "effect": lambda sim, p: sim.apply_election(29, p)},
    30: {"name": "Propaganda Target", "type": "ELECT_PLAYER", "desc": "Elected lose all Influence tracker cubes.", "effect": lambda sim, p: sim.apply_election(30, p)},
    31: {"name": "Mining Subsidies", "type": "ELECT_PLANET", "desc": "Planets of this type yield 2 Ore immediately.", "effect": lambda sim, t: sim.apply_election_planet(31, t)},
    32: {"name": "Agricultural Grants", "type": "ELECT_PLANET", "desc": "Planets of this type yield 2 Credits immediately.", "effect": lambda sim, t: sim.apply_election_planet(32, t)},
    33: {"name": "Core Exploitation", "type": "ELECT_PLANET", "desc": "+1 Yield Native, but move cost +1 Energy.", "effect": lambda sim, t: sim.apply_election_planet(33, t)},
    34: {"name": "Cultural Preservation", "type": "ELECT_PLANET", "desc": "Type cannot be attacked or terraformed.", "effect": lambda sim, t: sim.apply_election_planet(34, t)},
    35: {"name": "Planetary Embargo", "type": "ELECT_PLANET", "desc": "Type generates no resources during upkeep.", "effect": lambda sim, t: sim.apply_election_planet(35, t)},
    36: {"name": "Subspace Anomaly", "type": "ELECT_PLANET", "desc": "Moving AWAY from type costs +1 Energy.", "effect": lambda sim, t: sim.apply_election_planet(36, t)},
    37: {"name": "Fortified Worlds", "type": "ELECT_PLANET", "desc": "Type gains +6 Defense baseline.", "effect": lambda sim, t: sim.apply_election_planet(37, t)},
    38: {"name": "Bountiful Harvest", "type": "ELECT_PLANET", "desc": "Controllers of this type gain 1 VP.", "effect": lambda sim, t: sim.apply_election_planet(38, t)},
    39: {"name": "Unstable Core", "type": "ELECT_PLANET", "desc": "Both Attacker and Defender lose 1 ship before rolls.", "effect": lambda sim, t: sim.apply_election_planet(39, t)},
    40: {"name": "Planetary Capital", "type": "ELECT_PLANET", "desc": "Type provides 3 Voting Power.", "effect": lambda sim, t: sim.apply_election_planet(40, t)},
}

OBJECTIVES = {
    # Stage 1 Public Objectives (1 VP)
    1: {"name": "Expand Borders", "stage": 1, "vp": 1, "type": "EXP", "desc": "1 Planet", "check": lambda p: len(p.planets) >= 1},
    2: {"name": "Diversify Economy", "stage": 1, "vp": 1, "type": "ECON", "desc": "Spent 5 Res", "check": lambda p: p.resources_spent_this_round >= 5},
    3: {"name": "Technological Advancement", "stage": 1, "vp": 1, "type": "TECH", "desc": "2 Lv2 Techs", "check": lambda p: len([v for v in p.tech.values() if v >= 2]) >= 2},
    4: {"name": "Build a Mighty Fleet", "stage": 1, "vp": 1, "type": "MIL", "desc": "4 Ships", "check": lambda p: len(p.ships) >= 4},
    5: {"name": "Secure the Sectors", "stage": 1, "vp": 1, "type": "EXP", "desc": "3 Sectors", "check": lambda p: len(set(s.sector_id for s in p.ships)) >= 3},
    6: {"name": "Mining Boom", "stage": 1, "vp": 1, "type": "EXP", "desc": "Mining World", "check": lambda p: any(t.type == "Mining" for t in p.planets)},
    7: {"name": "Agrarian Push", "stage": 1, "vp": 1, "type": "EXP", "desc": "Farming World", "check": lambda p: any(t.type == "Farming" for t in p.planets)},
    8: {"name": "Gas Harvesting", "stage": 1, "vp": 1, "type": "EXP", "desc": "Jovian World", "check": lambda p: any(t.type == "Jovian" for t in p.planets)},
    9: {"name": "Political Influence", "stage": 1, "vp": 1, "type": "ECON", "desc": "Spend 3 Influence", "check": lambda p: p.inf_spent_this_round >= 3},
    10: {"name": "Energy Reserves", "stage": 1, "vp": 1, "type": "ECON", "desc": "Spend 3 Energy", "check": lambda p: p.nrgy_spent_this_round >= 3},
    11: {"name": "Industrial Might", "stage": 1, "vp": 1, "type": "ECON", "desc": "Spend 3 Ore", "check": lambda p: p.ore_spent_this_round >= 3},
    12: {"name": "Wealth Accumulation", "stage": 1, "vp": 1, "type": "ECON", "desc": "Spend 3 Credits", "check": lambda p: p.cred_spent_this_round >= 3},
    13: {"name": "Fleet Consolidation", "stage": 1, "vp": 1, "type": "MIL", "desc": "2 ships on 1 sector", "check": lambda p: any(len([s for s in p.ships if s.sector_id == sid]) >= 2 for sid in range(4))},
    14: {"name": "Wormhole Navigation", "stage": 1, "vp": 1, "type": "EXP", "desc": "WarpPoint ship", "check": lambda p: any(p.sim.get_planet_at(s.sector_id, s.x, s.y) == "WarpPoint" for s in p.ships)},
    15: {"name": "Colonial Outreach", "stage": 1, "vp": 1, "type": "EXP", "desc": "Colony Moon", "check": lambda p: any(t.moon == "Colony" for t in p.planets)},
    16: {"name": "Political Titan", "stage": 1, "vp": 1, "type": "DIP", "desc": "5 Votes in round", "check": lambda p: p.max_votes_in_single_round >= 5},
    17: {"name": "Filibuster", "stage": 1, "vp": 1, "type": "DIP", "desc": "3 Inf in Council", "check": lambda p: p.council_inf_spent >= 3},
    18: {"name": "Flagship Commissioning", "stage": 1, "vp": 1, "type": "MIL", "desc": "Flagship Active", "check": lambda p: p.flagship_active and len(p.built_extensions) >= 1},

    # Stage 2 Public Objectives (2 VP)
    101: {"name": "Galactic Dominance", "stage": 2, "vp": 2, "type": "EXP", "desc": "2 Planets", "check": lambda p: len(p.planets) >= 2},
    102: {"name": "Economic Powerhouse", "stage": 2, "vp": 2, "type": "ECON", "desc": "Spent 10 Res", "check": lambda p: p.resources_spent_this_round >= 10},
    103: {"name": "Mastery of Science", "stage": 2, "vp": 2, "type": "TECH", "desc": "2 Lv4 Techs", "check": lambda p: len([v for v in p.tech.values() if v >= 4]) >= 2},
    104: {"name": "Centralize Command", "stage": 2, "vp": 2, "type": "EXP", "desc": "Shipyard and Colony", "check": lambda p: any(t.moon == "Shipyard" for t in p.planets) and any(t.moon == "Colony" for t in p.planets)},
    105: {"name": "Resource Monopoly", "stage": 2, "vp": 2, "type": "EXP", "desc": "Mining and Farming", "check": lambda p: any(t.type == "Mining" for t in p.planets) and any(t.type == "Farming" for t in p.planets)},
    106: {"name": "Atmospheric Dominance", "stage": 2, "vp": 2, "type": "EXP", "desc": "Jovian and Farming", "check": lambda p: any(t.type == "Jovian" for t in p.planets) and any(t.type == "Farming" for t in p.planets)},
    107: {"name": "Deep Core Harvesting", "stage": 2, "vp": 2, "type": "EXP", "desc": "Mining and Jovian", "check": lambda p: any(t.type == "Mining" for t in p.planets) and any(t.type == "Jovian" for t in p.planets)},
    108: {"name": "Hostile Takeover", "stage": 2, "vp": 2, "type": "MIL", "desc": "Xeno World", "check": lambda p: any(t.type == "Xenophobic" for t in p.planets)},
    109: {"name": "Ancient Secrets", "stage": 2, "vp": 2, "type": "EXP", "desc": "Elder Civilization", "check": lambda p: any(t.type == "Elder" for t in p.planets)},
    110: {"name": "Terraformer", "stage": 2, "vp": 2, "type": "EXP", "desc": "Terraformed planet", "check": lambda p: any(t.type == "Terraformed" for t in p.planets)},
    111: {"name": "Shield Tech Mastery", "stage": 2, "vp": 2, "type": "TECH", "desc": "Shields Lv3", "check": lambda p: p.tech["Shields"] >= 3},
    112: {"name": "Weapon Tech Mastery", "stage": 2, "vp": 2, "type": "TECH", "desc": "Weapons Lv3", "check": lambda p: p.tech["Weapons"] >= 3},
    113: {"name": "Engine Tech Mastery", "stage": 2, "vp": 2, "type": "TECH", "desc": "Engines Lv3", "check": lambda p: p.tech["Engines"] >= 3},
    114: {"name": "Command Tech Mastery", "stage": 2, "vp": 2, "type": "TECH", "desc": "Command Lv3", "check": lambda p: p.tech["Command"] >= 3},
    115: {"name": "Invasion Force", "stage": 2, "vp": 2, "type": "MIL", "desc": "3 Enemy Sectors", "check": lambda p: len(set(s.sector_id for s in p.ships if s.sector_id != p.id)) >= 3},
    116: {"name": "Puppet Master", "stage": 2, "vp": 2, "type": "DIP", "desc": "Elected other", "check": lambda p: p.successfully_elected_other},
    117: {"name": "Juggernaut Pattern", "stage": 2, "vp": 2, "type": "MIL", "desc": "4 Flagship Ext", "check": lambda p: p.flagship_active and len(p.built_extensions) >= 4},
    118: {"name": "Political Blockade", "stage": 2, "vp": 2, "type": "DIP", "desc": "Vote winner and Enemy Sector", "check": lambda p: p.voted_with_winner and any(s.sector_id != p.id for s in p.ships)},

    # Secret Objectives (1 VP)
    201: {"name": "Surprise Attack", "stage": "SEC", "type": "MIL", "desc": "Anomaly combat", "vp": 1, "check": lambda p: p.won_combat_near_anomaly},
    202: {"name": "Cultural Hub", "stage": "SEC", "type": "EXP", "desc": "2 same planets", "vp": 1, "check": lambda p: any(len([t for t in p.planets if t.type == pt]) >= 2 for pt in ["Mining", "Farming", "Jovian"])},
    203: {"name": "Xenology Expert", "stage": "SEC", "type": "EXP", "desc": "Xeno/Elder world", "vp": 1, "check": lambda p: any(t.type in ["Xenophobic", "Elder"] for t in p.planets)},
    204: {"name": "Aggressive Expansion", "stage": "SEC", "type": "EXP", "desc": "Enemy sector planet", "vp": 1, "check": lambda p: any(t.sector_id != p.id for t in p.planets)},
    205: {"name": "Miner Guild", "stage": "SEC", "type": "EXP", "desc": "2 Mining worlds", "vp": 1, "check": lambda p: len([t for t in p.planets if t.type == "Mining"]) >= 2},
    206: {"name": "Agrarian Society", "stage": "SEC", "type": "EXP", "desc": "2 Farming worlds", "vp": 1, "check": lambda p: len([t for t in p.planets if t.type == "Farming"]) >= 2},
    207: {"name": "Gas Giants", "stage": "SEC", "type": "EXP", "desc": "2 Jovian worlds", "vp": 1, "check": lambda p: len([t for t in p.planets if t.type == "Jovian"]) >= 2},
    208: {"name": "The Pacifist", "stage": "SEC", "type": "MIL", "desc": "0 combat this round", "vp": 1, "check": lambda p: p.combat_count_this_round == 0},
    209: {"name": "Blockade", "stage": "SEC", "type": "MIL", "desc": "Ship on enemy planet Hex", "vp": 1, "check": lambda p: any(s.sector_id != p.id and any(t.sector_id == s.sector_id and t.x == s.x and t.y == s.y for t in p.sim.get_all_planets() if isinstance(t, Planet)) for s in p.ships)},
    210: {"name": "Hoarder", "stage": "SEC", "type": "ECON", "desc": "8 of single res", "vp": 1, "check": lambda p: any(v >= 8 for v in p.resources.values())},
    211: {"name": "Tech Supremacy", "stage": "SEC", "type": "TECH", "desc": "All techs in column (Lv4)", "vp": 1, "check": lambda p: any(v >= 4 for v in p.tech.values())},
    212: {"name": "Deep Space Exploration", "stage": "SEC", "type": "EXP", "desc": "2 reveal round", "vp": 1, "check": lambda p: p.revealed_this_round >= 2},
    213: {"name": "Interloper", "stage": "SEC", "type": "EXP", "desc": "2 enemy sectors", "vp": 1, "check": lambda p: len(set(s.sector_id for s in p.ships if s.sector_id != p.id)) >= 2},
    214: {"name": "The Diplomat", "stage": "SEC", "type": "DIP", "desc": "Elder alliance round", "vp": 1, "check": lambda p: p.forged_elder_alliance_this_round},
    215: {"name": "Exterminator", "stage": "SEC", "type": "MIL", "desc": "Destroy ship", "vp": 1, "check": lambda p: p.destroyed_ship_this_round},
    216: {"name": "Voice of the Senate", "stage": "SEC", "type": "DIP", "desc": "Voted alone winner", "vp": 1, "check": lambda p: p.voted_alone_on_winner},
    217: {"name": "Capital Ship Kill", "stage": "SEC", "type": "MIL", "desc": "Destroy Flagship", "vp": 1, "check": lambda p: p.destroyed_flagship_this_round},
}
# Fill remaining (up to 45) with variants for batch simulation
for i in range(1, 46):
    if i not in OBJECTIVES:
        OBJECTIVES[i] = {"name": f"Strategic Goal {i}", "type": "GEN", "desc": "Placeholder Objective", "check": lambda p: False}

class Ship:
    def __init__(self, owner_id):
        self.owner_id = owner_id
        self.sector_id = owner_id
        self.x = 0
        self.y = 0
        self.is_flagship = False
        self.extensions = []
        self.damage_token = False

class Planet:
    def __init__(self, sector_id, x, y, type=None, is_unknown=True):
        self.sector_id = sector_id
        self.x = x
        self.y = y
        self.type = type # 'Mining', 'Farming', 'Jovian', 'Xeno', 'Elder', 'Terraformed'
        self.is_unknown = is_unknown
        self.owner_id = None
        self.moon = None # 'Colony' or 'Shipyard'

class Player:
    def __init__(self, id, civ_name, ship_flavor="Wanderer-A"):
        self.id = id
        self.civ_name = civ_name
        self.ship_flavor = ship_flavor
        self.resources = {Resource.ORE: 2, Resource.ENERGY: 3, Resource.CREDITS: 2, Resource.INFLUENCE: 1}
        self.tech = {"Weapons": 1, "Shields": 1, "Engines": 1, "Command": 1}
        self.ships = [Ship(id), Ship(id)]
        self.planets = []
        self.hand_tactics = []
        self.hand_secrets = []
        self.vp = 0
        self.votes_cast_total = 0
        self.max_votes_in_single_round = 0
        self.combat_count = 0
        self.combat_count_this_round = 0
        self.tactics_played_count = 0
        self.flagship_active = False
        self.used_tactics = []
        self.built_extensions = []
        self.vote_history = [] # List of tuples: (Round, AgendaID, VoteType, Power)
        self.claimed_objectives = set()
        self.secret_objective = None
        self.priority_mode = "GEN" # GEN, MIL, TECH, ECON, EXP
        self.target_tech = None
        self.savings_target = {Resource.CREDITS: 0, Resource.ORE: 0, Resource.ENERGY: 0, Resource.INFLUENCE: 0}
        
        # v4.0 Tracking
        self.resources_spent_this_round = 0
        self.inf_spent_this_round = 0
        self.nrgy_spent_this_round = 0
        self.ore_spent_this_round = 0
        self.cred_spent_this_round = 0
        self.council_inf_spent = 0
        self.successfully_elected_other = False
        self.voted_with_winner = False
        self.voted_alone_on_winner = False
        self.won_combat_near_anomaly = False
        self.revealed_this_round = 0
        self.destroyed_ship_this_round = False
        self.destroyed_flagship_this_round = False
        self.forged_elder_alliance_this_round = False
        self.head_of_diplomacy = False
        self.aiiji_synthesis_count = 0
    
    def get_upkeep_yield(self):
        # AI decision for homeworld: prioritize most needed or balanced
        # For simplicity in simulation, pick random if not specified, or balanced
        choices = [
            {Resource.INFLUENCE: 1},
            {Resource.CREDITS: 2},
            {Resource.ORE: 2},
            {Resource.ENERGY: 3}
        ]
        chosen = random.choice(choices)
        for res, amt in chosen.items():
            self.resources[res] += amt

        # Faction Upkeep Bonuses
        faction_data = FACTIONS[self.civ_name]
        if "upkeep" in faction_data:
            for res, amt in faction_data["upkeep"].items():
                self.resources[res] += amt

        # Planet yields
        for planet in self.planets:
            # AI decision: 2 of type or 1 Influence
            # Heuristic: If influence < 2, take influence, else take resources
            if self.resources[Resource.INFLUENCE] < 2:
                self.resources[Resource.INFLUENCE] += 1
            else:
                # Map planet type to resource
                yields = {"Mining": Resource.ORE, "Farming": Resource.CREDITS, "Jovian": Resource.ENERGY}
                if planet.type in yields:
                    self.resources[yields[planet.type]] += 2
                else:
                    self.resources[Resource.INFLUENCE] += 1 # Default for special planets
            
            # Colony Moon
            if planet.moon == "Colony":
                self.resources[Resource.INFLUENCE] += 1

    def can_afford(self, resources):
        for res, amt in resources.items():
            if self.resources.get(res, 0) < amt:
                return False
        return True

    def spend(self, resources):
        for res, amt in resources.items():
            self.resources[res] -= amt
            self.resources_spent_this_round += amt
            if res == Resource.INFLUENCE: self.inf_spent_this_round += amt
            elif res == Resource.ENERGY: self.nrgy_spent_this_round += amt
            elif res == Resource.ORE: self.ore_spent_this_round += amt
            elif res == Resource.CREDITS: self.cred_spent_this_round += amt

class ParsecSim:
    def __init__(self, players_count=4, vp_target=5, silent=False):
        self.players_count = players_count
        self.vp_target = vp_target
        self.silent = silent
        self.round_number = 1
        self.start_player_index = 0
        self.players = self.setup_players()
        self.board = self.setup_board()
        self.decks = {
            "Stage1": list(range(1, 19)),
            "Stage2": list(range(101, 119)),
            "Secrets": list(range(201, 218)),
            "Agendas": list(range(1, 41)),
            "Tactics": list(range(1, 26))
        }
        random.shuffle(self.decks["Stage1"])
        random.shuffle(self.decks["Stage2"])
        random.shuffle(self.decks["Secrets"])
        
        # Public Objective Track (3 Stage1, 2 Stage2 face down)
        self.public_objectives = [self.decks["Stage1"].pop() for _ in range(3)] + \
                                 [self.decks["Stage2"].pop() for _ in range(2)]
        self.revealed_public_count = 1
        
        # Secret Objective Draft (Deal 2, keep 1)
        for player in self.players:
            choice1 = self.decks["Secrets"].pop()
            choice2 = self.decks["Secrets"].pop()
            player.secret_objective = random.choice([choice1, choice2])
            player.sim = self
        
        self.council_unlocked = False
        self.start_player_index = 0
        self.elder_variant = True # Default to Elder Variant trigger
        self.planetary_capital = None

    def log(self, message):
        if not self.silent:
            print(message)

    def setup_players(self):
        civ_names = list(FACTIONS.keys())
        random.shuffle(civ_names)
        players = []
        for i in range(self.players_count):
            players.append(Player(i, civ_names[i], random.choice(["Wanderer-A", "Raider-B"])))
        return players

    def setup_board(self):
        board = {}
        for p_id in range(self.players_count):
            board[p_id] = {
                (0,0): Planet(p_id, 0, 0, type="Homeworld", is_unknown=False),
                (2,2): Planet(p_id, 2, 2, is_unknown=True),
                (4,0): Planet(p_id, 4, 0, is_unknown=True),
                (4,2): "WarpPoint"
            }
        return board

    def get_planet_at(self, sector_id, x, y):
        return self.board.get(sector_id, {}).get((x, y))

    def get_all_planets(self):
        planets = []
        for sid in range(self.players_count):
            for obj in self.board[sid].values():
                if isinstance(obj, Planet):
                    planets.append(obj)
        return planets

    def run(self, max_rounds=100):
        game_over = False
        while not game_over and self.round_number <= max_rounds:
            self.log(f"--- Round {self.round_number} ---")
            
            # Reset Round Metrics
            for player in self.players:
                player.resources_spent_this_round = 0
                player.inf_spent_this_round = 0
                player.nrgy_spent_this_round = 0
                player.ore_spent_this_round = 0
                player.cred_spent_this_round = 0
                player.combat_count_this_round = 0
                player.revealed_this_round = 0
                player.destroyed_ship_this_round = False
                player.destroyed_flagship_this_round = False
                player.forged_elder_alliance_this_round = False
                self.calculate_priorities(player)
            
            self.phase_upkeep()
            self.phase_upgrade()
            self.phase_movement()
            self.phase_encounter()
            
            # Phase 5: Galactic Council
            if self.council_unlocked:
                self.phase_council()
            else:
                # Check Elder Variant Trigger
                self.check_council_trigger()

            # Phase 6: Scoring
            game_over = self.phase_scoring()
            
            if self.round_number == max_rounds and not game_over:
                self.log("Max round limit reached. Resolving with current VP.")
                game_over = True
            
            if not game_over:
                self.start_player_index = (self.start_player_index + 1) % self.players_count
                self.round_number += 1
        
        if not self.silent:
            self.generate_final_report()
        
        # Return summary for batch simulation
        # Tie-breaker: Highest VP if max_rounds reached
        winner = sorted(self.players, key=lambda p: p.vp, reverse=True)[0]
        return {
            "winner_civ": winner.civ_name,
            "rounds": self.round_number,
            "vp_counts": {p.civ_name: p.vp for p in self.players},
            "extensions_built": winner.built_extensions,
            "tech_levels": winner.tech
        }

    def calculate_priorities(self, player):
        # AI strategy: Pick the 'easiest' objective from Public + Secret
        potential = self.public_objectives + [player.secret_objective]
        # Heuristic: Pick the first one that isn't claimed yet
        target_obj = None
        for oid in potential:
            if oid not in player.claimed_objectives:
                target_obj = OBJECTIVES[oid]
                break
        
        if not target_obj:
            player.priority_mode = "GEN"
            return

        player.priority_mode = target_obj["type"]
        self.log(f"Player {player.id} is now HUNTING: {target_obj['name']} ({player.priority_mode})")

        # STRATEGIC AI: The Aiiji Political Synthesis Priority
        if player.civ_name == "The Aiiji":
            player.savings_target[Resource.INFLUENCE] = 6

        # Set specific targets
        if player.priority_mode == "TECH":
            if "Weapons" in target_obj["desc"]: player.target_tech = "Weapons"
            elif "Shields" in target_obj["desc"]: player.target_tech = "Shields"
        elif player.priority_mode == "ECON":
            if "Credits" in target_obj["desc"]: player.savings_target[Resource.CREDITS] = 10
            elif "Ore" in target_obj["desc"]: player.savings_target[Resource.ORE] = 5
            elif "Energy" in target_obj["desc"]: player.savings_target[Resource.ENERGY] = 8

    def phase_upkeep(self):
        for player in self.players:
            player.get_upkeep_yield()
            # Draw Tactic Card
            if self.decks["Tactics"] and len(player.hand_tactics) < 4:
                player.hand_tactics.append(self.decks["Tactics"].pop())
            # Flagship Repair
            if player.flagship_active:
                for ship in player.ships:
                    if ship.is_flagship and ship.damage_token:
                        if ship.extensions:
                            # Rule: Jettison extension to repair
                            lost_ext = ship.extensions.pop(0)
                            ship.damage_token = False
                            self.log(f"Player {player.id} repaired Flagship by jettisoning {lost_ext}")

    def phase_upgrade(self):
        for player in self.players:
            # Resource Conversion (Sim AI: Simple conversion)
            self.solve_resource_conversion(player)

            # Buy Tech
            self.ai_buy_techs(player)

            # Build Ship
            if len(player.ships) < 4:
                cost = {Resource.ORE: 1, Resource.ENERGY: 1, Resource.CREDITS: 1, Resource.INFLUENCE: 1}
                if player.can_afford(cost):
                    player.spend(cost)
                    player.ships.append(Ship(player.id))
                    self.log(f"Player {player.id} built a ship.")

            # Designate Flagship
            if not player.flagship_active and player.ships:
                player.ships[0].is_flagship = True
                player.flagship_active = True
                self.log(f"Player {player.id} designated a Flagship.")

            # Build Extensions
            if player.flagship_active:
                for ship in player.ships:
                    if ship.is_flagship and len(ship.extensions) < 4:
                        ext_count = len(ship.extensions)
                        cost_val = [2, 4, 6, 8][ext_count]
                        # Simplified cost: check if total resources >= cost_val
                        total_res = sum(player.resources.values())
                        if total_res >= cost_val:
                            # Randomly pick an extension from catalog (1-15)
                            ext_id = random.randint(1, 15)
                            if ext_id not in ship.extensions:
                                player.resources[Resource.CREDITS] -= min(player.resources[Resource.CREDITS], cost_val)
                                ship.extensions.append(ext_id)
                                player.built_extensions.append(ext_id)
                                ext_name = EXTENSION_NAMES.get(ext_id, f"Extension {ext_id}")
                                self.log(f"Player {player.id} built {ext_name} on Flagship.")

    def solve_resource_conversion(self, player):
        faction_data = FACTIONS[player.civ_name]
        conv = faction_data.get("convert")
        if not conv: return

        convs = [conv] if isinstance(conv, tuple) else conv
        
        # Priority 1: Objective-Specific Savings
        if player.priority_mode == "ECON":
            for res, target in player.savings_target.items():
                if target > 0 and player.resources[res] < target:
                    # Look for conversion TO this resource
                    for src, dst in convs:
                        if dst == res and player.resources[src] > 0:
                            player.resources[src] -= 1
                            player.resources[dst] += 1
                            return

        # Priority 2: Get Ore if near unknown planet
        at_planet = any((s.x, s.y) in [(2,2), (4,0)] for s in player.ships)
        if at_planet and player.resources[Resource.ORE] < 3:
            for src, dst in convs:
                if dst == Resource.ORE and player.resources[src] > 0:
                    player.resources[src] -= 1
                    player.resources[Resource.ORE] += 1
                    return

        # Priority 3: General Surplus
        for src, dst in convs:
            if player.resources[src] > 4:
                player.resources[src] -= 1
                player.resources[dst] += 1

    def ai_buy_techs(self, player):
        tree = TECH_TREES[player.ship_flavor]
        for tree_name, levels in tree.items():
            # STRATEGIC AI: If hunting a specific tech, skip others
            if player.priority_mode == "TECH" and player.target_tech and tree_name != player.target_tech:
                continue

            current_lv = player.tech[tree_name]
            if current_lv < len(levels) - 1:
                next_tech = levels[current_lv + 1]
                cost = next_tech["cost"].copy()
                
                # STRATEGIC AI: Check Savings Mode
                if player.priority_mode == "ECON":
                    can_afford_and_save = True
                    for res, target in player.savings_target.items():
                        if res in cost and (player.resources[res] - cost[res]) < target:
                            can_afford_and_save = False
                    if not can_afford_and_save: continue

                # Apply Civ Discount
                faction_data = FACTIONS[player.civ_name]
                discount = faction_data.get("discount", {})
                if tree_name in discount:
                    res_type = discount[tree_name]
                    if res_type in cost and cost[res_type] > 0:
                        cost[res_type] -= 1
                
                if player.can_afford(cost):
                    player.spend(cost)
                    player.tech[tree_name] += 1
                    self.log(f"Player {player.id} upgraded {tree_name} to Level {player.tech[tree_name]}")

    def phase_movement(self):
        for player in self.players:
            # STRATEGIC AI: Targeting based on objective type
            targets_unknown = []
            targets_enemy = []
            
            for sid in range(self.players_count):
                for coord, obj in self.board[sid].items():
                    if isinstance(obj, Planet) and obj.is_unknown:
                        targets_unknown.append((sid, coord[0], coord[1]))
            
            for other_p in self.players:
                if other_p.id != player.id:
                    for p in other_p.planets:
                        targets_enemy.append((p.sector_id, p.x, p.y))

            # Prioritization
            if player.priority_mode == "MIL":
                targets = targets_enemy if targets_enemy else targets_unknown
            elif player.priority_mode == "EXP":
                targets = targets_unknown if targets_unknown else targets_enemy
            else:
                targets = targets_unknown + targets_enemy

            for ship in player.ships:
                engine_lv = player.tech["Engines"]
                engine_data = TECH_TREES[player.ship_flavor]["Engines"][engine_lv]
                cost_energy = engine_data["energy_cost"]
                max_dist = engine_data.get("dist", 3)
                
                if player.resources[Resource.ENERGY] >= cost_energy:
                    if targets:
                        target = random.choice(targets)
                        tid, tx, ty = target
                        
                        can_warp_to = []
                        if ship.x == 4 and ship.y == 2:
                            adj1 = (ship.sector_id + 1) % self.players_count
                            adj2 = (ship.sector_id - 1 + self.players_count) % self.players_count
                            can_warp_to = [adj1, adj2]
                            
                        if tid == ship.sector_id:
                            dx = tx - ship.x
                            dy = ty - ship.y
                            dist_to_go = min(max_dist, abs(dx) + abs(dy))
                            if dist_to_go > 0:
                                player.resources[Resource.ENERGY] -= cost_energy
                                while dist_to_go > 0:
                                    if dx > 0: ship.x += 1; dx -= 1
                                    elif dx < 0: ship.x -= 1; dx += 1
                                    elif dy > 0: ship.y += 1; dy -= 1
                                    elif dy < 0: ship.y -= 1; dy += 1
                                    dist_to_go -= 1
                        elif tid in can_warp_to:
                            ship.sector_id = tid
                            ship.x, ship.y = 4, 2
                        else:
                            wx, wy = 4, 2
                            dx = wx - ship.x
                            dy = wy - ship.y
                            dist_to_go = min(max_dist, abs(dx) + abs(dy))
                            if dist_to_go > 0:
                                player.resources[Resource.ENERGY] -= cost_energy
                                while dist_to_go > 0:
                                    if dx > 0: ship.x += 1; dx -= 1
                                    elif dx < 0: ship.x -= 1; dx += 1
                                    elif dy > 0: ship.y += 1; dy -= 1
                                    elif dy < 0: ship.y -= 1; dy += 1
                                    dist_to_go -= 1

    def phase_encounter(self):
        for player in self.players:
            for ship in player.ships:
                # 1. Unknown Planet Encounter
                if (ship.x, ship.y) in [(2,2), (4,0)]:
                    planet = self.board[ship.sector_id].get((ship.x, ship.y))
                    if planet and planet.is_unknown:
                        self.process_exploration(player, planet)
                
                # 2. Combat (Very simplified: check for enemy ships)
                self.check_sector_combat(ship.sector_id, ship.x, ship.y)

    def process_exploration(self, player, planet):
        roll = random.randint(1, 6)
        
        # Civilization Exploration Reroll
        bonus = FACTIONS[player.civ_name].get("bonus")
        if bonus in ["ExploreReroll", "CommandReroll", "GeneralReroll"] and roll >= 4:
            # Rule: Must accept second result. Reroll if first is "bad" (4 or 5)
            # In explorations 1-3 is good (settle), 4-5 is dangerous/special
            if roll in [4, 5]:
                self.log(f"Player {player.id} triggered Exploration Reroll (First roll: {roll})")
                roll = random.randint(1, 6)

        self.log(f"Player {player.id} exploring ({planet.x},{planet.y}). Final Roll: {roll}")
        if roll <= 3:
            # Settle (3 Ore)
            if player.resources[Resource.ORE] >= 3:
                player.resources[Resource.ORE] -= 3
                planet.is_unknown = False
                planet.type = ["Mining", "Farming", "Jovian"][roll-1]
                planet.owner_id = player.id
                player.planets.append(planet)
                self.log(f"Player {player.id} settled {planet.type} Planet.")
        elif roll == 4: # Xeno
            # Simplified Combat Reward
            planet.is_unknown = False
            planet.type = random.choice(["Mining", "Farming", "Jovian"])
            planet.owner_id = player.id
            player.planets.append(planet)
            self.log(f"Player {player.id} conquered Xenophobic Empire.")
        elif roll == 5: # Elder
            if player.resources[Resource.INFLUENCE] >= 4:
                player.resources[Resource.INFLUENCE] -= 4
                planet.is_unknown = False
                planet.type = random.choice(["Mining", "Farming", "Jovian"])
                planet.owner_id = player.id
                player.planets.append(planet)
                self.log(f"Player {player.id} allied with Elder Civ.")

    def check_sector_combat(self, sector_id, x, y):
        in_sector = []
        for p in self.players:
            for s in p.ships:
                if s.sector_id == sector_id and s.x == x and s.y == y:
                    in_sector.append((p.id, s))
        
        if len(set(v[0] for v in in_sector)) > 1:
            # Multi-player combat
            self.resolve_combat(in_sector)

    def resolve_combat(self, ships_in_sector):
        # ships_in_sector is a list of (p_id, ship)
        # 1v1 simple loop
        p_ids = sorted(list(set(v[0] for v in ships_in_sector)))
        self.log(f"Step-by-Step Combat between Player {p_ids[0]} and {p_ids[1]}...")
        
        # Calculate Strength for p1 and p2
        def get_strength(p_id, ship, other_ships, is_attacker=True):
            player = self.players[p_id]
            roll = random.randint(1, 6)
            
            # Civilization Combat Reroll
            bonus = FACTIONS[player.civ_name].get("bonus")
            # Logic: Reroll if roll is low (1, 2, or 3) and bonus matches phase
            if (is_attacker and bonus in ["AttackReroll", "GeneralReroll"]) or \
               (not is_attacker and bonus in ["DefenseReroll", "GeneralReroll"]):
                if roll <= 3:
                    self.log(f"Player {player.id} triggered Combat Reroll (First roll: {roll})")
                    roll = random.randint(1, 6)

            tech_bonus = TECH_TREES[player.ship_flavor]["Weapons"][player.tech["Weapons"]]["bonus"]
            if not is_attacker: # Shields bonus if defending
                 tech_bonus = TECH_TREES[player.ship_flavor]["Shields"][player.tech["Shields"]]["bonus"]

            ship_bonus = 2 if ship.is_flagship else 1
            if ship.is_flagship:
                if 3 in ship.extensions and not is_attacker:
                    ship_bonus += 1
                if 4 in ship.extensions and is_attacker:
                    ship_bonus += 1
                    
            other_support = len(other_ships) # +1 per other ship in sector
            total = roll + tech_bonus + ship_bonus + other_support
            
            # Purist Hegemony Defense Bonus (+1)
            if not is_attacker and bonus == "DefensePlusOne":
                total += 1

            return total, roll

        # Simple 1-round resolution for the algorithm
        s1 = next(s for s in ships_in_sector if s[0] == p_ids[0])
        s2 = next(s for s in ships_in_sector if s[0] == p_ids[1])
        
        # Tactic Usage Simulation
        for p_id in [s1[0], s2[0]]:
            if self.players[p_id].hand_tactics:
                tactic = self.players[p_id].hand_tactics.pop()
                self.players[p_id].used_tactics.append(tactic)
                self.players[p_id].tactics_played_count += 1
                t_name = TACTIC_NAMES.get(tactic, f"Tactic Card {tactic}")
                self.log(f"Player {p_id} played Tactic Card {t_name} in combat.")

        bombard_win = False
        if s1[1].is_flagship and 1 in s1[1].extensions:
            if random.randint(1, 6) >= 5:
                self.log(f"Player {s1[0]} used Orbital Bombardment Array! Destroyed defending ship.")
                bombard_win = True

        if bombard_win:
            str1, roll1 = 100, 6
            str2, roll2 = 0, 1
        else:
            s1_support = getattr(self.players[s1[0]], 'ships', [])
            s1_support = [s for s in s1_support if s.sector_id == s1[1].sector_id and s != s1[1]]
            s2_support = getattr(self.players[s2[0]], 'ships', [])
            s2_support = [s for s in s2_support if s.sector_id == s2[1].sector_id and s != s2[1]]
            
            str1, roll1 = get_strength(s1[0], s1[1], s1_support, is_attacker=True)
            str2, roll2 = get_strength(s2[0], s2[1], s2_support, is_attacker=False)
        
        self.log(f"P{s1[0]} rolls {roll1} (Total {str1}) vs P{s2[0]} rolls {roll2} (Total {str2})")
        
        winner_id = None
        loser_id = None
        loser_ship = None
        
        if str1 > str2:
            self.log(f"Winner: P{s1[0]}")
            winner_id = s1[0]
            loser_id = s2[0]
            loser_ship = s2[1]
            # Hijack Planet if at enemy planet
            p_at = self.board[s1[1].sector_id].get((s1[1].x, s1[1].y))
            if isinstance(p_at, Planet) and p_at.owner_id == s2[0]:
                p_at.owner_id = s1[0]
                self.players[s1[0]].planets.append(p_at)
                self.players[s2[0]].planets.remove(p_at)
                self.log(f"Player {s1[0]} hijacked planet from Player {s2[0]}")
        elif str2 > str1:
            self.log(f"Winner: P{s2[0]}")
            winner_id = s2[0]
            loser_id = s1[0]
            loser_ship = s1[1]
        else:
            self.log("Tie! Both ships destroyed!")
            if s1[1].is_flagship and 2 in s1[1].extensions:
                self.log(f"P{s1[0]} Flagship protected by Command Carrier Bay.")
            else:
                if s1[1] in self.players[s1[0]].ships:
                    self.players[s1[0]].ships.remove(s1[1])
            if s2[1].is_flagship and 2 in s2[1].extensions:
                self.log(f"P{s2[0]} Flagship protected by Command Carrier Bay.")
            else:
                if s2[1] in self.players[s2[0]].ships:
                    self.players[s2[0]].ships.remove(s2[1])
            return # Combat ends on a tie
        
        # Scoring Hooks: Surprise Attack (201), Exterminator (215), Capital Ship Kill (217)
        if winner_id is not None:
            w_player = self.players[winner_id]
            l_player = self.players[loser_id]
            
            w_player.won_combat_near_anomaly = True # Simplified for sim
            self.check_immediate_score(w_player, 201)
            
            if loser_ship.is_flagship and not loser_ship.damage_token:
                loser_ship.damage_token = True
                self.log(f"Combat Result: P{winner_id} wins. P{loser_id}'s Flagship sustained a Damage Token!")
            else:
                w_player.destroyed_ship_this_round = True
                self.check_immediate_score(w_player, 215)
                
                if loser_ship.is_flagship:
                    w_player.destroyed_flagship_this_round = True
                    self.check_immediate_score(w_player, 217)
                    l_player.flagship_active = False

                self.players[loser_id].ships.remove(loser_ship)
                self.log(f"Combat Result: P{winner_id} wins. P{loser_id} ship destroyed.")
                
                # Flagship Expansion: Scavenger Harvesters
                w_ship = s1[1] if winner_id == s1[0] else s2[1]
                if w_ship.is_flagship and 10 in w_ship.extensions:
                    self.players[winner_id].resources[Resource.ORE] += 1
        
        if winner_id is not None:
            self.players[winner_id].combat_count += 1
            self.players[winner_id].combat_count_this_round += 1

    def check_council_trigger(self):
        # Elder Variant: Council triggers if anyone controls an Elder Civilization or all boards revealed
        triggered = any(any(t.type == "Elder" for t in p.planets) for p in self.players)
        if not triggered:
            # Failsafe: All unknown planets revealed?
            all_revealed = True
            for sid in range(self.players_count):
                for obj in self.board[sid].values():
                    if isinstance(obj, Planet) and obj.is_unknown:
                        all_revealed = False
                        break
            if all_revealed: triggered = True
        
        if triggered:
            self.council_unlocked = True
            self.log("### Galactic Council Convened! (Elder Variant Triggered) ###")

    def phase_council(self):
        if not self.decks["Agendas"]:
            self.decks["Agendas"] = list(range(1, 41))
            random.shuffle(self.decks["Agendas"])

        agenda_id = self.decks["Agendas"].pop()
        agenda = AGENDAS[agenda_id]
        self.log(f"Council Convened: {agenda['name']} - {agenda['desc']}")

        # Voting Power Calculation
        votes = {} # Player Index -> Total Power
        for idx, p in enumerate(self.players):
            power = 0
            # 1. Passive Planet Power
            for planet in p.planets:
                p_power = 0
                if planet.type == "Homeworld": p_power = 3 if p.head_of_diplomacy else 1
                elif planet.type == "Elder": p_power = 3
                elif planet.type == "Xenophobic": p_power = 2
                else: p_power = 1
                
                if planet.type == self.planetary_capital: p_power = 3
                if getattr(planet, 'moon', None) == "Colony": p_power += 1
                power += p_power
                
            # Flagship Expansion: Galactic Broadcast Node (+3 Votes)
            if any(s.is_flagship and 13 in s.extensions for s in p.ships):
                power += 3
            
            # 2. Influence Spending (Sim AI: Spend if high importance or randomized)
            inf_to_spend = min(p.resources[Resource.INFLUENCE], random.randint(0, 3))
            p.spend({Resource.INFLUENCE: inf_to_spend})
            p.council_inf_spent = inf_to_spend
            power += inf_to_spend
            votes[idx] = power
            p.votes_cast_total += power
            p.max_votes_in_single_round = power
            p.vote_history.append((self.round_number, agenda_id, "VOTE", power))

        # Resolution (Start player tiebreaks)
        # For simplicity, AI votes FOR or chooses random player for election
        vote_tally = {"FOR": 0, "AGAINST": 0}
        if agenda["type"] == "RESOLUTION":
            for idx, power in votes.items():
                choice = random.choice(["FOR", "AGAINST"])
                vote_tally[choice] += power
            winning_choice = "FOR" if vote_tally["FOR"] >= vote_tally["AGAINST"] else "AGAINST"
            self.log(f"Resolution Outcome: {winning_choice} (For {vote_tally['FOR']} vs Against {vote_tally['AGAINST']})")
            agenda["effect"](self, winning_choice == "FOR")
        else:
            # ELECT Player/Planet
            p_tally = {pid: 0 for pid in range(self.players_count)}
            for idx, power in votes.items():
                vote_for = random.randint(0, self.players_count - 1)
                p_tally[vote_for] += power
            elected_idx = sorted(p_tally.items(), key=lambda x: x[1], reverse=True)[0][0]
            self.log(f"Election Outcome: Player {elected_idx} Elected")
            agenda["effect"](self, self.players[elected_idx])
            for idx, p in enumerate(self.players):
                if p_tally[idx] >= 10: # Filibuster / Lobbyist logic
                    pass

    def apply_resolution(self, agenda_id, is_for):
        # Simplified implementations
        if is_for:
            self.log(f"Resolution {agenda_id} enforced.")
        else:
            self.log(f"Resolution {agenda_id} rejected.")

    def apply_election(self, agenda_id, elected_player):
        self.log(f"Player {elected_player.id} received mandate {agenda_id}.")
        if agenda_id == 28: # Vanguard: +1 VP
            elected_player.vp += 1
        elif agenda_id == 24: # Head of Diplomacy
            elected_player.resources[Resource.INFLUENCE] += 2
            for p in self.players: p.head_of_diplomacy = False
            elected_player.head_of_diplomacy = True

    def apply_election_planet(self, agenda_id, planet_type):
        self.log(f"Planets of type {planet_type} received mandate {agenda_id}.")
        if agenda_id == 40: # Planetary Capital
            self.planetary_capital = planet_type

    def check_immediate_score(self, player, objective_id):
        if objective_id in player.claimed_objectives: return
        if OBJECTIVES[objective_id]["check"](player):
            player.claimed_objectives.add(objective_id)
            player.vp += OBJECTIVES[objective_id]["vp"]
            self.log(f"!!! Player {player.id} scored ACTION PHASE Objective: {OBJECTIVES[objective_id]['name']} !!!")

    def phase_scoring(self) -> bool:
        for player in self.players:
            # 1 VP per planet (Legacy rule or expansion choice? Expansion says VP per Objective).
            # We'll use 1 VP per Planet as an in-built baseline if requested, but officially it's per Objective.
            player.vp = len(player.planets)
            
            scored_public = False
            scored_secret = False
            
            # Check Revealed Public Objectives (Limit to ONE)
            active_publics = self.public_objectives[:self.revealed_public_count]
            for obj_id in active_publics:
                if obj_id not in player.claimed_objectives:
                    if OBJECTIVES[obj_id]["check"](player):
                        player.claimed_objectives.add(obj_id)
                        player.vp += OBJECTIVES[obj_id]["vp"]
                        self.log(f"Player {player.id} scored ONE Public Objective: {OBJECTIVES[obj_id]['name']}")
                        scored_public = True
                        break # Rule: Exactly ONE Public per round
            
            # Check Secret Objective (Limit to ONE)
            if player.secret_objective not in player.claimed_objectives:
                if OBJECTIVES[player.secret_objective]["check"](player):
                    player.claimed_objectives.add(player.secret_objective)
                    player.vp += OBJECTIVES[player.secret_objective]["vp"]
                    self.log(f"Player {player.id} scored ONE Secret Objective: {OBJECTIVES[player.secret_objective]['name']}")
                    scored_secret = True

            # --- AIIJI MASTER PASSIVES ---
            if player.civ_name == "The Aiiji":
                # 1. Political Synthesis: Spend scaling Inf for an objective
                cost_infl = 6 + (player.aiiji_synthesis_count * 3)
                if not scored_public and player.resources[Resource.INFLUENCE] >= cost_infl:
                    active_publics = self.public_objectives[:self.revealed_public_count]
                    for obj_id in active_publics:
                        if obj_id not in player.claimed_objectives:
                            player.resources[Resource.INFLUENCE] -= cost_infl
                            player.claimed_objectives.add(obj_id)
                            player.aiiji_synthesis_count += 1
                            self.log(f"[Aiiji] Political Synthesis: Spent {cost_infl} Influence to claim {OBJECTIVES[obj_id]['name']}")
                            scored_public = True
                            break
                
                # 2. Voice of the Galaxy: +1 VP for 12+ total votes (Cumulative)
                if player.votes_cast_total >= 12 and "AiijiVP" not in player.claimed_objectives:
                    player.claimed_objectives.add("AiijiVP")
                    self.log("[Aiiji] Voice of the Galaxy: +1 VP granted for 12+ total votes.")

            # Recalculate VP from all claimed objectives (Persistent points)
            player.vp = len(player.planets)
                
            for oid in player.claimed_objectives:
                if oid == "AiijiVP":
                    player.vp += 1
                else:
                    player.vp += OBJECTIVES[oid]["vp"]
            
            if player.vp >= self.vp_target:
                self.log(f"*** PLAYER {player.id} WINS! (VP: {player.vp}) ***")
                return True
        
        # End of Scoring: Reveal next public objective
        if self.revealed_public_count < len(self.public_objectives):
            self.revealed_public_count += 1
            next_obj = OBJECTIVES[self.public_objectives[self.revealed_public_count-1]]
            self.log(f"Next Public Objective Revealed: {next_obj['name']}")
            
        return False

    def generate_final_report(self):
        self.log("\n## Simulation Results (Summary Table)\n")
        self.log("| Player | Civilization | VP | Result | Extensions Count | Tactics Played | Total Votes |")
        self.log("|---|---|---|---|---|---|---|")
        for p in self.players:
            res = "Winner" if p.vp >= self.vp_target else "Loser"
            self.log(f"| P{p.id} | {p.civ_name} | {p.vp} | {res} | {len(p.built_extensions)} | {len(p.claimed_objectives)} | {p.votes_cast_total} |")

        self.log("\n### Detailed Action Logs")
        for p in self.players:
            self.log(f"\n#### Player {p.id} ({p.civ_name})")
            ext_names = [EXTENSION_NAMES.get(eid, f"Ext {eid}") for eid in p.built_extensions]
            self.log(f"- **Extensions Built:** {', '.join(ext_names) if ext_names else 'None'}")
            
            tactic_names = [TACTIC_NAMES.get(tid, f"Tactic {tid}") for tid in p.used_tactics]
            self.log(f"- **Tactics Used:** {', '.join(tactic_names) if tactic_names else 'None'}")
            
            self.log("- **Council Vote History:**")
            if not p.vote_history:
                self.log("  - No votes cast.")
            for v in p.vote_history:
                a_name = AGENDAS.get(v[1], {}).get("name", f"Agenda {v[1]}")
                self.log(f"  - Round {v[0]} | {a_name} | Vote: {v[2]} | Strength: {v[3]}")

if __name__ == "__main__":
    sim = ParsecSim(players_count=4, vp_target=5)
    sim.run()
