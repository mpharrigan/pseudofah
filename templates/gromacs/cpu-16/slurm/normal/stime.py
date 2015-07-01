"""Get slurm time"""
import subprocess

def get_time_left(jobid):
    """Get the time left in the current job"""
    tl = subprocess.check_output([
        "bash",
        "get-time-left.sh",
        jobid
    ]).decode()
    tl = tl.split("-")
    if len(tl) > 1:
        days, hms = tl
        days = int(days)
    else:
        hms, = tl
        days = 0
    h, m, s = hms.split(":")
    # Let's be conservative:
    # round down by chopping off minutes, seconds
    hours = int(h) + 24 * days
    return hours
