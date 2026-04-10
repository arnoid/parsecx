# Parsec X: Master Edition Rulebook

## Table of Contents
1. [Components](#1-components)
2. [Setup](#2-setup)
3. [Phase Structure](#3-the-galactic-round-phase-structure)
4. [The Tech Tree](#4-the-tech-tree)
5. [Civilizations](#5-civilizations-of-the-parsec)
6. [Flagship Appendix](#6-flagship-appendix)
- [Appendix A: Advanced Tactics](#appendix-a-advanced-tactics-expansion)
- [Appendix B: Flagships](#appendix-b-flagship-expansion)
- [Appendix C: Galactic Council](#appendix-c-galactic-council-expansion)
- [Appendix D: Galactic Objectives](#appendix-d-galactic-objectives-expansion)

Welcome to **Parsec X**, a micro-4X space simulation game for 2 to 4 players. This Master Edition rulebook integrates the base rules with the *Advanced Tactics*, *Flagships*, *Galactic Council*, and *Galactic Objectives* expansions, reflecting the latest V1.1 balance adjustments.

---

## 1. Components
- **Sector Map Cards:** 4 double-sided cards forming the 3x5 grid sectors.
- **Ship Cards & Tech Tree Cards:** 1 per player.
- **Civilization Cards:** 8 unique factions (Sharnak, The Conversation, Wulfram, Rim Worlds, Aiiji, Altair, Gaian, Purist).
- **Cubes:** 15 per player (11 for tracking/tech, 4 for ships).
- **Moon Cubes:** 8 Black (Shipyard), 8 White (Colony).
- **Objective Decks:** Stage 1, Stage 2, and Secret.
- **Agenda Deck:** 45 cards for the Galactic Council.
- **Flagship Extension Board:** 1 per player.
- **Tactic Deck:** 30 cards for advanced maneuvers.
- **Dice:** Ten 6-sided dice (10d6).

## 1.1 Game Expansions
Some actions require Parsec X expansions. List of expansions available: 
- Advanced Tactics
  - Marked as **[ATac]**
- Flagships
  - Marked as **[Flag]**
- Galactic Council
  - Marked as **[GalCon]**
- Galactic Objectives
  - Marked as **[GalObj]**

---

## 2. Setup
1. **Map:** Arrange 4 Sector Map cards based on player count. Each sector is a **3x5 grid**.
2. **Civilization:** Each player receives 2 Civilization cards, chooses one, and discards the other.
3. **Hull Choice:** Choose either a **Wanderer** or **Raider** hull and receive your Tech Tree card.
4. **Starting Fleet:** Each player places 2 ships (cubes) on their Homeworld sector.
5. **Resources:** Place tracking cubes on the starting resource markers on your Ship Card.
6. **[GalObj]** **Objectives:**
    - Prepare the Stage 1 and Stage 2 Public Objective decks. The public objective track starts empty; one new objective will be added to the board each turn (see Appendix D).
    - Deal 2 Secret Objectives to each player; they keep one.
7. **[Flag]** **Flagship:** Every player starts with the right to designate one of their ships as a Flagship during the game.

---

## 3. The Galactic Round (Phase Structure)
A round consists of six sequential phases. Phases 1 and 2 are simultaneous; 3, 4, and 5 proceed in clockwise order starting with the Start Player.

### Phase 1: Upkeep
- **Resource Gathering:** Collect native yields from your Homeworld and any controlled planets.
- **[ATac]** **Tactic Cards:** Draw 1 Tactic Card from the deck.
- **[Flag]** **Jettison Flagship Extensions:** You may jettison one Flagship Extension to remove a Damage Token from your Flagship.

### Phase 2: Upgrade
- **Ship Construction:** Pay the indicated Ore/Credit cost to build new ships.
- **Tech Research:** Pay resources to move cubes down your Tech Tree (Engines, Command, Shields, Weapons).
- **[Flag]** **Flagship Designation:** If you have no Flagship, designate an existing ship as one.
- **[Flag]** **Extensions:** Buy unique modules for your Flagship (Cost: 2/4/6/8 resources for slots 1/2/3/4).

### Phase 3: Movement
- **Grid Travel:** Move ships orthogonally. Movement costs **Energy**.
- **Distance:** Your movement limit is defined by your Engines tech (e.g., Level 1 = 3 spaces).
- **Spacewarps:** If a ship is on a Spacewarp icon (4, 2), it may jump to a Spacewarp on an **adjacent** sector (clockwise or counter-clockwise).

### Phase 4: Encounter
- **Exploration:** If a ship enters a sector containing an Unknown Planet (a planet with no type defined yet), the player rolls 1d6 and consults the **Planetary Atlas** below to determine the outcome.
- **Combat:** If you occupy a sector with an opponent's ship or planet, combat occurs.
  - **Strength:** Roll 1d6 + Weapons/Shields tech + Support (+1 for every additional friendly ship in the sector).
  - **[Flag]** **Flagships:** Count as 2 ships for support and have native strength bonuses.
  - **Ties:** If totals are equal, **both ships are destroyed** (**[Flag]** unless protected by a *Command Carrier Bay*).
  - **[ATac]** **Retreat:** Before rolls, either the Attacker or Defender may discard **1 Resource** to retreat to an adjacent safe sector. No combat die is rolled.

#### Planetary Atlas

When encountering an Unknown Planet, roll 1d6 and resolve the result:

| Roll | Discovery | Settlement | Upkeep Yield |
|------|-----------|------------|--------------|
| 1 | Mining World | 3 Credits | 2 Ore or 1 Influence |
| 2 | Farming World | 3 Influence | 2 Credits or 1 Influence |
| 3 | Jovian World | 3 Ore | 2 Energy or 1 Influence |
| 4 | Xenophobic Empire | Combat (see below) | Determined by conquest roll |
| 5 | Elder Civilization | Diplomatic Alliance (see below) | Determined by alliance roll |
| 6 | Terraforming Candidate | Player's choice (see below) | Based on chosen type |

**Rolls 1–3 (Standard Worlds):** The player discovers the planet type and may immediately settle it by paying the listed settlement cost. If settled, the player places a Civilization Marker on the planet and will collect its Upkeep Yield each round during Phase 1.

**Roll 4 (Xenophobic Empire):** The player encounters a warlike force that will not negotiate. The player must attack the planet in Combat. The Xenophobic Empire adds **+5 to its Defense Strength** die roll. If the player fails and their ship is destroyed, the Xenophobic Empire remains on the board — this player or any other player may fly a ship to the location on subsequent turns and attempt to conquer it again. If the player is successful, they:
1. Roll 1d6 to determine the planet type they now control: **1–2** = Mining World, **3–4** = Farming World, **5–6** = Jovian World.
2. Randomly draw a Moon cube. **White** = Colony Moon (grants +1 Influence during Upkeep). **Black** = Shipyard Moon.
3. The player does **not** pay any settlement resources — the planet is claimed by right of conquest.

> **Sharnak Imperium Special Rule:** When Sharnak attacks a Xenophobic Empire, they apply their *Combat Attack Reroll* bonus (reroll if 1–3) and gain a **+2 Attack Strength bonus** vs. Xenophobic Empires. See Section 5 for details.

**Roll 5 (Elder Civilization):** The player may attempt a Diplomatic Alliance with this ancient civilization. The player must spend Influence equal to a **1d3+2** roll (resulting in a cost of 3, 4, or 5 Influence). If the player can pay the cost, the alliance is forged:
1. Roll 1d6 to determine the planet type: **1–2** = Mining World, **3–4** = Farming World, **5–6** = Jovian World.
2. There are **no Moons** for Elder Civilization planets.
3. The planet provides **+3 Passive Voting Power** in the Galactic Council.

If the player cannot or chooses not to pay, they lose **1 Influence** and the Elder Civilization remains available — any player may attempt to forge an alliance on subsequent turns.

**Roll 6 (Terraforming Candidate):** The player discovers a barren world suitable for terraforming. The player may choose to terraform it into any standard planet type by paying the corresponding cost:
- **Mining World:** 4 Credits + 1 Influence
- **Farming World:** 4 Energy + 1 Influence
- **Jovian World:** 4 Ore + 1 Influence

If terraformed, the player also randomly draws a Moon cube. **White** = Colony Moon (+1 Influence during Upkeep). **Black** = Shipyard Moon. Terraforming is optional — if the player declines, the Terraforming Candidate remains on the board and any player may attempt terraforming on later turns.

### **[GalCon]** Phase 5: Galactic Council**
*Triggered once an Elder Civilization is claimed or all planets are revealed.*
1. **Convene:** The Start Player draws 1 Agenda card.
2. **Voting:** Players vote using **Influence** (1:1) and **Passive Voting Power** from planets.
   - *Homeworld:* +1 Vote (or +3 if Head of Diplomacy).
   - *Planetary Capital:* +3 Votes.
   - *Elder/Xenophobic:* +3 / +2 Votes.
3. **Resolution:** Highest total passes immediately.

### **[GalObj]** Phase 6: Scoring**
- **[GalObj]** **Public Objectives:** If you meet the criteria, place a cube on a Public Objective.
- **[GalObj]** **Secret Objectives:** Reveal and score one Secret Objective.
- **Victory:** The game ends after **Round 10**. The player with the highest Victory Points is the winner. If multiple players share the high score, they share a joint victory.

> **Altair Divide Special Rule:** During Scoring, the Altair Divide's Flagship sector counts as 1 controlled Mining World for the purpose of **EXP-type objectives only** (e.g. *Expand Borders*, *Galactic Dominance*, *Cultural Hub*, *Miner's Guild*). The Flagship must be active and on the board. See Section 5 for full details.

---

## 4. The Tech Tree
Players choose one of two hull types at setup, which determines their starting stats and technological progression.

### Wanderer (Focus: Efficiency & Logistics)
- **Weapons (ATT)**: Rail Gun (+1) ➔ Gauss Missile (+3: 1C, 1E, 3O) ➔ Fusion Cannon (+5: 2C, 2E, 2O) ➔ Antimatter Cannon (+6: 4C, 3E, 1O)
- **Shields (DEF)**: Force Shield (+1) ➔ Phase Shield (+2: 3C, 1E) ➔ Nano-Hull (+3: 4C, 2E) ➔ Nano-Cloud (+5: 6C, 3E)
- **Engines (ENG)**: Fusion (3 hex, 2E) ➔ Tachyon (3 hex, 1E: 3C, 1O) ➔ Ehrenhaft (5 hex, 1E: 3C, 2O) ➔ Stellar (5 hex, 1E: 4C, 3O)
- **Command (COM)**: Navicomm ➔ Veteran Captain (+1 roll cost 1I: 2C, 2E, 1I) ➔ Drone AI (Reroll cost 1E: 3C, 2E, 2I) ➔ Shipmind (Double Reroll: 4C, 2E, 2I)

### Raider (Focus: Combat & Aggression)
- **Weapons (ATT)**: Rail Gun (+2) ➔ Gauss Missile (+4: 3C, 1E, 3O) ➔ Fusion Cannon (+6: 3C, 2E, 3O) ➔ Antimatter Cannon (+7: 3C, 3E, 3O)
- **Shields (DEF)**: Force Shield (+2) ➔ Phase Shield (+3: 3C, 1E) ➔ Nano-Hull (+5: 4C, 2E) ➔ Nano-Cloud (+6: 6C, 3E)
- **Engines (ENG)**: *Identical to Wanderer cost/distance.*
- **Command (COM)**: Navicomm ➔ Veteran Captain (+1 roll cost 1I: 3C, 3E, 2I) ➔ Drone AI (Reroll cost 1E: 4C, 3E, 2I) ➔ Shipmind (Double Reroll: 4C, 4E, 3I)

---

## 5. Civilizations of the Parsec
Each civilization has a unique passive upkeep bonus, a resource conversion action, tech discounts, and an Elite Bonus.

| Faction | Passive Upkeep | Resource Conversion | Tech Discounts | Elite Bonus |
| :--- | :--- | :--- | :--- | :--- |
| **Sharnak Imperium** | +1 Ore, +1 Credits | Credits ➔ Ore (1:1) | Weapons (Ore), **Shields (Ore)** | Combat Attack Reroll |
| **The Conversation** | +1 Credits, +1 Influence | Bi-directional Credits ↔ Influence | Engines (Ore), Command (Credits) | Combat Defense Reroll |
| **Wulfram Collective** | +1 Influence | Ore ➔ Influence (1:1) | — | Combat Attack Reroll |
| **Rim Worlds Combine** | +1 Credits, +1 Ore | Ore ➔ Credits (1:1) | — | Exploration Discovery Reroll |
| **The Aiiji** | +2 Credits | Influence ➔ Credits // Credits ➔ Ore | Command (Influence) | General Action Reroll |
| **Altair Divide** | **+1 Influence** | Ore ➔ Influence // Influence ➔ Credits | Weapons (Energy), **Command (Credits)** | Prevent Enemy Rerolls |
| **Gaian Empire** | **+1 Credits, +1 Energy** | Credits ➔ Influence (1:1) | Shields (Energy), **Engines (Ore)** | Combat Defense Reroll |
| **Purist Hegemony** | **+1 Credits, +1 Influence** | **Bi-directional** Influence ↔ Ore | Command (Energy), **Engines (Credits)** | Innate +1 Defense Strength |

*Resource Legend: C=Credits, I=Influence, E=Energy, O=Ore. Changes from v1.0 are in **bold**.*

### Civilization Special Rules

**Sharnak Imperium — Military Doctrine:**  
When the Sharnak Imperium attacks a **Xenophobic Empire** (Planetary Atlas, Roll 4), they apply their *Combat Attack Reroll* bonus in that encounter (reroll if the die shows 1–3). Additionally, the Sharnak military machine grants a **+2 bonus to their Attack Strength** specifically against Xenophobic Empires, representing their unmatched doctrine for sustained assault warfare.

**Purist Hegemony — Fortified Homeworld:**  
The Purist Hegemony's Homeworld is a heavily fortified capital. It grants **+2 Passive Voting Power** in the Galactic Council instead of the standard +1 (or +4 if the player holds the Head of Diplomacy mandate). This reflects their political weight derived from their impenetrable core world. Their bidirectional Influence ↔ Ore conversion allows them to shift between fortress-building and political campaigning each round.

**Gaian Empire — Ecological Specialization:**  
Gaian culture has a deep bond with fertile worlds. During **Phase 1 (Upkeep)**, each **Farming World** the Gaian Empire controls yields an additional **+1 Credit** on top of its standard output. This encourages specialization in Farming Worlds (explored via Planetary Atlas Roll 2) and gives the Gaian economy a distinctive ecological identity.

**Altair Divide — Flagship Intelligence Network:**  
The Altair Divide operates a vast intelligence fleet. During **Phase 6 (Scoring)**, their Flagship sector counts as **1 controlled planet** (type: Mining) for the purpose of scoring **Exploration (EXP) type objectives only** (e.g. *Expand Borders*, *Galactic Dominance*, *Cultural Hub*). This bonus does not apply to Military, Tech, Diplomatic, or Economic objectives. The Flagship must be active and deployed on the board.

**Altair Divide — Prevent Rerolls:**  
Once per combat, if an opponent would trigger their civilization's reroll bonus (e.g. *Attack Reroll*, *Defense Reroll*, *General Reroll*), the Altair Divide player may **cancel that reroll**. The original die result stands. This cancellation is declared aloud before the new roll is made.

---

## **[Flag]** 6. Flagship Appendix**
- **Damage:** Flagships take 2 hits to destroy. The first hit grants a "Damage Token."
- **Extensions:** Unique modules built during Phase 2.
- **Death:** If destroyed, all Extensions are lost. You must rebuild from slot 1 if you designate a new hull.

---
## Appendix A: Advanced Tactics Expansion

By expanding upon the base rules and our previous modules, this expansion fundamentally completes the *Parsec X* experience. It introduces a physical deck of unpredictable Tactic Cards that add extreme bluffing and sudden plot twists to the table.

This expansion integrates cleanly with the *Galactic Council*, *Flagships*, and *Galactic Objectives* rulesets.

---

### 1. Combat Refinements (Taking Hits & Retreating)

Combat in Parsec X is often brutally swift. These advanced rules inject tactical agency when facing impossible odds.

**Tactical Retreats:** 
*   Immediately before combat dice are rolled in the Encounter Phase, either the Attacker or Defender may declare a structural Retreat. 
*   To retreat, the player must immediately discard **1 Resource** from their tracker (representing logistical chaos). 
*   They then immediately move their surviving fleet back to an adjacent, safe sector (a sector containing no enemy ships). No combat die is rolled. If no safe sector is adjacent, you cannot retreat.

**Flagship Durability:** 
*   A Flagship boasts immense structural integrity. It now takes **2 full Hits** (Combat roll losses) to destroy a Flagship.
*   When a Flagship loses a combat roll for the first time, do not destroy it. Instead, place a **Damage Token** on it.
*   If a Flagship with a Damage Token loses a combat roll, it is destroyed completely, clearing its Extension Board.

---

### 2. The Tactic Deck

Tactic cards represent sudden maneuvers, espionage, and brilliant strategic traps. 
*   **Drawing Cards:** During **Phase 1: Upkeep**, after gathering resources from your planets, you may immediately draw **1 Tactic Card** from the deck.
*   **Hand Limit:** You may never hold more than **4 Tactic Cards** in your hand at any given time. If you draw a 5th, you must discard one.
*   **Playing Cards:** Every Tactic Card has a specific timing window described on the card (e.g. *Action*, *Combat*, *Agenda Phase*). Playing a card costs no resources unless the card explicitly states otherwise. Resolve its effect and discard it.

---

### APPENDIX: THE TACTIC DECK CATALOG (25 Unique Cards)

Assemble a deck using the following 25 Tactic Cards.

### Combat Tricks
1.  **Emergency Thrusters:** *(Combat)* Play immediately after losing a combat roll. Ignore the loss and do not remove a ship. You must immediately retreat the fleet into an adjacent safe sector.
2.  **Shield Overload:** *(Combat)* Play before dice are rolled. Gain a temporary +3 Defense Strength for this specific die roll.
3.  **Experimental Ordnance:** *(Combat)* Play before dice are rolled. If you win this specific roll, destroy 2 enemy ships instead of 1.
4.  **Bypass Codes:** *(Combat)* Play against a heavily fortified planet. Ignore the planet's native Defense Strength bonuses (e.g., Planetary Capitals or Terraformed planets) for this entire encounter.
5.  **Flanking Maneuver:** *(Combat)* Play if you are the Attacker. You may re-roll your combat die once.
6.  **Sabotage:** *(Combat)* Play before dice are rolled. The opposing player cannot apply their current *Weapon* or *Shield* Tech Tree bonus to this encounter.
7.  **Point Defense Grid:** *(Combat)* Play when an opponent uses a Flagship's Orbital Bombardment. Completely negate the bombardment.
8.  **Kamikaze Protocol:** *(Combat)* Play immediately after losing a combat roll. Both your ship and the winning enemy ship are destroyed simultaneously.

### Economic & Strategic
9.  **Industrial Espionage:** *(Action/Upkeep)* Play during your Upkeep phase. Steal 2 Resources of your choice directly from another player's tracker.
10. **Trade Network Hack:** *(Action)* Swap the position of two of your ships anywhere on the board instantly.
11. **Smuggler’s Route:** *(Action/Movement)* During your movement phase, one of your ships may move across diagonals for this turn.
12. **Deep Cover Agent:** *(Action/Scoring)* Play during the Scoring phase. You may swap one of your hidden Secret Objectives with a newly drawn one from the deck.
13. **Rapid Deployment:** *(Action/Upgrade)* Play during your Upgrade phase. You may build 1 ship completely for free.
14. **Ghost Fleet:** *(Action/Movement)* During movement, your fleet may pass directly through sectors occupied by enemy ships without stopping or triggering combat.
15. **Resource Transmutation:** *(Action)* Completely empty your Ore tracking bar, and gain an identical amount of Credits.

### Uncharted Space
16. **Astrogation Master:** *(Action/Encounter)* Play when uncovering an Unknown Planet. You may physically dictate what the planet is without rolling a die.
17. **Distress Beacon:** *(Action/Movement)* Pull any one of your ships from the board directly into the sector containing your Flagship, regardless of distance.
18. **Anomalous Field:** *(Action)* Play on any Sector map card. No ships may enter or leave that specific map card for the rest of this entire round.
19. **Diplomatic Backchannels:** *(Action/Encounter)* Automatically succeed in forging a Diplomatic Alliance with an Elder Civilization without rolling or paying the Influence cost.
20. **Aggressive Terraforming:** *(Action/Encounter)* When encountering a Terraforming Candidate (Planetary Atlas, Roll 6), terraform it for half of the required resource cost (rounded down).

### Political Sabotage (requires Galactic Council Expansion)
21. **Veto Power:** *(Agenda Phase)* Play instantly when a Resolution (For/Against) is passed. Cancel the outcome. The Agenda fails.
22. **Bribery:** *(Agenda Phase)* Play before votes are cast. You may subtract up to 3 votes from any opponent's final voting total this round.
23. **Political Assassination:** *(Agenda Phase)* Play after an Election has been designated. Choose one specific player; they cannot be voted for on this Agenda. 
24. **Filibuster Delay:** *(Agenda Phase)* Push the currently revealed Agenda card to the bottom of the deck and immediately draw a new one to vote on instead.
25. **Blackmail:** *(Agenda Phase)* Play before a player casts their vote. You declare exactly how that player must cast their base planetary voting power.


## Appendix B: Flagship Expansion

Towering above standard cruisers, the Flagships are the crowning achievement of a civilization's military and logistical engineering. This expansion lets a player designate a capital ship and bolt devastating modular technology onto its hull.

### 1. Flagship Designation

Every player has the right to field exactly one Flagship at any given time.
*   **Designating the Hull:** During **Phase 2 (Upgrade)**, if you do not currently have an active Flagship on the board, you may freely designate any one of your existing, standard ships as your Flagship. Place a coin, specialized token, or a differently colored acrylic cube underneath it.
*   **Combat Prowess:** Because it commands your forces from the front lines, a Flagship counts as **2 ships** for the purpose of calculating Combat Strength bonuses (providing a native +2 instead of +1 to a sector's total numerical strength).

### 2. The Extension Board

When you designate a Flagship, you unlock the use of a personal **Flagship Extension Board**. 
This board contains exactly **4 Slots** into which you can plug powerful Extensions.

### Building Extensions
During **Phase 2 (Upgrade)**, you may pay resources to build a new Extension from the global catalog and slot it into your Extension Board.
*   **Uniqueness Requirement:** You may never build two of the exact same Extension on your Flagship. Every module must be unique.
*   **Escalating Cost:** The price of installing an Extension increases as the ship becomes heavier and more technologically saturated. The cost must be paid using any combination of Ore, Energy, or Credits:
    *   **1st Extension:** Costs 2 Resources
    *   **2nd Extension:** Costs 4 Resources
    *   **3rd Extension:** Costs 6 Resources
    *   **4th Extension:** Costs 8 Resources

*Note: You may only ever have a maximum of 4 Extensions active simultaneously.*

### 3. Flagship Destruction

If you lose a combat that involved your Flagship, your Flagship is destroyed along with any standard ships mandated by combat casualty rules. 

**Catastrophic Loss:** If your Flagship is destroyed, your entire Extension Board is flushed. You must discard and clear all built Extensions.
During a future Phase 2, you may designate a new Flagship, but you must start over from scratch with zero Extensions, paying starting costs for the first slots.

### 4. Emergency Repairs

If a Flagship has sustained a **Damage Token** (via the Advanced Tactics module), you may repair the hull by sacrificing its upgrades.

**Jettisoning Components:** During **Phase 1 (Upkeep)**, you may permanently discard one active Extension from your Flagship's Extension Board to immediately remove its Damage Token. The slot becomes empty, and the component is destroyed.

---

### APPENDIX: THE EXTENSION CATALOG

When purchasing an Extension, select one of the following 15 unique modules. It remains active as long as your Flagship is alive.

### Combat Operations
1.  **Orbital Bombardment Array:** *(Action: Encounter Phase)* Before standard combat rolls begin against an enemy planet, the Flagship may roll 1 die. On a 5 or 6, one defending enemy ship on that planet is unconditionally destroyed.
2.  **Command Carrier Bay:** *(Passive)* Any other friendly standard ships in the same sector as the Flagship cannot be chosen as casualties during tiebreaker combats or standard losses, protecting your smaller vessels.
3.  **Ablative Hull Plating:** *(Passive)* The physical bulk of the ship protects it; the Flagship confers a permanent, innate +1 Defense Strength to any combat it participates in.
4.  **Precision Targeting AI:** *(Passive)* The Flagship links targeting arrays across the fleet, conferring a permanent, innate +1 Attack Strength to any combat it participates in.
5.  **EMP Pulse Caster:** *(Action: Encounter Phase)* Once per round, before combat dice are rolled, spend 1 Energy. You may completely negate the opponent's "Weapon" or "Shield" technology tree bonus for this combat.

### Navigation & Exploration
6.  **Quantum Slipstream Drive:** *(Action: Movement Phase)* Spend 3 Energy to instantly jump the Flagship (and any ships physically sliding underneath it) to any Spacewarp icon on the board, regardless of adjacency.
7.  **Deep Space Sensors:** *(Action: Encounter Phase)* When the Flagship is in a sector discovering an Unknown Planet, roll 2 dice instead of 1. You may choose which of the two results you want to use.
8.  **Tractor Beam:** *(Action: Movement Phase)* When moving out of a sector, the Flagship may hook onto exactly one opposing enemy ship located in its starting sector and forcefully drag that ship along into its destination sector.

### Logistics & Economy
9.  **Diplomatic Envoy Protocol:** *(Passive)* The Influence cost to successfully forge a Diplomatic Alliance with an Elder Civilization is fundamentally reduced by 2 if the Flagship is stationed in that sector.
10. **Scavenger Harvesters:** *(Passive)* Every time the Flagship wins a combat and destroys an enemy ship, your civilization immediately salvages the wreckage, gaining either 1 Ore or 1 Credit.
11. **Advanced Logistics Hub:** *(Passive)* During the Upgrade Phase, your Flagship operates as a mobile command base. You may spawn newly purchased ships directly onto the Flagship's sector exactly as if it were a Shipyard Moon.
12. **Terraforming Charges:** *(Passive)* The sheer engineering power on board allows the Flagship to reshape worlds. The resource cost to terraform a Terraforming Candidate (Planetary Atlas, Roll 6) is reduced by 2 if the Flagship is stationed in that sector.

### Intergalactic Politics & Glory (Requires Expansions)
*These extensions bridge your Flagship directly into the mechanics of the Objective and Council modules.*

13. **Galactic Broadcast Node:** *(Passive - Requires Galactic Council)* During Phase 5 (Galactic Council), your Flagship grants you an innate **+3 Voting Power**, acting as a massive, mobile seat of political influence.
14. **Stealth Recon Uplink:** *(Passive - Requires Galactic Objectives)* During Objective Deck Setup or whenever you draw a Secret Objective, you may hold 1 additional Secret Objective card in your hand beyond the standard limit, giving you more hidden paths to Victory Points.
15. **Mobile Command Center:** *(Passive - Requires Galactic Objectives)* During Phase 6 (Scoring), the sector containing your Flagship may count as 1 controlled planet (of any basic planetary type of your choice) solely for the purpose of meeting requirements for Stage 1 or Stage 2 Public Objectives.


## Appendix C: Galactic Council Expansion

Welcome to the Senate. This rule module injects complex political maneuvers into the micro-footprint of **Parsec X**. Leveraging the new Phase structure introduced in the *Galactic Objectives Expansion*, this module shifts the Scoring phase to allow players to enact game-altering laws and direct sanctions. 

> [!NOTE]
> This module requires the *Galactic Objectives Expansion* to be in play.

### 1. Updated Round Structure

The phase sequence for Parsec X is updated as follows:
**Phase 1:** Upkeep ➔ **Phase 2:** Upgrade ➔ **Phase 3:** Movement ➔ **Phase 4:** Encounter ➔ **Phase 5: GALACTIC COUNCIL** ➔ **Phase 6: SCORING**

### 2. Setting the Trigger Condition
Before the game begins, the table must collectively choose **one** of the following four variants which dictates when the Galactic Council is unlocked and convenes for the first time:

1.  **The Elder Variant (Recommended):** The Council Phase does not occur until at least one player successfully controls an *Elder Civilization*. Once an Elder Civilization is claimed, the Council Phase happens every round thereafter. *(Failsafe: If no Elder Civilizations are rolled, the Council unlocks the round that the very last Unknown Planet on the board is revealed).*
2.  **The Escalation Variant:** The Council remains dormant until any player reaches **3 Victory Points**. Once reached, the late-game becomes heavily political.
3.  **The Planetary Milestone Variant:** The Council unlocks the round immediately after any player successfully leaves their Homeworld and takes control of a 2nd planet.
4.  **The Immediate Variant:** The Council happens every single round starting from Round 1.

### 3. The Galactic Council Phase mechanics

Once the Galactic Council has been unlocked, the following steps occur during Phase 5:

1.  **Convene:** The Start Player draws the top card of the Agenda Deck and reads it aloud to the table.
2.  **Voting Sequence:** Starting with the player to the left of the Start Player and moving clockwise, each player must declare their votes. You may choose to pass/abstain. Once a vote has been stated, it is locked. The Start Player votes last and acts as the tiebreaker.
3.  **Voting Power (The Currency):** Players cast votes using two cumulative methods:
    *   **Spending Influence:** You may spend Influence Resources directly from your resource tracker. (1 Spent Influence = 1 Vote).
    *   **Passive Planet Voting Power:** Planets you control inherently provide voting power without needing to be "spent" or exhausted:
        *   *Homeworlds:* +1 Vote
        *   *Elder Civilizations:* +3 Votes
        *   *Xenophobic Empires:* +2 Votes
        *   *Standard Planets (Mining/Farming/Jovian/Terraformed):* +1 Vote each
        *   *Colony Moons (White Cube):* Add +1 Vote to their attached planet.
4.  **Resolution:** The outcome with the highest total votes passes, and its text immediately comes into effect. **Tie-Breaking:** In the event of a tied vote, the Start Player's chosen outcome prevails. If the Start Player abstained, the agenda fails with no effect.

> **Purist Hegemony Special Rule:** The Purist Homeworld grants **+2 Passive Voting Power** (instead of the standard +1). If the Purist player holds the *Head of Diplomacy* mandate, their Homeworld grants **+4 votes** instead of +3. See Section 5 for details.

---

### 4. Council-Linked Objectives Addendum

Add these 4 thematic objective cards to your Object Deck (from the previous expansion).
1.  **Political Titan (Stage 1):** Cast 5 or more votes during a single Agenda resolution this round.
2.  **Filibuster (Stage 1):** Spend 3 Influence Resources during the Galactic Council Phase.
3.  **Puppet Master (Stage 2):** Vote "For" on an Election Agenda that successfully elects a player other than yourself.
4.  **Voice of the Senate (Secret):** Win a vote where you were the only player to vote for the winning outcome.

---

### APPENDIX: THE AGENDA DECK (40 Unique Cards)

Assemble a deck using the following 40 Agendas. 

### A. RESOLUTIONS (Vote: FOR or AGAINST)
These mandate immediate global effects or alter game rules permanently.

1.  **Wormhole Tolls:** **For:** Moving through a Spacewarp now costs 1 Credit in addition to Energy. **Against:** All players must discard 1 Energy resource.
2.  **Demilitarized Zones:** **For:** A player cannot attack a planet if their track has 0 Influence. **Against:** No effect.
3.  **Arms Trade:** **For:** All players gain 2 Ore. **Against:** All players may build 1 ship at half cost (rounded up) during the next Upgrade Phase.
4.  **Technological Subsidies:** **For:** The next Technology upgrade a player purchases costs 1 fewer Resource. **Against:** All players with 3+ Techs lose 1 Energy.
5.  **Imperial Taxation:** **For:** All players must lose 2 Credits or destroy 1 of their own ships. **Against:** The Start Player loses 3 Credits.
6.  **Economic Stimulus:** **For:** Every player gains 2 Credits and 1 Energy. **Against:** No effect.
7.  **Deforestation Acts:** **For:** Farming Worlds provide +1 Ore during Upkeep but -1 Credit. **Against:** All players controlling Farming Worlds gain 1 Influence.
8.  **Mining Regulations:** **For:** Mining Worlds provide -1 Ore during Upkeep. **Against:** The player(s) with the most Mining Worlds loses 2 Ore.
9.  **Xenobiology Grants:** **For:** Players controlling Xenophobic Empires or Elder Civilizations gain 2 Energy immediately. **Against:** Xenophobic Empires gain +1 Defense globally.
10. **Strict Borders:** **For:** Ships confer +2 Defense to controlled planets instead of +1. **Against:** Remove all ships residing on Spacewarp nodes (they are destroyed).
11. **Fleet Restrictions:** **For:** The maximum fleet size is reduced to 3 ships. If you have 4, destroy 1 immediately. **Against:** No effect.
12. **Shield Harmonization:** **For:** All players treat their Shield (DEF) technology as being 1 tier higher during Combat. **Against:** No effect.
13. **Accelerated Deployment:** **For:** Players may spawn ships on *any* planet they control, not just Homeworlds or Shipyards. **Against:** Build costs for the next round are increased by 1 Ore.
14. **Peace Accords:** **For:** No combat may be initiated during the next Round's Encounter phase. **Against:** The player who cast the most votes loses 1 ship.
15. **War Effort:** **For:** Players may discard 2 Credits to add +1 to an attack roll. **Against:** Players must discard 1 Ore or 1 Energy.
16. **Resource Scarcity:** **For:** During the next Upkeep phase, players only gather resources from their Homeworld. **Against:** No effect.
17. **Colonial Tax:** **For:** Colony Moons provide 1 Credit instead of 1 Influence. **Against:** Destroy all Colony Moons.
18. **Void Research:** **For:** Any player uncovering an Unknown planet gains 1 Energy immediately. **Against:** Unknown planets get +1 Defense.
19. **Expansion Initiative:** **For:** Settlement costs for empty planets roll 1, 2, or 3 are reduced by 1 Resource. **Against:** Settlement costs are increased by 1 Resource.
20. **Diplomatic Immunity:** **For:** Players cannot attack Homeworlds or Elder Civilizations. **Against:** No effect.

### B. ELECTIONS (Vote: ELECT PLAYER or ELECT PLANET TYPE)
These target specific players or specific types of planets (e.g. Jovian Worlds).

21. **Galactic Treasurer (Elect Player):** Elected player gains 3 Credits during every Upkeep Step.
22. **Supreme Commander (Elect Player):** Elected player's ships roll with an innate +1 Attack standard bonus.
23. **Minister of Science (Elect Player):** Elected player may immediately unlock 1 Tech of their choice for free.
24. **Head of Diplomacy (Elect Player):** Elected player gains 2 Influence. Whenever they vote, their Homeworld counts as 3 votes.
25. **Outcast (Elect Player):** Elected player cannot vote in the next 2 Galactic Council phases.
26. **Imperial Sanctions (Elect Player):** Elected player loses half their total stored resources (rounded down, their choice of which).
27. **Architect of Ruin (Elect Player):** Elected player may immediately destroy 1 opponent ship in an adjacent sector to their fleet.
28. **Vanguard (Elect Player):** Elected player immediately gains 1 Victory Point.
29. **Public Enemy (Elect Player):** Any player who destroys a ship belonging to the Elected player gains 1 Influence.
30. **Propaganda Target (Elect Player):** Elected player loses all remaining Influence cubes on their tracker.
31. **Mining Subsidies (Elect Planet Type):** Each planet of this type immediately yields 2 Ore to its controller.
32. **Agricultural Grants (Elect Planet Type):** Each planet of this type immediately yields 2 Credits to its controller.
33. **Core Exploitation (Elect Planet Type):** Planets of this type provide +1 Resource of their native yield during Upkeep, but cost 1 Energy extra to move onto.
34. **Cultural Preservation (Elect Planet Type):** Planets of this type cannot be attacked.
35. **Planetary Embargo (Elect Planet Type):** Planets of this type generate no resources during the Upkeep phase.
36. **Subspace Anomaly (Elect Planet Type):** Ships moving away from planets of this type cost 1 additional Energy.
37. **Fortified Worlds (Elect Planet Type):** Planets of this type roll with a baseline +6 Defense Strength.
38. **Bountiful Harvest (Elect Planet Type):** The controller(s) of these planets immediately gain 1 VP.
39. **Unstable Core (Elect Planet Type):** If combat occurs on this planet type, both Attacker and Defender lose 1 ship before rolls are made.
40. **Planetary Capital (Elect Planet Type):** From now on, this planet type provides 3 Voting Power instead of its usual passive amount.

### C. EXPANSION INTEGRATION AGENDAS
*Mix these into the Agenda deck if you are playing with both the Flagship and Galactic Objective expansion modules.*

41. **[Flag]** **(Resolution) Flagship Registration:** **For:** Building Flagship Extensions costs +1 Resource globally. **Against:** Building Flagship Extensions costs -1 Resource globally.
42. **[GalObj]** **(Resolution) Classified Objectives Disclosure:** **For:** All players must visibly reveal 1 Secret Objective they are holding. **Against:** All players must randomly discard 1 Secret Objective and draw a new one to replace it.
43. **[Flag]** **(Election) Admiral of the Fleet (Elect Player):** The elected player's Flagship counts as 3 ships in combat instead of 2 for the rest of the game.
44. **[GalObj]** **(Election) Public Disgrace (Elect Player):** The elected player cannot score any Public Objectives during the next Scoring phase.
45. **[Flag]** **(Election) Public Hero (Elect Player):** The elected player immediately gains 1 VP as long as they currently have an active Flagship securely stationed on the board.


## Appendix D: Galactic Objectives Expansion

This unofficial expansion introduces an alternative victory point system for **Parsec X** inspired by *Twilight Imperium*, replacing the original "first to 4 planets" win condition with dynamic, diverse economic, technological, and militaristic objectives. Instead of simply racing for planets, players will compete over public directives and hidden agendas set by the Galactic Council.

### 1. New Mechanics: Victory Points (VP)

### Game Length
The game is played over a fixed duration of **10 Rounds**. After the 10th round is completed, the game ends.

### Victory Condition
The player with the most Victory Points at the end of Round 10 is the winner. If there is a tie for the most VP, the result is a **shared victory**.

### 2. Objective Deck Setup

Before the game begins, split the objectives into three decks: **Stage 1 Public**, **Stage 2 Public**, and **Secret Objectives**. Shuffle each deck separately.

1.  Place the **Stage 1 Public** and **Stage 2 Public** objective decks face down near the board.
2.  The public objective track starts empty.
3.  Deal each player **two Secret Objectives**. Each player keeps one and discards the other face down to the box.

### 3. New Phase: SCORING (Phase 5)

Rounds in Parsec X now feature a fifth phase:
**Phase 1:** Upkeep ➔ **Phase 2:** Upgrade ➔ **Phase 3:** Movement ➔ **Phase 4:** Encounter ➔ **Phase 5: SCORING**

During the Scoring Phase, beginning with the Start Player and proceeding clockwise:
1.  **Reveal New Objective:** At the start of the phase, add a new Public Objective to the track from the decks:
    - **Turns 1–5:** Reveal a card from the **Stage 1** deck.
    - **Turns 6–10:** Reveal a card from the **Stage 2** deck.
2.  **Score Objectives:** A player scores **ALL** Public Objectives and Secret Objectives they qualify for. To score a Public Objective, the player places a cube on it. They do not claim the card, allowing other players to score it on future turns.
    *(The previously enforced limit of one public objective per round is removed).*

### Action Phase Secret Objectives
Some Secret Objectives have the **(Action Phase)** tag. These are the *only* objectives that are not scored during Phase 5. A player may instantly reveal and score an Action Phase objective immediately when its condition is met during Phase 2 (Upgrade), Phase 3 (Movement), or Phase 4 (Encounter). The objective is placed face up in the player's play area and its VP applies immediately.

*Note: You may only score one Secret Objective per round, regardless of whether it is an Action Phase objective or a Scoring Phase objective.*

---

### APPENDIX: THE OBJECTIVE CARDS

There are exactly 45 unique objectives in this expansion.

### Stage 1 Public Objectives (Worth 1 VP each)

1.  **Expand Borders:** Control 1 Planet outside of your Homeworld.
2.  **Diversify Economy:** Spend a total of 5 Resources (Credits, Influence, Energy, and/or Ore) during the Scoring Phase.
3.  **Technological Advancements:** Have at least 2 technologies in two different Tech Tree columns.
4.  **Build a Mighty Fleet:** Have your maximum of 4 ships on the game board.
5.  **Secure the Sectors:** Have ships in at least 3 different sectors on the board.
6.  **Mining Boom:** Control at least 1 Mining World.
7.  **Agrarian Push:** Control at least 1 Farming World.
8.  **Gas Harvesting:** Control at least 1 Jovian World.
9.  **Political Influence:** Spend 3 Influence Resources during the Scoring Phase.
10. **Energy Reserves:** Spend 3 Energy Resources during the Scoring Phase.
11. **Industrial Might:** Spend 3 Ore Resources during the Scoring Phase.
12. **Wealth Accumulation:** Spend 3 Credit Resources during the Scoring Phase.
13. **Fleet Consolidation:** Have exactly 2 Ships on a single Sector Map Card.
14. **Wormhole Navigation:** Have a Ship resting on a Spacewarp icon.
15. **Colonial Outreach:** Control a planet that has a Colony Moon (White Cube).

### Stage 2 Public Objectives (Worth 2 VP each)

1.  **Galactic Dominance:** Control 2 Planets outside of your Homeworld.
2.  **Economic Powerhouse:** Spend a total of 10 Resources of any combination during the Scoring Phase.
3.  **Mastery of Science:** Unlock the final tier technology (bottom row) in two different Tech Tree columns.
4.  **Centralize Command:** Have a ship on a Shipyard Moon *and* a Colony Moon simultaneously.
5.  **Resource Monopoly:** Control 1 Farming World and 1 Mining World.
6.  **Atmospheric Dominance:** Control 1 Jovian World and 1 Farming World.
7.  **Deep Core Harvesting:** Control 1 Mining World and 1 Jovian World.
8.  **Hostile Takeover:** Control 1 Xenophobic Empire.
9.  **Ancient Secrets:** Control 1 Elder Civilization.
10. **Terraformer:** Control 1 planet that was settled via Terraforming (Planetary Atlas, Roll 6).
11. **Shield Technology Mastery:** Unlock Phase Shield or Nano-Hull (DEF Level 3 or 4).
12. **Weapon Technology Mastery:** Unlock Gauss Missiles or Fusion Cannon (ATT Level 3 or 4).
13. **Engine Technology Mastery:** Unlock Stellar Drive or Navicomm (ENG Level 3 or 4).
14. **Command Technology Mastery:** Unlock Shipmind (COM Level 3).
15. **Invasion Force:** Have 3 Ships residing in 3 different Enemy Sectors.

### Secret Objectives (Worth 1 VP each)

1.  **(Action Phase) Surprise Attack:** Win a combat against a player whose ship is in a sector with an Unknown Planet or Spacewarp.
2.  **Cultural Hub:** Control 2 Planets of the exact same type (e.g., 2 Mining Worlds).
3.  **Xenology Expert:** Control a planet that was once a Xenophobic Empire or an Elder Civilization.
4.  **Aggressive Expansion:** Control a planet in another player's starting Sector Map Card.
5.  **Miner's Guild:** Control 2 Mining Worlds.
6.  **Agrarian Society:** Control 2 Farming Worlds.
7.  **Gas Giants:** Control 2 Jovian Worlds.
8.  **The Pacifist:** Have 0 Combat encounters this entire round.
9.  **Blockade:** Have a ship on a sector occupied by another player's controlled planet (without conquering it).
10. **Hoarder:** Have 8 or more of a single resource type on your tracker at the end of Phase 5.
11. **Tech Supremacy:** Have unlocked all technologies in a single column.
12. **Deep Space Exploration:** Successfully uncover 2 Unknown Planets this round.
13. **Interloper:** Have ships on two different opponents' Sector Map Cards.
14. **The Diplomat:** Successfully forge a Diplomatic Alliance with an Elder Civilization this round.
15. **(Action Phase) Exterminator:** Destroy an opponent's ship during combat.

### Expansion Integration Objectives
*Mix these into the Objective deck if you are playing with the Flagship and Galactic Council expansion modules.*

**Stage 1 Public Objectives (1 VP)**

16. **[GalCon]** **Political Titan:** Cast 5 or more votes during a single Agenda resolution this round.
17. **[GalCon]** **Filibuster:** Spend exactly 3 Influence Resources during the Galactic Council Phase.
18. **[Flag]** **Flagship Commissioning:** Have an active Flagship on the board with at least 1 Extension built on its board.

**Stage 2 Public Objectives (2 VP)**

16. **[GalCon]** **Puppet Master:** Vote "For" on an Election Agenda that successfully elects a player other than yourself.
17. **[Flag]** **Juggernaut Pattern:** Have an active Flagship on the board with 4 Extensions built on its extension board.
18. **[GalCon]** **[Flag]** **Political Blockade:** Successfully vote for the winning outcome of an Agenda card, AND have an active Flagship stationed on an opponent's Sector Map card simultaneously.

**Secret Objectives (1 VP)**

16. **[GalCon]** **Voice of the Senate:** Win a Galactic Council vote where you were the only player to vote for the winning outcome.
17. **[Flag]** **(Action Phase) Capital Ship Kill:** Overwhelmingly destroy another player's Flagship during combat.
