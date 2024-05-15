import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from ProjectHousePrice import DataClean as DC
from ProjectHousePrice import DataDownload as DD
from ProjectHousePrice import DataExtractor as DX

import sys

def main():
    #2018-as aadtok elemzése
    RentHousedf = pd.read_csv(r"RentBudapestDataset\flats.csv")
    CleanedData = DC(RentHousedf)

    #Ingatlan.com letöltése
    StartURL = "https://ingatlan.com/lista/elado+lakas+budapest+10-mFt-tol"

    IngatlanDownloader = DD()
    HTMLScraper = DX("output.html")
    IngatlanDf = pd.DataFrame()
    for i in range(2):
        if i == 0:
            print(i)
            IngatlanDownloader.HTMLDownloader(StartURL)
        else:
            IngatlanDownloader.HTMLDownloader(StartURL+f"?page={i+1}")
        IngatlanDf = HTMLScraper.getData(IngatlanDf)
        
    print(IngatlanDf)
    # LocPricedf = CleanedData.HousePriceHue()

    # NoOutlierdfPrice = OutlierFilter(LocPricedf, 'price')
    # NoOutlierdfSize = OutlierFilter(NoOutlierdfPrice, 'size')


    # sns.scatterplot(data=NoOutlierdfPrice, x="latitude", y='longitude', hue="price", size="price")
    # plt.show()

    # sns.displot(NoOutlierdfPrice['price'])
    # plt.show()

    # sns.scatterplot(data=NoOutlierdfSize, x="size", y='price')
    # plt.show()


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