def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    extracted_data = []
    target_states = {'S25', 'S4', 'S17', 'S1', 'S5'}

    for line in lines:
        if line.strip():  # skip empty lines
            grmzm, states = line.strip().split('\t')
            state_list = states.split(',')
            state_list = [state.strip() for state in state_list if state.strip()]  # clean and remove empty strings

            # Remove duplicates by converting to a set and then back to a list
            unique_states = list(set(state_list))

            # Check if all target states are in the unique states
            if target_states.issubset(unique_states):
                extracted_data.append(f"{grmzm}\t{', '.join(unique_states)}")

    # Write the extracted data to the output file
    with open(output_file, 'w') as file:
        for data in extracted_data:
            file.write(data + '\n')

# Example usage
input_file = 'states.txt'
output_file = 'states_output.txt'
process_data(input_file, output_file)
