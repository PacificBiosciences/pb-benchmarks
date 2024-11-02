#!/usr/bin/env bash

DOCKER_IMAGE="docker://pkrusche/hap.py:latest"

# https://downloads.pacbcloud.com/public/reference-genomes/human_GRCh38_no_alt_analysis_set.tar.2023-12-04.gz
REFERENCE="./human_GRCh38_no_alt_analysis_set.fasta"

# ftp://ftp.ncbi.nlm.nih.gov//giab/ftp/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38/HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz
# ftp://ftp.ncbi.nlm.nih.gov//giab/ftp/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38/HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz.tbi
TRUTH_VCF="./HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz"

# ftp://ftp.ncbi.nlm.nih.gov//giab/ftp/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38/HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed
HC_BED="./HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed"

QUERY_VCF=$1
OUTPUT_PREFIX=${2:-all}

singularity exec --bind "$PWD" ${DOCKER_IMAGE} \
  /opt/hap.py/bin/hap.py --threads 24 -o "${OUTPUT_PREFIX}" \
  --pass-only --gender male \
  --reference ${REFERENCE} --engine=vcfeval \
  --false-positives ${HC_BED} ${TRUTH_VCF} \
  "${QUERY_VCF}"
