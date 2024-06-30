# Remove Duplicates

def remove_duplicates(input_file, output_file):
    seen_transcripts = set()
    seen_genes = set()
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('#'):  # skip header lines
                outfile.write(line)
                continue
            
            fields = line.strip().split('\t')
            attributes = fields[8]
            
            transcript_id = attributes.split(';')[0].split('"')[1]
            gene_id = attributes.split(';')[1].split('"')[1]
            
            if transcript_id not in seen_transcripts and gene_id not in seen_genes:
                seen_transcripts.add(transcript_id)
                seen_genes.add(gene_id)
                outfile.write(line)

if __name__ == '__main__':
    input_file = 'maize_with_lncRNAs_renamed.gtf'
    output_file = 'output_lncrnas.gtf'
    remove_duplicates(input_file, output_file)
