import glob
import re


class Amber:
    def get_current_gen(self, fol):
        gens = glob.glob("{}/mdcrd.*".format(fol))

        def key(x):
            s = re.search("mdcrd.(\d+)", x).group(1)
            return int(s)

        gen = sorted(gens, key=key)[-1]
        gen = key(gen) + 1
        return gen
