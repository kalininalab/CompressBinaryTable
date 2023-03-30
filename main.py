import pandas as pd


# Compresses the binary table
def compression_algorithm(input_file):

    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file, sep=",", dtype={"name/position": str, "outcome": int, "*": int})
        print("CSV")
    elif input_file.endswith(".tsv"):
        df = pd.read_csv(input_file, sep="\t", dtype={"name/position": str, "outcome": int, "*": int})
        print("TSV")
    else:
        return -1

    columns = df.columns.to_list()
    #print(columns)
    array = df.to_numpy()

    #will be add select 1 as a option too
    selection = 1

    dictionary_of_strains_data = {}

    for strain in array:
        strain_list = strain.tolist()
        strain_name = strain_list[0]
        index_counter = 0
        temp_list = []
        for elem in strain_list[1:]:
            if elem == selection or elem == str(selection):
                temp_list.append(index_counter)
            
            index_counter += 1
        
        dictionary_of_strains_data[strain_name] = temp_list

    
    return dictionary_of_strains_data, columns, selection


# Writes compressed file into outfile 
def compressed_file_writer(outfile, dictionary_of_strains_data, columns, selection):

    with open(outfile, "w") as compressed_file:
        compressed_file.write(str(selection))
        for col in columns[1:]:
            compressed_file.write(";" + str(col))
        compressed_file.write("\n")

        for key in dictionary_of_strains_data.keys():
            compressed_file.write(str(key))
            for index in dictionary_of_strains_data[key]:
                compressed_file.write(";" + str(index))
            
            compressed_file.write("\n")


# Decompresses the compressed file
def decompress_file(compressed_file):

    # Check if given file is properly formatted

    if not compressed_file.endswiht(".cbt"):
        print("Given file is not cbt format")
        return -1

    with open(compressed_file) as infile:
        lines = infile.readlines()

    default_value = str(lines[0].split(";")[0])

    # Checks if it is binary matrix

    if default_value not in ["0" ,"1"]:
        print("Given table is not binary")
        return -1
    
    all_the_strains = []

    # Set the value which will printed to indexes
    
    if default_value == "0":
        indexed_value = "1"
    else:
        indexed_value = "0"
    
    columns = lines[0][1:]

    first_line = []

    first_line.append("name/position")
    columns_split = columns.split(";")
    for col in columns_split:
        first_line.append(col)

    all_the_strains.append(first_line)

    for line in lines[1:]:
        splitted = line.split(";")
        strain_name = splitted[0]
        temp_list = [default_value for _ in range(len(columns.split(";"))+1)]
        temp_list[0] = strain_name
        for index in splitted[1:]:
            temp_list[index] = indexed_value

        all_the_strains.append(temp_list)


    return all_the_strains


# Prints decompressed file to given file name
def decompress_file_printer(outfile_name, all_the_strains, outfile_type="tsv"):

    seperator = None

    if outfile_type == "tsv":
        seperator = "\t"
    elif outfile_type == "csv":
        seperator = ","
    else:
        print("Outfile type can be only csv or tsv")
        return -1

    with open(outfile_name + ".%s" %outfile_type , "w") as ofile:

        for line in all_the_strains:
            ofile.write(str(line[0]))
            for elem in line[1:]:
                ofile.write(seperator + str(elem))
            
            ofile.write("\n")
    
    return 0


dictionary, columns, sel = compression_algorithm("./combined_binary_mutations_non_snp_corrected_0.05.tsv")

compressed_file_writer("./test.cbt", dictionary, columns, sel)

dictionary2, columns2, sel2 = compression_algorithm("/scratch/SCRATCH_SAS/alper/Mycobacterium/non_dropped/combined_binary_mutations.tsv")

compressed_file_writer("./test2.cbt", dictionary2, columns2, sel2)

#print(arr)
