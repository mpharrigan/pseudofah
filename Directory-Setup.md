Directory Setup
===============

 - data/
    - run-0/
    - run-1/
    - run-2/
        - topol.tpr -> ../../runs/2.tpr
          (or inpcrd)
        - trajout_comp.xtc
          (or mdcrd.2)
        - submitjob-2.job.py
        - simulate-2.sh
        - templates/ -> path/to/pseudofah/templates/gromacs/cpu-16/slurm/normal/
 - inpcrds/
    - 0.inpcrd
    - 1.inpcrd
    - 2.inpcrd
 - prmtops/
    - 3rvy.prmtop
 - runs/
    - 0.inpcrd -> ../inpcrds/0.inpcrd
    - 0.prmtop -> ../prmtops/3rvy.prmtop
    - 2.inpcrd -> ../inpcrds/2.inpcrd
    - 2.prmtop -> ../prmtops/3rvy.prmtop
    
