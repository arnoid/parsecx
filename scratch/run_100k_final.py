import sys
import os
import time
sys.path.append(os.getcwd())
from batch_runner import run_batch

if __name__ == "__main__":
    start_time = time.time()
    # vp_target is unused in the simulation logic now, but kept for filename/compatibility
    run_batch(total_iterations=100000, checkpoint_size=5000, vp_target=10, filename="simulation_report_100k_final.md")
    end_time = time.time()
    print(f"Total time for 100,000 simulations: {end_time - start_time:.2f} seconds")
