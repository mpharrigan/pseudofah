import subprocess


class SlurmScheduler:
    def running(self, projname):
        lines = subprocess.check_output(["ss", "-mt"]).decode().splitlines()
        runs = []

        for line in lines:
            _, _, jname, *_, status, _, _, _ = line.split()
            proj, run, gen = jname.split("-")
            if proj != projname:
                continue
            if not status in ["PD", "R"]:
                continue
            run = int(run)
            gen = int(gen)
            runs += [run]

        return set(runs)

    @property
    def qsub(self):
        return "sbatch"

    def jobscript(self, proj, run, gen):
        return "submitjob-{}.sbatch.py".format(gen)
