import pandas as pd
from summary_utils import summarizeData

def main():
    # set the file path 
    file_path = "sample.csv"
    summarizeData(file_path)

if __name__ == "__main__":
    main()

##file_path = "sample.csv"

##df = pd.read_csv(file_path)

##print(df)