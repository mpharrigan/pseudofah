#!/usr/bin/env python3

#SBATCH --partition=pande
#SBATCH --job-name=v2-{{run}}-{{gen}}
#SBATCH --output=v2-{{run}}-{{gen}}-%j.sout
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=harrigan@stanford.edu

#SBATCH --nodes=1
#SBATCH --time=2-00:00:00
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1

import os
import subprocess
import sys

os.chdir(os.environ.get('SLURM_SUBMIT_DIR', '.'))
jobid = os.environ.get('SLURM_JOB_ID')
sys.path.insert(0, ".")

## Set up the next job and submit it as a dependency
from next import next
next({{run}}, {{next_gen}})
subprocess.call([
    "sbatch",
    "--dependency=afterok:{}".format(jobid),
    "submitjob-{{next_gen}}.sbatch.py"
])



## Submit new job
from get_time_left import get_time_left
hours = get_time_left(jobid)
print("Starting mdrun with {} hours".format(hours))
ret = subprocess.call(["bash", "simulate-{{gen}}.sh", str(hours)])
sys.exit(ret)

