import random

class Resource:
    ORE = "Ore"
    ENERGY = "Energy"
    CREDITS = "Credits"
    INFLUENCE = "Influence"
    ALL = [ORE, ENERGY, CREDITS, INFLUENCE]

FACTIONS = {
    "Sharnak Imperium": {"convert": (Resource.CREDITS, Resource.ORE), "discount": {"Weapons": Resource.ORE}, "bonus": "AttackReroll"},
    "The Conversation": {"convert": (Resource.INFLUENCE, Resource.CREDITS), "discount": {"Engines": Resource.ORE, "Command": Resource.CREDITS}, "bonus": None},
    "Wulfram Collective": {"convert": (Resource.ORE, Resource.INFLUENCE), "upkeep": {Resource.ORE: 1}, "bonus": "AttackReroll"},
    "Rim Worlds Combine": {"convert": (Resource.ORE, Resource.CREDITS), "upkeep": {Resource.CREDITS: 1}, "bonus": "ExploreReroll"},
    "The Aiiji": {"convert": (Resource.INFLUENCE, Resource.CREDITS), "upkeep": "1d3Credits", "bonus": "CommandReroll"},
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

AGENDA_NAMES = {
    1: "Wormhole Tolls", 2: "Demilitarized Zones", 3: "Arms Trade", 4: "Technological Subsidies",
    5: "Imperial Taxation", 6: "Economic Stimulus", 7: "Deforestation Acts", 8: "Mining Regulations",
    9: "Xenobiology Grants", 10: "Strict Borders", 11: "Fleet Restrictions", 12: "Shield Harmonization",
    13: "Accelerated Deployment", 14: "Peace Accords", 15: "War Effort", 16: "Resource Scarcity",
    17: "Colonial Tax", 18: "Void Research", 19: "Expansion Initiative", 20: "Diplomatic Immunity",
    21: "Galactic Treasurer", 22: "Supreme Commander", 23: "Minister of Science", 24: "Head of Diplomacy",
    25: "Outcast", 26: "Imperial Sanctions", 27: "Architect of Ruin", 28: "Vanguard",
    29: "Public Enemy", 30: "Propaganda Target", 31: "Mining Subsidies", 32: "Agricultural Grants",
    33: "Core Exploitation", 34: "Cultural Preservation", 35: "Planetary Embargo", 36: "Subspace Anomaly",
    37: "Fortified Worlds", 38: "Bountival Harvest", 39: "Unstable Core", 40: "Planetary Capital",
    41: "Flagship Registration", 42: "Classified Objectives Disclosure", 43: "Admiral of the Fleet",
    44: "Public Enemy (Elect Player)", 45: "Public Hero"
}

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
        self.combat_count = 0
        self.tactics_played_count = 0
        self.flagship_active = False
        self.used_tactics = []
        self.built_extensions = []
        self.vote_history = [] # List of tuples: (Round, AgendaID, VoteType, Power)
    
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
            if faction_data["upkeep"] == "1d3Credits":
                self.resources[Resource.CREDITS] += random.randint(1, 3)
            else:
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

    def can_afford(self, cost_dict):
        for res, amt in cost_dict.items():
            if self.resources.get(res, 0) < amt:
                return False
        return True

    def spend(self, cost_dict):
        for res, amt in cost_dict.items():
            self.resources[res] -= amt

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
            "Agendas": list(range(1, 46)),
            "PublicObjectives": list(range(1, 46)),
            "Tactics": list(range(1, 26))
        }

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

    def run(self, max_rounds=500):
        game_over = False
        while not game_over and self.round_number <= max_rounds:
            self.log(f"--- Round {self.round_number} ---")
            self.phase_upkeep()
            self.phase_upgrade()
            self.phase_movement()
            self.phase_encounter()
            self.phase_council()
            
            if self.round_number == max_rounds:
                self.log("Max round limit reached. Resolving with current VP.")
                game_over = True
            else:
                game_over = self.phase_scoring()
            
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
        
        # Priority 1: Get Ore if near unknown planet
        at_planet = any((s.x, s.y) in [(2,2), (4,0)] for s in player.ships)
        if at_planet and player.resources[Resource.ORE] < 3:
            for src, dst in convs:
                if dst == Resource.ORE and player.resources[src] > 0:
                    player.resources[src] -= 1
                    player.resources[Resource.ORE] += 1
                    return

        for src, dst in convs:
            if player.resources[src] > 4:
                player.resources[src] -= 1
                player.resources[dst] += 1

    def ai_buy_techs(self, player):
        tree = TECH_TREES[player.ship_flavor]
        for tree_name, levels in tree.items():
            current_lv = player.tech[tree_name]
            if current_lv < len(levels) - 1:
                next_tech = levels[current_lv + 1]
                cost = next_tech["cost"].copy()
                
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
            # Aggressive Targeting
            targets = []
            # 1. Unknown planets (Any sector)
            for sid in range(self.players_count):
                for coord, obj in self.board[sid].items():
                    if isinstance(obj, Planet) and obj.is_unknown:
                        targets.append((sid, coord[0], coord[1]))
            # 2. Enemy planets
            for other_p in self.players:
                if other_p.id != player.id:
                    for p in other_p.planets:
                        targets.append((p.sector_id, p.x, p.y))

            for ship in player.ships:
                engine_lv = player.tech["Engines"]
                engine_data = TECH_TREES[player.ship_flavor]["Engines"][engine_lv]
                cost_energy = engine_data["energy_cost"]
                
                if player.resources[Resource.ENERGY] >= cost_energy:
                    if targets:
                        # Stochastic Choice: Pick from top targets with some randomness
                        # For simplicity, shuffle targets or pick random if multiple
                        random.shuffle(targets)
                        tid, tx, ty = targets[0]
                        ship.sector_id, ship.x, ship.y = tid, tx, ty
                        player.resources[Resource.ENERGY] -= cost_energy

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
        self.log(f"Player {player.id} exploring ({planet.x},{planet.y}). Roll: {roll}")
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
        def get_strength(p_id, ship, other_ships):
            player = self.players[p_id]
            roll = random.randint(1, 6)
            tech_bonus = TECH_TREES[player.ship_flavor]["Weapons"][player.tech["Weapons"]]["bonus"]
            ship_bonus = 2 if ship.is_flagship else 1
            other_support = len(other_ships) # +1 per other ship in sector
            total = roll + tech_bonus + ship_bonus + other_support
            return total, roll

        # Simple 1-round resolution for the algorithm
        s1 = ships_in_sector[0]
        s2 = ships_in_sector[1]
        
        # Tactic Usage Simulation
        for p_id in [s1[0], s2[0]]:
            if self.players[p_id].hand_tactics:
                tactic = self.players[p_id].hand_tactics.pop()
                self.players[p_id].used_tactics.append(tactic)
                self.players[p_id].tactics_played_count += 1
                t_name = TACTIC_NAMES.get(tactic, f"Tactic Card {tactic}")
                self.log(f"Player {p_id} played Tactic Card {t_name} in combat.")

        str1, roll1 = get_strength(s1[0], s1[1], [])
        str2, roll2 = get_strength(s2[0], s2[1], [])
        
        self.log(f"P{s1[0]} rolls {roll1} (Total {str1}) vs P{s2[0]} rolls {roll2} (Total {str2})")
        
        if str1 > str2:
            self.log(f"Winner: P{s1[0]}")
            self.players[s2[0]].ships.remove(s2[1])
            # Hijack Planet if at enemy planet
            p_at = self.board[s1[1].sector_id].get((s1[1].x, s1[1].y))
            if isinstance(p_at, Planet) and p_at.owner_id == s2[0]:
                p_at.owner_id = s1[0]
                self.players[s2[0]].planets.remove(p_at)
                self.players[s1[0]].planets.append(p_at)
                self.log(f"Player {s1[0]} hijacked planet from Player {s2[0]}")
        elif str2 > str1:
            self.log(f"Winner: P{s2[0]}")
            self.players[s1[0]].ships.remove(s1[1])

    def phase_council(self):
        if self.round_number < 2: return # Trigger logic
        
        if not self.decks["Agendas"]:
            self.log("Agenda deck empty. Reshuffling...")
            self.decks["Agendas"] = list(range(1, 46))
            random.shuffle(self.decks["Agendas"])

        agenda = self.decks["Agendas"].pop()
        agenda_name = AGENDA_NAMES.get(agenda, f"Agenda {agenda}")
        self.log(f"Council Convened: {agenda_name}")

        # Categorize Agenda Type
        if (1 <= agenda <= 20) or (41 <= agenda <= 42):
            agenda_type = "RESOLUTION"
        elif (21 <= agenda <= 30) or (43 <= agenda <= 45):
            agenda_type = "ELECT_PLAYER"
        elif (31 <= agenda <= 40):
            agenda_type = "ELECT_PLANET"
        else:
            agenda_type = "RESOLUTION" # Fallback

        # Calculate voting power
        for player in self.players:
            power = 1 # Homeworld
            power += len(player.planets)
            # Flagship Bonus
            if 13 in player.built_extensions: # Galactic Broadcast Node
                power += 3
            # Spend Influence? (AI choice: spend up to 2)
            can_spend = min(player.resources[Resource.INFLUENCE], 2)
            player.resources[Resource.INFLUENCE] -= can_spend
            power += can_spend
            
            # Decide Vote Value based on Type
            if agenda_type == "RESOLUTION":
                vote_val = random.choice(["FOR", "AGAINST"])
            elif agenda_type == "ELECT_PLAYER":
                # Choose a target player (maybe exclude self if it's a negative agenda?)
                target_p = random.randint(0, len(self.players)-1)
                vote_val = f"P{target_p}"
            elif agenda_type == "ELECT_PLANET":
                vote_val = random.choice(["MINING", "FARMING", "JOVIAN", "TERRAFORMED", "XENOPHOBIC", "ELDER"])
            
            player.vote_history.append((self.round_number, agenda, vote_val, power))
            player.votes_cast_total += power
            self.log(f"Player {player.id} cast {power} votes: {vote_val}.")

    def phase_scoring(self) -> bool:
        # Objective logic: 1 VP per planet + bonuses for tech/ships
        for player in self.players:
            player.vp = len(player.planets)
            # Add bonus VP for high tech or large fleet to accelerate game
            if player.tech["Weapons"] >= 3: player.vp += 1
            if len(player.ships) >= 4: player.vp += 1
            
            if player.vp >= self.vp_target:
                self.log(f"*** PLAYER {player.id} WINS! (VP: {player.vp}) ***")
                return True
        return False

    def generate_final_report(self):
        self.log("\n## Simulation Results (Summary Table)\n")
        self.log("| Player | Civilization | VP | Result | Extensions Count | Tactics Played | Total Votes |")
        self.log("|---|---|---|---|---|---|---|")
        for p in self.players:
            res = "Winner" if p.vp >= self.vp_target else "Loser"
            self.log(f"| P{p.id} | {p.civ_name} | {p.vp} | {res} | {len(p.built_extensions)} | {len(p.used_tactics)} | {p.votes_cast_total} |")

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
                a_name = AGENDA_NAMES.get(v[1], f"Agenda {v[1]}")
                self.log(f"  - Round {v[0]} | {a_name} | Vote: {v[2]} | Strength: {v[3]}")

if __name__ == "__main__":
    sim = ParsecSim(players_count=4, vp_target=5)
    sim.run()
