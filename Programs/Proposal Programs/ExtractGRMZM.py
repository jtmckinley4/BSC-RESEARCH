import re

def extract_grmzm_numbers(input_filename, output_filename):
    grmzm_numbers = []

    # Open and read the input file
    with open(input_filename, 'r') as infile:
        for line in infile:
            # Extract GRMZM numbers using regular expression
            match = re.search(r'GRMZM\d+G\d+', line)
            if match:
                grmzm_numbers.append(match.group())
    
    # Write extracted GRMZM numbers to output file
    with open(output_filename, 'w') as outfile:
        for number in grmzm_numbers:
            outfile.write(number + '\n')

# Input and output file names
input_filename = 'ZMtoGRMZM.txt'
output_filename = 'extracted_grmzm_numbers.txt'

# Extract and write GRMZM numbers to output file
extract_grmzm_numbers(input_filename, output_filename)


