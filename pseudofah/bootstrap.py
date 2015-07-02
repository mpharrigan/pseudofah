import sys
import os

if len(sys.argv) != 3:
    print("Usage: {} run template_name".format(sys.argv[0]))
    sys.exit(1)

run = int(sys.argv[1])
rundir = "run-{}".format(run)
os.makedirs(rundir, exist_ok=False)
os.chdir(rundir)

templatename = sys.argv[2]
templatedir = "../../../{}/".format(templatename)
assert os.path.exists(templatedir)
assert os.path.isdir(templatedir)

os.symlink(templatedir, "templates")

os.symlink("../../../runs/{}.inpcrd".format(run), "inpcrd")
os.symlink("../../../runs/{}.prmtop".format(run), "prmtop")

import subprocess

subprocess.call([
    "python",
    "templates/next.py",
    str(run),
    str(0)
])
