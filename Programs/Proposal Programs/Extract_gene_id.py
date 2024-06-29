def extract_gene_ids(input_file, output_file):
    seen_genes = set()
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('#'):  # skip header lines
                continue
            
            fields = line.strip().split('\t')
            attributes = fields[8]
            
            gene_id = attributes.split(';')[1].split('"')[1].replace("gene:", "")
            
            if gene_id not in seen_genes:
                seen_genes.add(gene_id)
                outfile.write(gene_id + '\n')

# Usage
input_file = 'output_lncrnas.gtf'
output_file = 'gene_id.txt'
extract_gene_ids(input_file, output_file)

