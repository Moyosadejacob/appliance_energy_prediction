import pandas as pd

def get_data(file_path):
    """
    This isa function that takes a file path and read in data
    with pandas
    :file_path: is the file path
    : df : resulting data 
    """

    df= pd.read_csv(file_path)

    return df