from bs4 import BeautifulSoup
import pandas as pd

class DataExtractor():
    def __init__(self, HTMLFileName) -> None:
        self.HTMLFileName = HTMLFileName

    def getData(self, df:pd.DataFrame, pageNumber:int) -> pd.DataFrame:
        with open(self.HTMLFileName+f"{pageNumber}.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, "html.parser")

        data_listing_ids = soup.find_all(attrs={"data-listing-id": True})

        listing_ids = [tag["data-listing-id"] for tag in data_listing_ids]

        listing_cards = soup.find_all(class_="listing-card-content col-12 col-md-8 py-3 py-md-3 px-3 position-relative")


        values = []
        for card in listing_cards:
            fw_bold = card.find(class_="fw-bold fs-5 text-onyx me-3 font-family-secondary").text.strip()
            fs_7_1 = card.find(class_="d-block fw-500 fs-7 text-onyx font-family-secondary").text.strip()
            fs_7_2 = card.find(class_="fs-7 text-onyx fw-bold").text.strip()
            values.append({"fw_bold": fw_bold, "fs_7_1": fs_7_1, "fs_7_2": fs_7_2})


        new_df = pd.DataFrame(values)

        new_df["listing_id"] = listing_ids


        df = pd.concat([df, new_df], ignore_index=True)
        return df

