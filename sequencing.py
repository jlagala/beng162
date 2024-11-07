import csv
from Bio import AlignIO

# Load fasta alignment file
alignment = AlignIO.read("T2 All Class Alignment.fasta", "fasta")

# Define reference sequence (assumes it's the first in the file)
reference = alignment[0].seq
start_marker = "CACTTCAGGACAGCATGTTTGCT"
end_marker = "CACACCCCCATTTCCTGGA"

# Find starting and ending positions in reference sequence
start_pos = str(reference).find(start_marker)
end_pos = str(reference).find(end_marker) + len(end_marker)

# Trim reference and sample sequences
trimmed_reference = reference[start_pos:end_pos]

indel_data = []

# Loop through each sample sequence
for record in alignment[1:]:
    sample_id = record.id
    sample_seq = record.seq[start_pos:end_pos]

    insertions = []
    deletions = []
    i = 0
    ref_position = 0 

    while i < len(trimmed_reference):
        if trimmed_reference[i] != '-': 
            ref_position += 1

        # Detect insertion in sample
        if trimmed_reference[i] == '-' and sample_seq[i] != '-':
            insertion_start = ref_position + 1 # Idk why I need to do this, but it kinda works
            insertion_length = 0
            while i < len(trimmed_reference) and trimmed_reference[i] == '-' and sample_seq[i] != '-':
                insertion_length += 1
                i += 1
            insertions.append((insertion_start, insertion_length))
        
        # Detect deletion in sample
        elif trimmed_reference[i] != '-' and sample_seq[i] == '-':
            deletion_start = ref_position + 1 # Idk why I need to do this, but it kinda works
            deletion_length = 0
            while i < len(trimmed_reference) and trimmed_reference[i] != '-' and sample_seq[i] == '-':
                deletion_length += 1
                i += 1
            deletions.append((deletion_start, deletion_length))
        
        else:
            i += 1

    # Add the sample data to the main indel_data list
    indel_data.append({
        "Sample ID": sample_id,
        "Insertion Positions": [ins[0] for ins in insertions],
        "Insertion Lengths": [ins[1] for ins in insertions],
        "Deletion Positions": [del_[0] for del_ in deletions],
        "Deletion Lengths": [del_[1] for del_ in deletions]
    })

# Write the results to a CSV file
output_csv_file = "indel_analysis_results_t2.csv"
with open(output_csv_file, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([
        "Sample ID", 
        "Insertion Positions", "Insertion Lengths", 
        "Deletion Positions", "Deletion Lengths"
    ])

    for data in indel_data:
        insertion_positions = ", ".join(map(str, data["Insertion Positions"])) if data["Insertion Positions"] else ""
        insertion_lengths = ", ".join(map(str, data["Insertion Lengths"])) if data["Insertion Lengths"] else ""
        deletion_positions = ", ".join(map(str, data["Deletion Positions"])) if data["Deletion Positions"] else ""
        deletion_lengths = ", ".join(map(str, data["Deletion Lengths"])) if data["Deletion Lengths"] else ""
        
        csvwriter.writerow([
            data["Sample ID"], 
            insertion_positions, insertion_lengths, 
            deletion_positions, deletion_lengths
        ])

print(f"Results have been saved to '{output_csv_file}'.")
