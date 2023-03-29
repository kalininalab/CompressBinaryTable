import pandas as pd


def compression_algorithm(input_file):

    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file, sep=",", dtype={"name/position": str, "outcome": int, "*": int})
    elif input_file.endswith(".tsv"):
        df = pd.read_csv(input_file, sep=",", dtype={"name/position": str, "outcome": int, "*": int})
    else:
        return -1

    columns = df.columns
    array = df.to_numpy()