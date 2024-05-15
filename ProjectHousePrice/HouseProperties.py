import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('this_is_a_test.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all elements with the specified class
listing_cards = soup.find_all(class_='listing-card-content col-12 col-md-8 py-3 py-md-3 px-3 position-relative')

# Initialize lists to store the extracted data
fw_bold_fs_5 = []
fw_500_fs_7 = []
fw_bold_fs_7 = []

# Extract the text from the specific classes
for card in listing_cards:
    fw_bold_fs_5_text = card.find(class_='fw-bold fs-5 text-onyx me-3 font-family-secondary')
    fw_500_fs_7_text = card.find(class_='d-block fw-500 fs-7 text-onyx font-family-secondary')
    fw_bold_fs_7_text = card.find(class_='fs-7 text-onyx fw-bold')
    
    # Append the text to the respective lists
    fw_bold_fs_5.append(fw_bold_fs_5_text.get_text(strip=True) if fw_bold_fs_5_text else '')
    fw_500_fs_7.append(fw_500_fs_7_text.get_text(strip=True) if fw_500_fs_7_text else '')
    fw_bold_fs_7.append(fw_bold_fs_7_text.get_text(strip=True) if fw_bold_fs_7_text else '')

# Create a DataFrame
data = {
    'fw_bold_fs_5': fw_bold_fs_5,
    'fw_500_fs_7': fw_500_fs_7,
    'fw_bold_fs_7': fw_bold_fs_7
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

