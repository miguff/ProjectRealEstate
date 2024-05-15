import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('this_is_a_test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with the class 'listing-card-content col-12 col-md-8 py-3 py-md-3 px-3 position-relative'
listing_cards = soup.find_all(class_='listing-card-content col-12 col-md-8 py-3 py-md-3 px-3 position-relative')

# Prepare lists to store the extracted data
fw_bold_text = []
fw_500_text = []

# Loop through each listing card
for card in listing_cards:
    # Extract data with class 'fw-bold fs-5 text-onyx me-3 font-family-secondary'
    bold_element = card.find(class_='fw-bold fs-5 text-onyx me-3 font-family-secondary')
    if bold_element:
        fw_bold_text.append(bold_element.get_text(strip=True))
    else:
        fw_bold_text.append(None)

    # Extract data with class 'd-block fw-500 fs-7 text-onyx font-family-secondary'
    fw_500_element = card.find(class_='d-block fw-500 fs-7 text-onyx font-family-secondary')
    if fw_500_element:
        fw_500_text.append(fw_500_element.get_text(strip=True))
    else:
        fw_500_text.append(None)

# Create a DataFrame
data = {
    'fw_bold_text': fw_bold_text,
    'fw_500_text': fw_500_text
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
