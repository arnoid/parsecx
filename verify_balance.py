import random
from parsec_sim import ParsecSim, Resource
from collections import Counter

def run_simulation_batch(count=10000):
    winner_seats = Counter()
    winner_civs = Counter()
    total_rounds = 0
    
    for _ in range(count):
        sim = ParsecSim(players_count=4, silent=True)
        results = sim.run()
        
        # In case of shared victory, count all winners
        winners = results["winner_civ"]
        for civ_name in winners:
            winner_civs[civ_name] += 1
            # Find which seat this civ occupied
            seat = next(p.id for p in sim.players if p.civ_name == civ_name)
            winner_seats[seat] += 1
        
        total_rounds += results["rounds"]

    print(f"\n--- Batch Results ({count} games) ---")
    print(f"Avg Rounds per Game: {total_rounds / count:.2f}")
    
    print("\nWin Rate by Seat (0 is first position in R1):")
    for seat in range(4):
        wr = (winner_seats[seat] / count) * 100
        print(f"Seat {seat}: {wr:.2f}% ({winner_seats[seat]} wins)")

    print("\nWin Rate by Civilization:")
    for civ, wins in winner_civs.most_common():
        wr = (wins / count) * 100
        print(f"{civ:20}: {wr:.2f}%")

if __name__ == "__main__":
    run_simulation_batch(10000)
