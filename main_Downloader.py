import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

from ProjectHousePrice import DataClean as DC
from ProjectHousePrice import DataDownload as DD
from ProjectHousePrice import DataExtractor as DX

import sys
import time

def main():
    #Ingatlan.com letöltése
    StartURL = "https://ingatlan.com/lista/elado+lakas+budapest+10-mFt-tol"
    numberOfPages = 5
    IngatlanDownloader = DD()
    HTMLScraper = DX("output\output")
    IngatlanDf = pd.DataFrame()


    # DataDownload(IngatlanDownloader, numberOfPages, StartURL)
    # IngatlanDf = DataExtract(HTMLScraper, numberOfPages, IngatlanDf)
    # IngatlanDf.to_excel("D:\Projects\ProjectRealEstate\IngatlanDB.xlsx")

    #Ez átmeneti, amíg nem lesz kész
    IngatlanDf = pd.read_excel("IngatlanDB.xlsx", index_col=0)
    DataManipulate(IngatlanDf)


def DataManipulate(IngatlanDf: pd.DataFrame):
    ColumnName = ["Price", "location", "size (m2)", "id"]
    IngatlanDf.columns = ColumnName

    SplitColumnsPrice = IngatlanDf["Price"].str.split(expand=True)
    TypeData = SplitColumnsPrice[1].tolist()
    IngatlanDf.iloc[:, 0] = SplitColumnsPrice.iloc[:, 0]
    IngatlanDf.insert(1, "Type", TypeData)
    SplitColumnsSize = IngatlanDf["size (m2)"].str.split(expand=True)
    IngatlanDf.iloc[:, 3] = SplitColumnsSize.iloc[:, 0]
    IngatlanDf["Price"] = IngatlanDf["Price"].str.replace(',', '.').astype(float)
    print(IngatlanDf)



def DataExtract(HTMLScraper: DX, numberOfPages, IngatlanDf:pd.DataFrame) -> pd.DataFrame:
    
    for i in range(numberOfPages):
        try:
            IngatlanDf = HTMLScraper.getData(IngatlanDf, i+1)
        except:
            continue
    
    return IngatlanDf



def DataDownload(IngatlanDownloader: DD, numberOfPages: int, StartURL: str):
    for i in range(numberOfPages):
        if i == 0:
            try:
                IngatlanDownloader.HTMLDownloader(StartURL, i+1)
            except:
                IngatlanDownloader.Driverclose()
                time.sleep(2)
                IngatlanDownloader.StartDriver()
                continue
        else:
            try:
                IngatlanDownloader.HTMLDownloader(StartURL+f"?page={i+1}", i+1)
                
            except:
                IngatlanDownloader.Driverclose()
                time.sleep(2)
                IngatlanDownloader.StartDriver()
                time.sleep(2)
                continue
        time.sleep(5) 

    



def OutlierFilter(df: pd.DataFrame, columnName: str) -> pd.DataFrame:
    """
    Remove outliers from a DataFrame based on the interquartile range (IQR) method.

    Parameters:
    df (pd.DataFrame): The input DataFrame from which to remove outliers.
    columnName (str): The name of the column to check for outliers.

    Returns:
    pd.DataFrame: A DataFrame with outliers removed based on the specified column.
    
    This function calculates the interquartile range (IQR) for the specified column.
    Outliers are defined as data points that fall below Q1 - 1.5*IQR or above Q3 + 1.5*IQR,
    where Q1 is the first quartile (25th percentile) and Q3 is the third quartile (75th percentile).
    The function returns a DataFrame with these outliers removed.
    """
    # Calculate the first quartile (Q1) and third quartile (Q3)
    q_low = df[columnName].quantile(0.25)
    q_hi = df[columnName].quantile(0.75)
    
    # Calculate the interquartile range (IQR)
    iqr = q_hi - q_low
    
    # Define the minimum and maximum bounds for outliers
    Minimum = q_low - 1.5 * iqr
    Maximum = q_hi + 1.5 * iqr
    
    # Filter the DataFrame to remove outliers
    retdf = df[(df[columnName] < Maximum) & (df[columnName] > Minimum)]
    
    return retdf



if __name__ == "__main__":
    main()