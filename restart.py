import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage {} projname".format(sys.argv[0]))
    sys.exit(1)

myproj = sys.argv[1]

lines = subprocess.check_output(["ss", "-mt"]).decode().splitlines()
runs = []
for line in lines:
    _, _, jname, *_ = line.split()
    proj, run, gen = jname.split("-")
    run = int(run)
    gen = int(gen)
    runs += [(proj,run)]

running = set(runs)
print("These are running", sorted(running))

import glob
import re
import os
for fol in glob.glob("run-*"):
    _, run = fol.split("-")
    run = int(run)
    if (myproj, run) in running:
        print(run, "is running. skipping")
        continue

    scrs = glob.glob("{}/mdcrd.*".format(fol))
    def key(x):
        s = re.search("mdcrd.(\d+)", x).group(1)
        return int(s)
    scr = sorted(scrs, key=key)[-1]
    scr = key(scr) + 1

    print("generating", scr, "in", fol, "(run {})".format(run))
    subprocess.check_call(["python", "templates/next.py", str(run), str(scr)], cwd=fol)
    subprocess.check_call(['sbatch', "submitjob-{}.sbatch.py".format(scr)], cwd=fol)



