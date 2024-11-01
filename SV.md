# Get Q100 truthset
wget https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/analysis/NIST_HG002_DraftBenchmark_defrabbV0.015-20240215/GRCh38_HG2-T2TQ100-V1.0.vcf.gz

grep -v chr[XY] GRCh38_HG2-T2TQ100-V1.0_stvar.benchmark.bed > GRCh38_HG2-T2TQ100-V1.0_stvar.benchmark.only_autosomes.bed

# Create an sv filtered version of the truth set:
bcftools view -i 'INFO/SVTYPE!="."' -Oz -o GRCh38_HG2-T2TQ100-V1.0.svtype.vcf.gz GRCh38_HG2-T2TQ100-V1.0.vcf.gz
bcftools index -t GRCh38_HG2-T2TQ100-V1.0.svtype.vcf.gz

# Counting confident truth set:
bedtools intersect -header -f 1.0 -wa -a GRCh38_HG2-T2TQ100-V1.0.svtype.vcf.gz -b GRCh38_HG2-T2TQ100-V1.0_stvar.benchmark.bed | bcftools view --no-header -i 'strlen(REF)>50 || max(strlen(ALT))>50' - | wc -l
