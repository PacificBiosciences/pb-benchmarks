import pysam
from collections import defaultdict
import argparse

def process_vcf(vcf_file, sample_name="QUERY"):
    """
    Processes a VCF file to calculate allele-specific length differences grouped by SNVs and INDELs,
    for the specified sample, grouped by the `BD` format field.

    Args:
        vcf_file (str): Path to the VCF file.
        sample_name (str): Name of the sample to process (default is "QUERY").

    Returns:
        tuple: Two dictionaries (for SNVs and INDELs), where keys are `BD` values (or FN for "."), and
               values are the total differences summed across alleles for each variant type.
    """
    # Open the VCF file
    vcf = pysam.VariantFile(vcf_file)

    # Check if the sample exists
    if sample_name not in vcf.header.samples:
        raise ValueError(f"Sample '{sample_name}' not found in VCF file.")

    # Initialize dictionaries to store sums of differences grouped by BD
    snv_sums = defaultdict(int)
    indel_sums = defaultdict(int)

    # Iterate over the records in the VCF file
    for record in vcf:
        # Get the BD value for the sample
        if "BD" not in record.format:
            continue  # Skip if BD is not available
        bd_value = record.samples[sample_name]["BD"]
        if bd_value is None or bd_value == ".":
            bd_value = "FN"  # Treat missing BD values as FN

        # Get the REF and ALT alleles
        ref = record.ref
        alts = record.alts if record.alts else []  # Handle cases with no ALT alleles

        # Loop over each ALT allele
        for alt in alts:
            # Determine if this is an SNV (REF and ALT are length 1)
            if len(ref) == 1 and len(alt) == 1:
                snv_sums[bd_value] += 1  # Add fixed length difference for SNVs
            else:
                # For INDELs, calculate the absolute length difference for this allele
                length_diff = abs(len(ref) - len(alt))
                indel_sums[bd_value] += length_diff

    return snv_sums, indel_sums

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process a VCF file and calculate allele-specific length differences by BD.")
    parser.add_argument("vcf_file", help="Path to the input VCF file")
    parser.add_argument("--sample", default="QUERY", help="Sample name to process (default: QUERY)")
    args = parser.parse_args()

    # Process the VCF file
    try:
        snv_sums, indel_sums = process_vcf(args.vcf_file, args.sample)

        # Print SNV summary without headers
        for bd_value, total_difference in snv_sums.items():
            print(f"{bd_value}\tSNV\t{total_difference}")

        # Print INDEL summary without headers
        for bd_value, total_difference in indel_sums.items():
            print(f"{bd_value}\tINDEL\t{total_difference}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
