import pandas as pd


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



dictionary, columns, sel = compression_algorithm("./combined_binary_mutations_non_snp_corrected_0.2_column_corrected.tsv")

compressed_file_writer("./test.cbt", dictionary, columns, sel)

#print(arr)
