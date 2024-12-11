import pysam
from collections import defaultdict
import argparse

def process_vcf(vcf_file, sample_name="QUERY"):
    """
    Processes a VCF file to calculate the max allele length differences grouped by SNVs and INDELs,
    for the specified sample, grouped by the `BD` format field.
    
    Args:
        vcf_file (str): Path to the VCF file.
        sample_name (str): Name of the sample to process (default is "QUERY").
    
    Returns:
        tuple: Two dictionaries (for SNVs and INDELs), where keys are `BD` values, and
               values are the total max differences for each variant type.
    """
    # Open the VCF file
    vcf = pysam.VariantFile(vcf_file)
    
    # Check if the sample exists
    if sample_name not in vcf.header.samples:
        raise ValueError(f"Sample '{sample_name}' not found in VCF file.")
    
    # Initialize dictionaries to store sums of max differences grouped by BD
    snv_sums = defaultdict(int)
    indel_sums = defaultdict(int)
    
    # Iterate over the records in the VCF file
    for record in vcf:
        # Get the BD value for the sample
        if "BD" not in record.format:
            continue  # Skip if BD is not available
        bd_value = record.samples[sample_name]["BD"]
        if bd_value is None:
            continue  # Skip if BD is missing
        
        # Get the REF and ALT alleles
        ref = record.ref
        alts = record.alts if record.alts else []  # Handle cases with no ALT alleles
        
        # Determine if this is an SNV (all alleles are length 1)
        is_snv = len(ref) == 1 and all(len(alt) == 1 for alt in alts)
        
        if is_snv:
            # SNVs have a default length difference of 1
            snv_sums[bd_value] += 1
        else:
            # INDELs: Calculate max difference in length between REF and ALT alleles
            max_diff = max(abs(len(ref) - len(alt)) for alt in alts) if alts else 0
            indel_sums[bd_value] += max_diff
    
    return snv_sums, indel_sums

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process a VCF file and calculate max length differences by BD.")
    parser.add_argument("vcf_file", help="Path to the input VCF file")
    parser.add_argument("--sample", default="QUERY", help="Sample name to process (default: QUERY)")
    args = parser.parse_args()

    # Process the VCF file
    try:
        snv_sums, indel_sums = process_vcf(args.vcf_file, args.sample)
        
        # Print SNV summary
        print("SNV Summary:")
        for bd_value, total_difference in snv_sums.items():
            print(f"BD={bd_value}: Total SNV Length Difference={total_difference}")
        
        # Print INDEL summary
        print("\nINDEL Summary:")
        for bd_value, total_difference in indel_sums.items():
            print(f"BD={bd_value}: Total INDEL Length Difference={total_difference}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
