import subprocess
import sys
import glob
import re
from .schedulers import scheduler
from .mdengines import mdengine
from .utility import yes_no, wrap


def potential_runs():
    return set(int(re.match("run-(\d+)", fol).group(1))
               for fol in glob.iglob("run-*"))


def main(projname, regenerate=True):
    potruns = potential_runs()
    print("I found these runs")
    print(wrap(potruns))
    print()

    schej = scheduler()
    okruns = schej.running(projname)
    print("I found these runs properly queued")
    print(wrap(okruns))
    print()

    tosubmit = potruns - okruns
    print("I'm going to submit these runs")
    print(wrap(tosubmit))
    print()

    if yes_no("Should I do it?"):
        print("Alright")
    else:
        print("Ok :(")
        sys.exit(1)

    md = mdengine()
    for run in tosubmit:
        fol = "run-{}".format(run)
        gen = md.get_current_gen(fol)
        if regenerate:
            subprocess.check_call(
                ["python", "templates/next.py", str(run), str(gen)], cwd=fol)
        subprocess.check_call([
            schej.qsub,
            schej.jobscript(projname, run, gen)
        ], cwd=fol)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("projname", help="Project Name")
    parser.add_argument("--regenerate", dest="regenerate", action="store_true")
    parser.add_argument("--no-regenerate", dest="regenerate",
                        action="store_false")
    parser.set_defaults(regenerate=True)
    args = parser.parse_args()
    main(args.projname, args.regenerate)
