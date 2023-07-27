#!/bin/bash -l
#SBATCH --account=atom
#SBATCH --job-name=solps_ftx_job
#SBATCH --qos=debug
#SBATCH -C cpu
#SBATCH --nodes=1
#SBATCH --time=00:30:00
#SBATCH --output=log.slurm.stdOut

cd $SLURM_SUBMIT_DIR   # optional, since this is the default behavior

module load python/3.9-anaconda-2021.11
conda activate /global/homes/a/a7l/.conda/envs/ftx
module load PrgEnv-cray cray-python

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/gcc/11.2.0/snos/lib64
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

ips.py --config=ips.ftx.config --platform=conf.ips.perlmutter --log=log.framework 2>>log.stdErr 1>>log.stdOut

egrep -i 'error' log.* > log.errors
