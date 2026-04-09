import collections
import statistics
from parsec_sim import ParsecSim

def run_batch(iterations=10000):
    win_counts = collections.Counter()
    total_rounds = []
    vp_stats = collections.defaultdict(list)
    extensions_built = collections.Counter()
    
    print(f"Running {iterations} simulations...")
    
    for i in range(iterations):
        if i % 1000 == 0:
            print(f"Progress: {i}/{iterations}...")
            
        sim = ParsecSim(players_count=4, vp_target=5, silent=True)
        result = sim.run()
        
        # Winner stats (handle shared victory)
        winners = result["winner_civ"]
        for w in winners:
            win_counts[w] += 1 / len(winners)
            
        total_rounds.append(result["rounds"])
        
        for civ, vp in result["vp_counts"].items():
            vp_stats[civ].append(vp)
            
        for ext in result.get("extensions_built", []):
            extensions_built[ext] += 1

    print("\n--- Batch Simulation Results ---")
    print(f"Win Rates:")
    for civ, wins in win_counts.most_common():
        rate = (wins / iterations) * 100
        print(f"  {civ}: {rate:.2f}%")
        
    print(f"\nAverage Game Length: {statistics.mean(total_rounds):.2f} rounds")
    
    print(f"\nAverage VP per Civilization:")
    for civ, vps in vp_stats.items():
        print(f"  {civ}: {statistics.mean(vps):.2f}")
        
    # Most common extensions for winners
    print(f"\nTop 5 Extensions for Winners:")
    from parsec_sim import EXTENSION_NAMES
    for ext_id, count in extensions_built.most_common(5):
        ext_name = EXTENSION_NAMES.get(ext_id, f"Ext {ext_id}")
        print(f"  {ext_name}: {count} builds")

if __name__ == "__main__":
    run_batch(10000)
