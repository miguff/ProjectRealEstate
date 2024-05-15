import pandas as pd

class DataClean():

    def __init__(self, RentHousedf: pd.DataFrame) -> None:
        """
        Here we initialize the class with the required Datafframe. The dataframe must have the given parameters
        
        Parameters:
                -'location': The 'location' column is expected to have coordinates in the format '(latitude, longitude)'.
                -'price': The 'price column is expected to be either integer or float.
        """
        self.RentHousedf = RentHousedf

    def HousePriceHue(self) -> pd.DataFrame:
        """
        Processes a DataFrame to extract latitude and longitude from the 'location' column
        and pairs them with the 'price' column, returning a new DataFrame with 'latitude', 
        'longitude', and 'price' columns.

        It uses the initilized DataFrame

        Returns:
        pd.DataFrame: A DataFrame with columns 'latitude', 'longitude', and 'price'.
                  Rows with invalid or missing location data are dropped.
        """
    
    
    
        LocPricedf = self.RentHousedf[["location", "price", "size"]]
        LocPricedf[['latitude', 'longitude']] = LocPricedf['location'].str.extract(r'\(([^,]+),\s*([^)]+)\)')
        LocPricedf.dropna(inplace=True)
        LocPricedf['latitude'] = pd.to_numeric(LocPricedf['latitude'], errors='coerce')
        LocPricedf['longitude'] = pd.to_numeric(LocPricedf['longitude'], errors='coerce')
        LocPricedf.drop('location', inplace=True, axis=1)
        #LocPricedf["price"] = LocPricedf["price"]/100000
        LocPricedf['price'] = LocPricedf['price'].astype(int)
        return LocPricedf