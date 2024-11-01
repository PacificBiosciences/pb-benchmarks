# pb-benchmarks

The provenance of benchmark datasets and the resulting statistics are tracked in this readme. This readme provides the information required to reproduce the results. If questions/concerns arise, please open an issue. 

Application note: https://www.pacb.com/wp-content/uploads/Application-brief-Comprehensive-human-genomic-variant-detection-with-HiFi-long-read-sequencing.pdf 

Small variant benchmarks were done against GIAB 4.2.1 HG002, and the structural variant benchmarks were carried out against GIAB T2T V1.0 HG002. 

## PacBio HiFi 
- The variant calls provided are assoicated with the SPRQ chemistry (https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/GIAB_trio/)
- small variants: https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/
- structural variants: https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/

### small variant results (DeepVariant 1.6 full coverage 20-fold)
| Type | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
|------|--------|-------------|----------|----------|-------------|----------|-----------|-------|---------------|------------------|----------------|-----------------|
| INDEL | PASS  | 525469      | 513484   | 11985    | 956105      | 9346     | 414296    | 5286  | 0.977192      | 0.98275          | 0.433316       | 0.979963        |
| SNP   | PASS  | 3365127     | 3356805  | 8322     | 4143790     | 2255     | 779837    | 1225  | 0.997527      | 0.99933          | 0.188194       | 0.998428        |

### small variant results (DeepVariant 1.6 full coverage 30-fold)
| Type | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
|------|--------|-------------|----------|----------|-------------|----------|-----------|-------|---------------|------------------|----------------|-----------------|
| INDEL | PASS  | 525469      | 520114   | 5355     | 971125      | 4625     | 426619    | 2506  | 0.989809      | 0.991506         | 0.439304       | 0.990657        |
| SNP   | PASS  | 3365127     | 3362495  | 2632     | 4177463     | 1152     | 808868    | 492   | 0.999218      | 0.999658         | 0.193627       | 0.999438        |

### structural variant titration results (Sawfish)
| depth | recall | precision  | F1-score    |
|-------|--------|-------|-------|
| 9.72    | 0.8804 | 0.99  | 0.932 |
| 11.67    | 0.9072 | 0.9895 | 0.9466 |
| 13.61    | 0.9229 | 0.9894 | 0.955 |
| 15.56    | 0.9356 | 0.9894 | 0.9618 |
| 17.5    | 0.9411 | 0.9891 | 0.9645 |
| 19.45    | 0.9463 | 0.9891 | 0.9672 |
| 24.31    | 0.9525 | 0.9882 | 0.9701 |
| 29.17    | 0.956  | 0.9885 | 0.972 |
| 34.04    | 0.9586 | 0.9883 | 0.9733 |
| 38.9    | 0.9608 | 0.9882 | 0.9743 |


## Illumina 
 - https://zenodo.org/records/8350256 (4.2.1), https://www.illumina.com/science/genomics-research/articles/CMRG_hg38.html (3.7.5)
 - small variants 4.2.1: HG002_35x.hard-filtered.vcf.gz (388f58faa52a8811fe19b06533d2c3d5)
 - small variants 3.7.5: HG002.30x_novaseq_pcrfree.dragen.vcf.gz (cf2c302a99b96e1e4806cb644524357c) 
 - structural variants 4.2.1: HG002_35x.sv.vcf.gz (760b9c5c295fc82b045f83ed15e524a9)


### small variant results (full coverage 35-fold Dragen 4.2.1)
| Type | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
|------|--------|-------------|----------|----------|-------------|----------|-----------|-------|---------------|------------------|----------------|-----------------|
| INDEL | PASS | 525469 | 524141 | 1328 | 980875 | 721 | 433435 | 474 | 0.997473 | 0.998683 | 0.441886 | 0.998077 |
| SNP | PASS | 3365127 | 3357852 | 7275 | 3849974 | 1860 | 489362 | 985 | 0.997838 | 0.999447 | 0.127108 | 0.998642 |

### small variant results (full coverage 30-fold, Dragen 3.7.5)
| Type | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
|------|--------|-------------|----------|----------|-------------|----------|-----------|-------|---------------|------------------|----------------|-----------------|
| INDEL | PASS  | 525469      | 521874   | 3595     | 995996      | 3500     | 448346    | 1869  | 0.993158      | 0.993609         | 0.450148       | 0.993384        |
| SNP   | PASS  | 3365127     | 3353531  | 11596    | 4042134     | 14752    | 672953    | 3869  | 0.996554      | 0.995621         | 0.166485       | 0.996088        |


### structural variation results (full coverage 35-fold, Dragen 4.2.1)
| TP_base | TP_comp | FP  | FN    | recall | precision | f1    |
|---------|---------|-----|-------|--------|-----------|-------|
| 8645    | 7857    | 235 | 13605 | 0.3885 | 0.971     | 0.555 |

## ONT
 - https://labs.epi2me.io/giab-2023.05/
 - small variants: hg002.wf_snp.vcf.gz (fa2111cdeb4959e1ed1cfe402d128c39)
 - structural variants: hg002.wf_sv.vcf.gz (cd185fb011345e702f7eb2ba7a19213b)

### structural variant results (full 60-fold coverage)
| TP_base | TP_comp | FP   | FN   | recall | precision | f1    |
|---------|---------|------|------|--------|-----------|-------|
| 12806   | 10586   | 114  | 1755 | 0.8795 | 0.9893    | 0.9312 |


### small variant results (full 60-fold coverage)
| Type | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
|------|--------|-------------|----------|----------|-------------|----------|-----------|-------|---------------|------------------|----------------|-----------------|
| INDEL | PASS | 525469 | 453173 | 72296 | 776968 | 24911 | 283861 | 8400 | 0.862416 | 0.949482 | 0.365345 | 0.903857 |
| SNP | PASS | 3365127 | 3357580 | 7547 | 4418637 | 4925 | 1054410 | 1166 | 0.997757 | 0.998536 | 0.238628 | 0.998147 |


## GIAB 4.2.1 truthset (small variants)
 - ftp://ftp.ncbi.nlm.nih.gov//giab/ftp/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38
 - HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz (dc750b3807d4af1f7ffec852e9c2f771)
 - HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed.gz (79e87791bb5184477b1fd1d48898479a)

## GIAB T2T (T2T_V0.015-20240215_T2T-HG002-Q100v1.0) (structural variants)
 - see SV.md
 - for benchmarking steps using true vari please see: https://www.biorxiv.org/content/10.1101/2024.08.19.608674v1

## hap.py (small variants)
- version: v0.3.8-17-gf15de4a
- script to run the small variant benchmarks is provided in the repo: happy_runner.sbatch
