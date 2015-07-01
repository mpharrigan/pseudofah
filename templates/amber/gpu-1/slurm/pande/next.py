"""Jinja template the next gen."""

from jinja2 import Environment, FileSystemLoader
import glob
import os

def next(run, gen, templates="templates"):
    
    templ_vars = dict(
            run=run,
            gen=gen,
            next_gen=gen+1
    )

    # jinja2 can't follow symlinks until v2.8 (not yet)
    real_templates = os.path.realpath(templates)
    env = Environment(loader=FileSystemLoader(real_templates))

    for fn in glob.glob("{}/*".format(templates)):
        in_fn = os.path.basename(fn)
        print("Loading template", in_fn)
        templ = env.get_template(in_fn)
        out_fn = in_fn.replace("GENI", str(gen))
        with open(out_fn, 'w') as f:
            f.write(templ.render(**templ_vars))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: {} run [gen]".format(sys.argv[0]))
        sys.exit(1)
    next(int(sys.argv[1]), int(sys.argv[2]))
