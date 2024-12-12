# SV benchmarking

- [GIAB FTP](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/analysis/NIST_HG002_DraftBenchmark_defrabbV0.015-20240215/)

## Download Q100 truthset

```bash
BASE_URL="https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/analysis/NIST_HG002_DraftBenchmark_defrabbV0.015-20240215/"

wget "$BASE_URL/GRCh38_HG2-T2TQ100-V1.0.vcf.gz"
wget "$BASE_URL/GRCh38_HG2-T2TQ100-V1.0_stvar.benchmark.bed"
```

## Create an sv filtered version of the truth set

```bash
grep -v chr[XY] \
  GRCh38_HG2-T2TQ100-V1.0_stvar.benchmark.bed \
> GRCh38_HG2-T2TQ100-V1.0_stvar.benchmark.only_autosomes.bed

bcftools view \
  -i 'INFO/SVTYPE!="."' \
  -Oz -o GRCh38_HG2-T2TQ100-V1.0.svtype.vcf.gz \
  GRCh38_HG2-T2TQ100-V1.0.vcf.gz
bcftools index -t \
  GRCh38_HG2-T2TQ100-V1.0.svtype.vcf.gz
```

## Counting confident truth set

```bash
bedtools intersect \
  -header -f 1.0 -wa \
  -a GRCh38_HG2-T2TQ100-V1.0.svtype.vcf.gz \
  -b GRCh38_HG2-T2TQ100-V1.0_stvar.benchmark.bed \
| bcftools view --no-header \
  -i 'strlen(REF)>50 || max(strlen(ALT))>50' - \
| wc -l
```

## Benchmark variants against truth set

```bash
# benchmark
truvari bench \
  --reference ${reference_fasta} \
  --includebed ${benchmark_region_bed} \
  --base ${benchmark_vcf} \
  --comp ${input_sv_call_vcf} \
  --output ${output_dir} \
  --passonly --pickac --dup-to-ins

# harmonize representations
truvari refine \
  --reference ${reference_fasta} \
  --regions ${output_dir}/candidate.refine.bed \
  --recount \
  --use-region-coords \
  --use-original-vcfs \
  --alignmafft \
  ${output_dir}

# assess benchmarking results
truvari ga4gh \
  --input ${output_dir} \
  --output ${output_dir}/combined_result \
  --with-refine
```

## Run final summary script
```bash
  python process_truvari_ga4gh_vcfs.py  \
  --truth-vcf  ga4gh_with_refine_truth.vcf.gz \ 
  --query-vcf ga4gh_with_refine_query.vcf.gz
```