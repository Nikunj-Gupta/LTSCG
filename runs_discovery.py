import os

RUNS_DIRECTORY = "runs_ltscg/" 
PARTITION = "main"

def write_run_file(content, num): 
    os.makedirs(RUNS_DIRECTORY, exist_ok=True)    
    f = open(f"{RUNS_DIRECTORY}/run_{num}.job", "a")
    f.write(content)
    f.close()

# 1. SLURM header for the single script:
file = f"""#!/bin/bash
#SBATCH --account=prasanna_1363
#SBATCH --partition={PARTITION}
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --mem=128G
#SBATCH --time=48:00:00 

conda activate ltscg
module load gcc/11.3.0 git/2.36.1

echo "Starting parallel job script"
"""

ENVS = ["gather", "gymma"] 
MAX_SEEDS = 11 

"""
Baselines 
""" 
commands = []
count = 0 
for seed in range(MAX_SEEDS): 
    for env in ENVS: 
            if env=="gather": cmd = f"""python3 src/main.py --config=ltscg --env-config=gather with seed={seed} use_cuda=False""" 
            if env=="gymma": cmd = f"""python3 src/main.py --config=ltscg --env-config=gymma with env_args.key="pz-mpe-simple-tag-v3" seed={seed} use_cuda=False""" 
            count+=1
            write_run_file(file+cmd, count) 