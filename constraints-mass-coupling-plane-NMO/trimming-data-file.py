# Open the input file for reading
with open("dune_t2hk_S14.dat", "r") as infile:
    # Read the lines from the input file
    lines = infile.readlines()

# Open a new file for writing the modified data
with open("dune_t2hk_S14.txt", "w") as outfile:
    # Iterate through each line in the input file
    for line in lines:
        # Split the line into columns
        columns = line.split()

        # Iterate through each column
        for i in range(len(columns)):
            # Try to convert the column value to a float
            try:
                value = float(columns[i])
                # Format the float to have 5 digits after the decimal point
                columns[i] = "{:.5f}".format(value)
            except ValueError:
                # If conversion fails, leave the column unchanged
                pass

        # Join the modified columns and write the line to the output file
        outfile.write(" ".join(columns) + "\n")

