# Parsec X: Simulation Results Tracking

This document tracks the results of simulated matches of Parsec X running with **all expansions enabled** (Advanced Tactics, Flagships, Galactic Council, and Galactic Objectives). The goal is to accumulate data on civilization win rates, component usage, and meta-strategies.

## Simulation Setup Parameters
- **Expansions:** All (Core + 4 Expansions)
- **Player Count:** 4
- **Victory Condition:** Standard Game (5 VP), Long gane (7 VP), Epic game (10 VP)
- **Council Trigger:** The Elder Variant
- **Ships maximum count:** 4
- **Extensions maximum count:** 4
- **Votes cast limit** votes are generated via base planet passes (e.g., Homeworlds = 1, standard planets = 1) and by spending Influence resources (1 Influence = 1 Vote), or by galactic Galactic Broadcast Node (3 votes).

## Evaluation Metrics
The following metrics are tracked during each simulation to evaluate the balance and performance of different civilizations:

*   **Run ID:** The unique identifier for the simulated game instance.
*   **Player:** The generic seat number of the player in the simulation.
*   **Civilization:** The specific faction/empire randomly assigned to the player.
*   **Final VP:** The total Victory Points accumulated by the end of the game. Allows evaluating how close losers were to winning.
*   **Result:** Indicates whether the player achieved "Winner" status (reaching 5 VP first) or "Loser".
*   **Planets Controlled:** The total number of planetary bodies held at game end (including Special planets like the Core or Elders). This evaluates map presence and underlying economic strength.
*   **Flagship Details:** Denotes whether a Flagship was built, if it was destroyed in combat, and the peak number of Extensions it carried. Evaluates the viability of heavy capital ship strategies.
*   **Flagship Extensions Details:** Denotes which extensions were built on flagship. Evaluates the viability of heavy capital ship strategies.
*   **Combat Encounters:** The gross number of combat instances the player was involved in (both attacking and defending). Assesses aggressive versus isolationist playstyles.
*   **Votes Cast:** The sum of all Voting Power actively committed across all rounds of the Galactic Council phase. This measures the political influence of the civilization over laws and elections.
*  **Agendas/ELections** : agendas and elections voted during council phase. Also indicate which option/player were voted.
*   **Tactics Played:** The total number of Tactic Cards actively used from the player's hand, highlighting reliance on combat trickery and sudden maneuvers.
*   **Key Strategy / Scoring Path:** A qualitative summary of the primary playstyle utilized by the civilization to pursue their Victory Points.

---
