#!/bin/bash
#SBATCH -p compute
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --cpus-per-task 24
#SBATCH -o slurm-%x-%j-%N.out


singularity exec \
  --bind $PWD,{XXX}/workflow_resources:/data \
  /pbi/flash/wrowell/workflow_resources/hap.py_latest.sif \
  /opt/hap.py/bin/hap.py --threads 24 -o ${2:-all} --pass-only \
  --gender male \
  -r /data/reference/human_GRCh38_no_alt_analysis_set.fasta \
  -f /data/resources/happy/HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed.gz \
  --stratification /data/resources/stratifications/v2.0-GRCh38-stratifications.tsv \
  --engine=vcfeval --engine-vcfeval-template /data/reference/human_GRCh38_no_alt_analysis_set.sdf \
  /data/resources/happy/HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz \
  $