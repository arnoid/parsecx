# Civilization Balance Changes: Wulfram & Aiiji

This document summarizes the specific tuning adjustments made to balance the **Wulfram Collective** (nerf) and **The Aiiji** (buff) during the simulation-driven optimization passes.

## ⚖️ Wulfram Collective (The Hegemon's Restraint)
**Objective:** Reduce early-game dominance by slowing down ship production and tech acceleration.

| Feature | Change Description |
|---|---|
| **Upkeep** | Changed from **+1 Ore** to **+1 Influence** per turn. |
| **Meta Impact** | Win rate reduced from ~42% to a stable **31.8%** across all modes. |

---

## 🧘 The Aiiji (The Enlightenment Synthesis)
**Objective:** Break the resource dead-end and bridge the military production gap.

| Feature | Change Description |
|---|---|
| **Upkeep** | Flat **+2 Credits** per turn (replaces randomized 1d3 Credits). |
| **Synthesis** | New conversion rule: **1 Credit to 1 Ore**. Allows spending wealth on ships and tech. |
| **Tech Discount** | New **Command Tech Discount**: -1 Influence to upgrade. |
| **Maneuver** | Bonus upgraded to **General Reroll**: Applicable to Attack, Defense, or Exploration dice. |
| **Meta Impact** | Win rate increased from ~8% to a competitive **19.4%** baseline. |

---

## V1.1 Epic Game Balance Patch

**Objective:** Correct scaling anomalies exposed during 10 VP / marathon length simulations.

| Civilization | Change Description |
|---|---|
| **The Aiiji (Nerf)** | **The Enlightenment Synthesis Scaling Cap**: The "Political Synthesis" ability cost now scales instead of being a flat rate. Starting cost is 6 Influence, increasing by +3 for each subsequent use (6 -> 9 -> 12 -> 15). |
| **The Conversation (Buff)** | **Persistent Negotiation Economy**: Added a permanent Upkeep bonus of +1 Credit and +1 Influence. Resource conversion is now bi-directional (Credits <-> Influence). Gained `DefenseReroll` combat bonus. |
