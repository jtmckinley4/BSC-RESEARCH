from Bio import SeqIO

def soft_mapping_gap_alignment(genomic_file, cdna_file, output_file):
    genomic_seq_record = SeqIO.read(genomic_file, "txt")
    cdna_seq_record = SeqIO.read(cdna_file, "txt")
    
    genomic_seq = genomic_seq_record.seq
    cdna_seq = cdna_seq_record.seq
    
    aligned_seq = []
    for genomic_base, cdna_base in zip(genomic_seq, cdna_seq):
        if genomic_base == cdna_base:
            aligned_seq.append(genomic_base.upper())
        else:
            aligned_seq.append(genomic_base.lower())
    
    aligned_seq = ''.join(aligned_seq)
    
    with open(output_file, 'w') as f:
        f.write(f'>{genomic_seq_record.id} (Exons in uppercase, Introns in lowercase)\n')
        f.write(f'{aligned_seq}\n')

if __name__ == "__main__":
    genomic_file = "genomic.txt"
    cdna_file = "cdna.txt"
    output_file = "aligned_sequence.txt"
    
    soft_mapping_gap_alignment(genomic_file, cdna_file, output_file)
