import os
import csv

def generateOut(directory):
    """
    Loops through a directory and reads the first line of every file.

    Args:
        directory (str): Path to the directory containing files.

    Returns:
        dict: A dictionary where keys are filenames and values are the first lines of the files.
    """
    outs = {}

    # Check if the directory exists
    directory=directory+'/xyz'
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return outs

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        fileID=filename.split(".")[0]
        # Ensure it's a file (not a directory)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    energy=file.readlines()[1].split(" ")[2]
                    #first_line = file.readline().strip()
                    outs[fileID] = energy
            except Exception as e:
                print(f"Could not read file '{filename}': {e}")
    outs=dict(sorted(outs.items(), key=lambda item: item[1],reverse=True))

    output_file = directory+"/out.csv"

    # Write the dictionary to a CSV file
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ID", "Energy"])
        # Write each key-value pair
        for key, value in outs.items():
            writer.writerow([key, value])


    return outs

print(generateOut('data/out'))