import collections
from parsec_sim import ParsecSim

def run_batch(total_iterations=10000, checkpoint_size=200, vp_target=7, filename="simulation_balance_report_long_7vp.md"):
    stats = {
        "wins": collections.Counter(),
        "total_rounds": 0,
        "civs_played": collections.Counter(),
        "winner_extensions": collections.Counter(),
        "winner_techs": collections.defaultdict(list)
    }

    print(f"Starting LONG batch simulation of {total_iterations} games (Target: {vp_target} VP) in batches of {checkpoint_size}...")
    
    for i in range(total_iterations):
        sim = ParsecSim(players_count=4, vp_target=vp_target, silent=True)
        for p in sim.players:
            stats["civs_played"][p.civ_name] += 1
            
        result = sim.run()
        print(f"Simulation #{i + 1} executed: Winner = {result['winner_civ']}, Rounds = {result['rounds']}")
        
        stats["wins"][result["winner_civ"]] += 1
        stats["total_rounds"] += result["rounds"]
        
        for ext_id in result["extensions_built"]:
            stats["winner_extensions"][ext_id] += 1
            
        for tech, lv in result["tech_levels"].items():
            stats["winner_techs"][tech].append(lv)

        if (i + 1) % checkpoint_size == 0 or (i + 1) == total_iterations:
            generate_report(stats, i + 1, vp_target, filename)
            print(f"\n--- Batch Checkpoint: {i + 1} games complete. Report updated in {filename}. ---\n")

def generate_report(stats, current_count, vp_target, filename):
    report = []
    report.append(f"# Parsec X Balance Report: {current_count} Simulations (Long {vp_target}VP Mode)\n")
    report.append(f"**Total Games:** {current_count}")
    report.append(f"**Average Game Length:** {stats['total_rounds'] / current_count:.2f} rounds\n")

    report.append("## Civilization Performance")
    report.append("| Civilization | Games Played | Wins | Win Rate |")
    report.append("|---|---|---|---|")
    
    civ_list = sorted(stats["civs_played"].keys(), key=lambda c: stats["wins"][c] / stats["civs_played"][c] if stats["civs_played"][c] > 0 else 0, reverse=True)
    for civ in civ_list:
        played = stats["civs_played"][civ]
        wins = stats["wins"][civ]
        win_rate = (wins / played * 100) if played > 0 else 0
        report.append(f"| {civ} | {played} | {wins} | {win_rate:.1f}% |")

    report.append("\n## Winner's Profile")
    report.append("### Top Extensions for Winners")
    from parsec_sim import EXTENSION_NAMES
    top_exts = stats["winner_extensions"].most_common(5)
    for ext_id, count in top_exts:
        name = EXTENSION_NAMES.get(ext_id, f"Ext {ext_id}")
        report.append(f"- **{name}:** {count} appearances")

    report.append("\n### Average Tech Levels (Winners)")
    for tech, lvs in stats["winner_techs"].items():
        avg_lv = sum(lvs) / len(lvs) if lvs else 0
        report.append(f"- **{tech}:** Level {avg_lv:.2f}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

def run_full_verification():
    # 5VP Baseline (30k sweep)
    run_batch(10000, 200, vp_target=5, filename="master_edition_report_5vp.md")
    # 7VP Endurance
    run_batch(10000, 200, vp_target=7, filename="master_edition_report_7vp.md")
    # 10VP Conquest
    run_batch(10000, 200, vp_target=10, filename="master_edition_report_10vp.md")

if __name__ == "__main__":
    run_full_verification()
