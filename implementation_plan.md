# Validation Report: Simulation vs Master Rulebook

I have thoroughly reviewed the simulation engine (`parsec_sim.py`) against the finalized Master Edition Rulebook (`ParsecX_Master_Edition_Rules.md`). Overall, the simulation implements complex systems like the Galactic Council and Tech Trees well. However, I have identified **5 key rule violations** that disrupt the simulation's mechanical accuracy.

## User Review Required

Please review the following discrepancies and the proposed fixes. If approved, I will implement these patches into `parsec_sim.py`.

### 1. Victory Point Overwrite Bug (Critical)
**Rulebook Constraint:** *Appendix D: "The game is no longer won by simply controlling 4 planets. Instead, players compete to score Objective Cards to earn Victory Points (VP)."*
**Simulation Issue:** In `phase_scoring`, lines 983 and 1028 execute `player.vp = len(player.planets)`. This completely wipes out any VP scored in previous rounds from objective cards and reverts their score to their planet count, invalidating the entire Galactic Objectives expansion. 
**Proposed Fix:** Remove `player.vp = len(player.planets)` entirely. VP calculation will rely purely on aggregating the VP values of claimed objectives from players.

### 2. Flagship Combat Support Value (Major)
**Rulebook Constraint:** *Appendix B: Flagships count as 2 ships for the purpose of calculating Combat Strength bonuses.*
**Simulation Issue:** In `get_strength()`, the simulation picks one ship to lead the combat and counts the rest as support: `other_support = len(other_ships)`. This means if a Flagship is acting as a support vessel to another cruiser, it only provides +1 support strength rather than +2.
**Proposed Fix:** Loop through `other_ships` to calculate support strength, granting +2 if the supporting ship `is_flagship`.

### 3. Missing Tactical Retreats (Major)
**Rulebook Constraint:** *Appendix A: "Before rolls, a defender may discard 2 Energy to move 1 space away."*
**Simulation Issue:** The Encounter phase and `resolve_combat` function have no logic allowing defending players to initiate an energy-based retreat.
**Proposed Fix:** Inject a check at the start of `resolve_combat`. Since this is an AI simulation, grant defenders a heuristic choice to retreat (e.g. discard 2 Energy to abort combat if their calculated strength is significantly lower than the attacker's strength).

### 4. Phantom Aiiji Passive (Minor)
**Rulebook Constraint:** *Section 5: The Aiiji possess "Political Synthesis: Spend Influence for VPs."*
**Simulation Issue:** The simulation contains hidden code granting The Aiiji an immediate +1 VP out of thin air if they cast 12 cumulative votes over the course of the game ("Voice of the Galaxy"). This legacy passive does not exist in the Master Rulebook.
**Proposed Fix:** Delete the Voice of the Galaxy hardcoded passive from the scoring hook.

### 5. Ship Building Base Costs (Minor)
**Rulebook Constraint:** *Phase 2: "Pay the indicated Ore/Credit cost to build new ships."*
**Simulation Issue:** The simulation hardcodes standard ship building to cost exactly 1 of every single resource (`ORE: 1, ENERGY: 1, CREDITS: 1, INFLUENCE: 1`), which is not an intended Parsec X ship cost.
**Proposed Fix:** Update the standard AI ship construction cost to 2 Ore, representing a standard basic hull. Or, map it based on the Wanderer vs Raider ship card defaults.

---

## Proposed Changes

### `parsec_sim.py`
#### [MODIFY] parsec_sim.py
- **Refactor `phase_scoring`:** Remove the `player.vp = len(player.planets)` lines so that points are purely cumulative based on Objective scoring.
- **Refactor `resolve_combat`:** Add Tactical Retreat heuristic for defending AI if `str2 < str1` and `ENERGY >= 2`.
- **Refactor `get_strength`:** Assign +2 support strength to Flagships in the `other_ships` array.
- **Cleanup `phase_upgrade`:** Correct the ship building resource cost. 
- **Cleanup `phase_scoring`:** Removed undocumented Aiiji 12-vote passive VP logic.

## Verification Plan

I will run `python parsec_sim.py` post-fix and verify the standard outputs to ensure game logic is sound. We will look for:
1. Players winning *exclusively* via achieving Objective VP.
2. The Combat log properly demonstrating Flagships granting +2 support strength. 
3. The Combat log occasionally logging a Tactical Retreat triggered by a defender. 
