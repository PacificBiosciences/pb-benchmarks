# SPRQ benchmark comparisons

[SPRQ Application brief](https://www.pacb.com/wp-content/uploads/Application-brief-Comprehensive-human-genomic-variant-detection-with-HiFi-long-read-sequencing.pdf)

This readme provides the information required to reproduce the results. Please contact [support@pacb.com](mailto:support@pacb.com) with any questions.

HG002 small variants were benchmarked against [GIAB v4.2.1 HG002 GRCh38 truth set](https://ftp.ncbi.nlm.nih.gov/giab/ftp/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38/) with hap.py v0.3.8-17-gf15de4a ([docker://pkrusche/hap.py:latest](https://hub.docker.com/r/pkrusche/hap.py/tags)).
HG002 structural variants were benchmarked against [GIAB T2TQ100 V1.0 HG002 GRCh38 truth set](ftp://ftp.ncbi.nlm.nih.gov//giab/ftp/data/AshkenazimTrio/analysis/NIST_HG002_DraftBenchmark_defrabbV0.015-20240215) with [truvari v4.2.2](https://pypi.org/project/truvari/4.2.2/).

## PacBio HiFi

- HG002 was sequenced on the Revio system with SPRQ chemistry, yielding 146 Gbp.  The reads were aligned with pbmm2 v1.13.1 and downsampled to [20-fold](https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/aligned_bam/HG002-20fold.GRCh38.haplotagged.bam) and [30-fold](https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/aligned_bam/HG002-30fold.GRCh38.haplotagged.bam) aligned depth for variant calling and benchmarking.
- Small variants were called with DeepVariant 1.6.1.
  - [20-fold](https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/HG002-20fold.GRCh38.small_variants.phased.vcf.gz)
  - [30-fold](https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/HG002-30fold.GRCh38.small_variants.phased.vcf.gz)
- Structural variants were called with Sawfish 0.12.4.
  - [20-fold](https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/HG002-20fold.genotyped.sawfish.sv.vcf.gz)
  - [30-fold](https://downloads.pacbcloud.com/public/revio/2024Q4/WGS/benchmark/HG002-30fold.genotyped.sawfish.sv.vcf.gz)

### PacBio HiFi small variant benchmarking results (DeepVariant 1.6.1)

| Depth | Type  | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
| :----: | :---: | ----------: | -------: | -------: | ----------: | -------: | --------: | ----: | ------------: | ---------------: | -------------: | --------------: |
| 20-fold |  SNP  |     3365127 |  3356805 |     8322 |     4143790 |     2255 |    779837 |  1225 |      0.997527 |          0.99933 |       0.188194 |        0.998428 |
| 30-fold |  SNP  |     3365127 |  3362495 |     2632 |     4177463 |     1152 |    808868 |   492 |      0.999218 |         0.999658 |       0.193627 |        0.999438 |
| 20-fold | INDEL |      525469 |   513484 |    11985 |      956105 |     9346 |    414296 |  5286 |      0.977192 |          0.98275 |       0.433316 |        0.979963 |
| 30-fold | INDEL |      525469 |   520114 |     5355 |      971125 |     4625 |    426619 |  2506 |      0.989809 |         0.991506 |       0.439304 |        0.990657 |

### PacBio HiFi structural variant benchmarking results (Sawfish 0.12.4)

| Depth | Recall | Precision | F1-score |
| ----: | ------ | --------- | -------- |
|  9.72 | 0.8804 | 0.9900    | 0.9320   |
| 11.67 | 0.9072 | 0.9895    | 0.9466   |
| 13.61 | 0.9229 | 0.9894    | 0.9550   |
| 15.56 | 0.9356 | 0.9894    | 0.9618   |
| 17.50 | 0.9411 | 0.9891    | 0.9645   |
| 19.45 | 0.9463 | 0.9891    | 0.9672   |
| 24.31 | 0.9525 | 0.9882    | 0.9701   |
| 29.17 | 0.9560 | 0.9885    | 0.9720   |
| 34.04 | 0.9586 | 0.9883    | 0.9733   |
| 38.90 | 0.9608 | 0.9882    | 0.9743   |

## Illumina

- HG002 DRAGEN variant call sets were obtained from [10.5281/zenodo.8350255](https://doi.org/10.5281/zenodo.8350256) (DRAGEN 4.2.1) and the [Illumina Genomics Research Hub](https://www.illumina.com/science/genomics-research/articles/CMRG_hg38.html) (DRAGEN 3.7.5)
- Small variant calls:
  - DRAGEN 4.2.1, 35-fold depth: [HG002_35x.hard-filtered.vcf.gz](https://zenodo.org/records/8350256/files/HG002_35x.hard-filtered.vcf.gz?download=1) (md5sum `388f58faa52a8811fe19b06533d2c3d5`)
  - DRAGEN 3.7.5, 30-fold depth: [HG002.30x_novaseq_pcrfree.dragen.vcf.gz](TKTKTK) (md5sum `cf2c302a99b96e1e4806cb644524357c`)
- Structural variant calls:
  - DRAGEN 4.2.4: [HG002_35x.sv.vcf.gz](https://zenodo.org/records/8350256/files/HG002_35x.sv.vcf.gz?download=1) (md5sum `760b9c5c295fc82b045f83ed15e524a9`)

### Illumina small variant benchmarking results (DRAGEN)

| DRAGEN version | Depth   | Type  | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
| :------------- | ------- | ----- | ------ | ----------: | -------: | -------: | ----------: | -------: | --------: | ----: | ------------: | ---------------: | -------------: | --------------: |
|          3.7.5 | 30-fold | SNP   | PASS   |     3365127 |  3353531 |    11596 |     4042134 |    14752 |    672953 |  3869 |      0.996554 |         0.995621 |       0.166485 |        0.996088 |
|          4.2.4 | 35-fold | SNP   | PASS   |     3365127 |  3357852 |     7275 |     3849974 |     1860 |    489362 |   985 |      0.997838 |         0.999447 |       0.127108 |        0.998642 |
|          3.7.5 | 30-fold | INDEL | PASS   |      525469 |   521874 |     3595 |      995996 |     3500 |    448346 |  1869 |      0.993158 |         0.993609 |       0.450148 |        0.993384 |
|          4.2.4 | 35-fold | INDEL | PASS   |      525469 |   524141 |     1328 |      980875 |      721 |    433435 |   474 |      0.997473 |         0.998683 |       0.441886 |        0.998077 |

### Illumina structural variant benchmarking results (35-fold, DRAGEN 4.2.4)

| TP_base | TP_comp | FP  | FN    | Recall | Precision | F1-score |
|---------|---------|-----|-------|--------|-----------|-------|
| 8645    | 7857    | 235 | 13605 | 0.3885 | 0.971     | 0.555 |

## ONT

- HG002 variant call sets from 60-fold aligned sup-basecall reads were downloaded from the s3 bucket associated with this [EPI2ME](https://labs.epi2me.io/giab-2023.05/) post.
- Small variants were called by Clair3 1.0.0: `hg002.wf_snp.vcf.gz` (`s3://ont-open-data/giab_2023.05/analysis/variant_calling/hg002_sup_60x/hg002.wf_snp.vcf.gz`, md5sum `fa2111cdeb4959e1ed1cfe402d128c39`)
- Structural variants were called by Sniffles2 2.0.7: `hg002.wf_sv.vcf.gz` (`s3://ont-open-data/giab_2023.05/analysis/variant_calling/hg002_sup_60x/hg002.wf_snp.vcf.gz`, md5sum `cd185fb011345e702f7eb2ba7a19213b`)

### ONT small variant benchmarking results (sup-basecall, 60-fold, Clair3 1.0.0)

| Type  | Filter | TRUTH.TOTAL | TRUTH.TP | TRUTH.FN | QUERY.TOTAL | QUERY.FP | QUERY.UNK | FP.gt | METRIC.Recall | METRIC.Precision | METRIC.Frac_NA | METRIC.F1_Score |
| ----- | ------ | ----------: | -------: | -------: | ----------: | -------: | --------: | ----: | ------------: | ---------------: | -------------: | --------------: |
| SNP   | PASS   |     3365127 |  3357580 |     7547 |     4418637 |     4925 |   1054410 |  1166 |      0.997757 |         0.998536 |       0.238628 |        0.998147 |
| INDEL | PASS   |      525469 |   453173 |    72296 |      776968 |    24911 |    283861 |  8400 |      0.862416 |         0.949482 |       0.365345 |        0.903857 |

### ONT structural variant benchmarking results (sup-basecall, 60-fold, Sniffles2 2.0.7)

| TP_base | TP_comp | FP  | FN   | Recall | Precision | F1-score |
| ------: | ------: | --- | ---: | -----: | --------: | -----: |
|   12806 |   10586 | 114 | 1755 | 0.8795 |    0.9893 | 0.9312 |

## GIAB 4.2.1 small variant truthset

- see [small variants readme](./small_variants.md)

## GIAB T2TQ100 V1.0 structural variant truthset (T2T_V0.015-20240215_T2T-HG002-Q100v1.0)

- see [SV readme](./SV.md)
- for benchmarking steps using truevari please see: [Saunders, et al. bioRxiv, 2024](https://www.biorxiv.org/content/10.1101/2024.08.19.608674v1)
