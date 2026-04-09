import sys
import os
sys.path.append(os.getcwd())
from batch_runner import run_batch
import time

if __name__ == "__main__":
    start_time = time.time()
    run_batch(total_iterations=10000, checkpoint_size=500, vp_target=5, filename="simulation_report_5vp_10k.md")
    end_time = time.time()
    print(f"Total time for 10,000 simulations: {end_time - start_time:.2f} seconds")
