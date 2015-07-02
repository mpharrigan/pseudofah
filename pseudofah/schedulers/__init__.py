from .slurm import SlurmScheduler


def scheduler():
    # TODO: Fancy stuff to determine current scheduler
    return SlurmScheduler()
