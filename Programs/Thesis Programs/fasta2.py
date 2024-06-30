from Bio import pairwise2
from Bio.Seq import Seq

# Function to read sequences from files
def read_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Function to perform alignment and generate the formatted output
def align_sequences(genomic_seq, cdna_seq):
    alignments = pairwise2.align.globalms(genomic_seq, cdna_seq, 2, -1, -2, -0.5)

    # Get the best alignment
    best_alignment = alignments[0]
    genomic_aligned, cdna_aligned = best_alignment.seqA, best_alignment.seqB

    # Generate the formatted output
    result = []
    for g, c in zip(genomic_aligned, cdna_aligned):
        if c == '-':
            result.append(g.lower())  # Intron (gap in cDNA)
        elif g == '-':
            continue  # Skip gaps in the genomic sequence
        else:
            result.append(g.upper())  # Exon (match or mismatch with cDNA)
    
    return ''.join(result)

def main():
    # Read sequences from files
    genomic_sequence = read_sequence('genomic.txt')
    cdna_sequence = read_sequence('cdna.txt')

    # Perform the alignment
    result_sequence = align_sequences(genomic_sequence, cdna_sequence)

    # Write the result to a file
    with open('aligned_sequence.txt', 'w') as output_file:
        output_file.write(result_sequence)

    print("Alignment complete. Output saved to 'aligned_sequence.txt'.")

if __name__ == "__main__":
    main()
