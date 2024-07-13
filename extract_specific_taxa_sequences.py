"""
extract_specific_taxa_sequences.py

This script extracts sequences from a FASTA file that belong to a specific taxon and writes them to a new file.

Usage:
    python extract_specific_taxa_sequences.py

Parameters:
    input_file (str): Path to the input FASTA file containing sequences with taxonomic information in headers.
    output_file (str): Path to the output file where sequences of the specified taxon will be written.
    summary_file (str): Path to the summary file where the count and names of the sequences will be written.
    target_taxon (str): The taxon to search for in the headers of the input sequences.

Example:
    python extract_specific_taxa_sequences.py --input_file your_input.fasta --output_file output_rhizobium.fasta --summary_file summary.txt --target_taxon Rhizobium
"""

def extract_specific_taxa_sequences(input_file, output_file, summary_file, target_taxon):
    """
    Extracts sequences from a FASTA file that belong to a specific taxon.

    Parameters:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output file.
        summary_file (str): Path to the summary file.
        target_taxon (str): The taxon to search for.

    Returns:
        None
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile, open(summary_file, 'w') as summaryfile:
        current_sequence = ''
        current_header = ''
        count = 0
        sequence_names = []

        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                # Header line
                if current_sequence and target_taxon in current_header:
                    # Write the sequence to the output file for the previous taxon
                    outfile.write(f"{current_header}\n{current_sequence}\n")
                    count += 1
                    sequence_names.append(current_header.split(' ')[0][1:])  # Extract the sequence name

                # Reset for the new sequence
                current_sequence = ''
                current_header = line  # Store the entire header line
            else:
                # Sequence line
                current_sequence += line

        # Process the last sequence in the file
        if current_sequence and target_taxon in current_header:
            outfile.write(f"{current_header}\n{current_sequence}\n")
            count += 1
            sequence_names.append(current_header.split(' ')[0][1:])  # Extract the sequence name

        # Write summary file
        summaryfile.write(f"Number of sequences found: {count}\n")
        summaryfile.write("Names of the sequences:\n")
        for name in sequence_names:
            summaryfile.write(f"{name}\n")

# Example usage
# In this example we will extract sequences from the Genus Rhizobium 
# Feel free to change it to the taxa of your choice 
fasta_input_file = 'fasta_db.fasta'
output_file_for_specific_taxon = 'output_rhizobium.fasta'
summary_file = 'summary.txt'
target_taxon = 'Rhizobium'

extract_specific_taxa_sequences(fasta_input_file, output_file_for_specific_taxon, summary_file, target_taxon)
