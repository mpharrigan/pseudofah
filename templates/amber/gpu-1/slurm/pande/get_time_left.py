"""Get slurm time"""
import subprocess

def get_time_left(jobid):
    """Get the time left in the current job"""
    tl = subprocess.check_output([
        "squeue", "-o", "%L", "--noheader", "-j", str(jobid)
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

if __name__ == "__main__":
    import sys
    print(get_time_left(int(sys.argv[1])), "hours")
