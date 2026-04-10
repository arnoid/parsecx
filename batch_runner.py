import collections
from parsec_sim import ParsecSim

def run_batch(total_iterations=10000, checkpoint_size=200, vp_target=7, filename="simulation_balance_report_long_7vp.md"):
    stats = {
        "wins": collections.Counter(),
        "total_rounds": 0,
        "civs_played": collections.Counter(),
        "winner_extensions": collections.Counter(),
        "winner_techs": collections.defaultdict(list),
        "agenda_usage": collections.Counter(),
        "agenda_outcomes": collections.defaultdict(collections.Counter),
        "winner_political_alignment": [],
        "winner_voting_power": [],
        "winner_mandate_wins": collections.Counter()
    }

    print(f"Starting batch simulation of {total_iterations} games (Fixed 10 Rounds) in batches of {checkpoint_size}...")
    
    for i in range(total_iterations):
        sim = ParsecSim(players_count=4, vp_target=vp_target, silent=True)
        for p in sim.players:
            stats["civs_played"][p.civ_name] += 1
            
        result = sim.run()
        if total_iterations <= 1000 or (i + 1) % 1000 == 0:
            winners_str = ", ".join(result['winner_civ'])
            print(f"Simulation #{i + 1} executed: Winner(s) = {winners_str}, Rounds = {result['rounds']}")
        
        for winner_civ in result["winner_civ"]:
            stats["wins"][winner_civ] += 1
            # Political Stats for Winners
            w_idx = next(idx for idx, p in enumerate(sim.players) if p.civ_name == winner_civ)
            winner = sim.players[w_idx]
            
            # 1. Voting Power Usage
            game_avg_power = (sum(v[3] for v in winner.vote_history) / len(winner.vote_history)) if winner.vote_history else 0
            stats["winner_voting_power"].append(game_avg_power)
            
            # 2. Political Alignment (Did winner vote for the outcome?)
            alignment_count = 0
            for v_round, v_agenda_id, v_choice, v_power in winner.vote_history:
                try:
                    outcome = next(o[1] for o in sim.council_outcomes if o[0] == v_agenda_id)
                    if v_choice == outcome:
                        alignment_count += 1
                        if "PLAYER_" in outcome and outcome == f"PLAYER_{w_idx}":
                            stats["winner_mandate_wins"][v_agenda_id] += 1
                except StopIteration:
                    pass
            if winner.vote_history:
                stats["winner_political_alignment"].append(alignment_count / len(winner.vote_history))

        # Global Council Stats
        for agenda_id, outcome in sim.council_outcomes:
            stats["agenda_usage"][agenda_id] += 1
            stats["agenda_outcomes"][agenda_id][outcome] += 1

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
    report.append(f"# Parsec X Balance Report: {current_count} Simulations (Fixed 10-Round Mode)\n")
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
    report.append("### All Extensions Built by Winners")
    from parsec_sim import EXTENSION_NAMES, EXTENSION_DESCRIPTIONS
    all_exts = stats["winner_extensions"].most_common()
    for ext_id, count in all_exts:
        name = EXTENSION_NAMES.get(ext_id, f"Ext {ext_id}")
        desc = EXTENSION_DESCRIPTIONS.get(ext_id, "")
        report.append(f"- **{name}:** {count} appearances")
        if desc:
            report.append(f"  *({desc})*")

    report.append("\n## Galactic Council Political Landscape")
    total_sessions = sum(stats["agenda_usage"].values())
    report.append(f"**Total Council Sessions Triggered:** {total_sessions} ({total_sessions/current_count*100:.2f}% of games)")
    report.append("\n| Agenda ID | Agenda Name | Frequency | Most Frequent Outcome | Description |")
    report.append("|---|---|---|---|---|")
    from parsec_sim import AGENDAS
    # Sort by frequency first, then ID
    sorted_agendas = sorted(AGENDAS.items(), key=lambda x: (stats["agenda_usage"].get(x[0], 0), -x[0]), reverse=True)
    
    for agenda_id, agenda in sorted_agendas:
        if agenda_id > 40: continue # Skip variant placeholders if any
        count = stats["agenda_usage"].get(agenda_id, 0)
        outcomes = stats["agenda_outcomes"][agenda_id].most_common(1)
        top_outcome = outcomes[0][0] if outcomes else "N/A"
        desc = agenda["desc"]
        report.append(f"| {agenda_id} | {agenda['name']} | {count} | {top_outcome} | {desc} |")

    report.append("\n### Winner Political Behavior")
    avg_align = (sum(stats["winner_political_alignment"]) / len(stats["winner_political_alignment"])) * 100 if stats["winner_political_alignment"] else 0
    avg_power = sum(stats["winner_voting_power"]) / len(stats["winner_voting_power"]) if stats["winner_voting_power"] else 0
    report.append(f"- **Political Alignment Rate:** {avg_align:.1f}% *(Frequency of winner voting with the majority)*")
    report.append(f"- **Avg Voting Power Spent:** {avg_power:.2f} per Council session")
    
    report.append("\n### All Mandates Held by Winners")
    for agenda_id, count in stats["winner_mandate_wins"].most_common():
        agenda = AGENDAS[agenda_id]
        name = agenda["name"]
        desc = agenda["desc"]
        report.append(f"- **{name}:** {count} times")
        report.append(f"  *({desc})*")

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
