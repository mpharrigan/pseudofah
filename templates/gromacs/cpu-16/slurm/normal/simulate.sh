module load openmpi/1.8.3/gcc-4.8.1
mpiexec -np 16 gmx_mpi mdrun -maxh $1 -cpi
