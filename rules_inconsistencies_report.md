# Parsec X: Rules & Simulation Inconsistencies Report

After cross-referencing the 150-game simulation results against both the core game rules (`parsecX_rules.txt`) and all the expansion module documents, I have identified several major rules violations and physical game limitations that the simulation data ignored. 

The simulation engine seems to have scaled faction economy infinitely, breaking the heavy constraints imposed by the game's actual cardboard components and rulebooks.

---

## 1. Flagship Extension Capacity Limit (CRITICAL)

**The Rule Violation:**
The simulation repeatedly highlights the dominance of **"5-Extension"** Flagships in the late game. Almost every winning entry for Long/Epic games lists Flagship details such as `Built (5 Extensions)`. 

**The Actual Rule:**
In `ParsecX_Flagships_Expansion.md` (Lines 14 & 25), the rules explicitly state a hard cap of 4 slots:
> *"This board contains exactly 4 Slots into which you can plug powerful Extensions."*
> *"Note: You may only ever have a maximum of 4 Extensions active simultaneously."*

Additionally, the Stage 2 Public Objective Card "Juggernaut Pattern" maxes out at **4 Extensions**, further cementing that 5 is an illegal game state.

## 2. Maximum Fleet Limit & Swarm Mechanics (CRITICAL)

**The Rule Violation:**
The simulation dataset describes factions like the Wulfram Collective winning through "mass production", "sheer ship numbers", and "highest ship count ever tracked". It tracks massive 10+ round attrition wars where games end with fleets painting the map.

**The Actual Rule:**
In the core `parsecX_rules.txt` (Line 17 and Line 266), the game imposes a strict, microscopic component limit on ships:
> *"A player may never have more than four ships at any time."*
> *"...the other four are used as a player’s ships in the game."*

The narrative of "swarming" the board in an Epic game is physically impossible under standard rules. With a hard cap of exactly 4 ships per player, a faction cannot field endless armadas; their production capabilities simply bounce off the ceiling. 

## 3. Galactic Council Voting Economy

**The Rule Violation:**
The simulation data shows certain political factions (like The Conversation) casting absurd volumes of votes, peaking at **185 total votes cast** per game. 

**The Actual Rule:**
Under `ParsecX_Galactic_Council_Expansion.md`, votes are generated via base planet passes (e.g., Homeworlds = 1, standard planets = 1) and by spending Influence resources (1 Influence = 1 Vote). Since the resource tracks have hard caps on the physical tracking cards, and fleets are capped at 4 ships to limit expansion, generating enough natural votes to hit ~180 across a standard 10-12 turn epic game implies an unbounded resource track or misinterpreting votes as purely cumulative rather than heavily limited by the maximum Influence storage capacity.

## 4. Player Elimination

**The Rule Violation:**
The simulation text routinely notes players completely wiping other players off the map to eliminate opponents. 

**The Actual Rule:**
`parsecX_rules.txt` (Line 499) clearly states:
> *"A player may never attack another player’s Homeworld."*

An opposing civilization can never be fully eliminated out of the game mechanically because their Homeworld hex is eternally safe from invasion, making the "Eliminated" status in the simulation tables impossible under standard combat rules.

---

### Conclusion & Next Steps
The early simulation data we generated successfully stress-tested the *theoretical mathematics* of the game's economy, but it critically failed to enforce the **micro-4X physical constraints** (4 ships, 4 extensions, unkillable homeworlds). 

If you want the Epic/Long game variants to function properly, we need to adapt our approach:
1. **Revise the simulation parameters** to enforce a hard 4-ship and 4-extension limit. This strongly limits early aggression but completely deflates late-game "infinite production" builds (meaning Wulfram wouldn't necessarily win in a 10 VP mode just off production).
2. **Rewrite the Core Rules** specifically for the Long/Epic Game modules to lift these caps, adding new components (like Fleet/Squadron tokens and larger boards) so that 5+ ships and 5+ extensions are actually legal on the table.
