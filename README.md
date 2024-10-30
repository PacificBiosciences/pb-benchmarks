# pb-benchmarks

## PacBio HiFi DeepVariant 
- TODO
- small variants:
- structural

## Illumina Dragen 
 - https://zenodo.org/records/8350256
 - small variants: HG002_35x.hard-filtered.vcf.gz (388f58faa52a8811fe19b06533d2c3d5)
 - structural variants: HG002_35x.sv.vcf.gz (760b9c5c295fc82b045f83ed15e524a9)


### small variant results (full coverage 35-fold)
| Type | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
|------|--------|-------------|----------|----------|-------------|----------|-----------|-------|---------------|------------------|----------------|-----------------|
| INDEL | PASS | 525469 | 524141 | 1328 | 980875 | 721 | 433435 | 474 | 0.997473 | 0.998683 | 0.441886 | 0.998077 |
| SNP | PASS | 3365127 | 3357852 | 7275 | 3849974 | 1860 | 489362 | 985 | 0.997838 | 0.999447 | 0.127108 | 0.998642 |


## ONT (full coverage 60-fold)
 - https://labs.epi2me.io/giab-2023.05/
 - small variants: hg002.wf_snp.vcf.gz (fa2111cdeb4959e1ed1cfe402d128c39)
 - structural variants: hg002.wf_sv.vcf.gz (cd185fb011345e702f7eb2ba7a19213b)

### small variant results
| Type | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
|------|--------|-------------|----------|----------|-------------|----------|-----------|-------|---------------|------------------|----------------|-----------------|
| INDEL | PASS | 525469 | 453173 | 72296 | 776968 | 24911 | 283861 | 8400 | 0.862416 | 0.949482 | 0.365345 | 0.903857 |
| SNP | PASS | 3365127 | 3357580 | 7547 | 4418637 | 4925 | 1054410 | 1166 | 0.997757 | 0.998536 | 0.238628 | 0.998147 |


## GIAB 4.2.1 truthset
 - ftp://ftp.ncbi.nlm.nih.gov//giab/ftp/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1, ftp://ftp.ncbi.nlm.nih.gov//giab/ftp/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38
 - HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz (dc750b3807d4af1f7ffec852e9c2f771)
 - HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed.gz (79e87791bb5184477b1fd1d48898479a)

## hap.py 
- v0.3.8-17-gf15de4a
