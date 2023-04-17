import requests
from bs4 import BeautifulSoup
import pandas as pd

# Defining the lists to store the value of each feature
title = []  # List to store the name of the product
description = []  # List to store price of the product

for i in range(1, 10):
    url = f"https://www.flipkart.com/boat-rockerz-255-pro-258-asap-charge-upto-40-hours-playback-bluetooth-headset/product-reviews/itm9d3a2c5e5356a?pid=ACCFZ95M5JTZQH3F&lid=LSTACCFZ95M5JTZQH3FM4IG6H&sortOrder=MOST_HELPFUL&certifiedBuyer=false&aid=overall&page={i}"

    # Make request to url
    response = requests.get(url)
    response.content

    # Parse the HTML response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting all the features together
    for data in soup.findAll('div', class_='_1AtVbE col-12-12'):

        names = data.find('p', attrs={'class': '_2-N8zT'})
        if names is not None:
            title.append(names.text)  # Add product name to list

        price = data.find('div', attrs={'class': 't-ZTKy'})
        if names is not None:
            description.append(price.text)  # Add price to list

# Storing the data into the structured format in the Data Frame
df = pd.DataFrame({'Review_title': title, 'Review': description})
df.head(10)

# Create a dataframe from the scraped data
df = pd.DataFrame(df)

# Save the dataframe to an Excel file
print(title)
df.to_csv("Flipkart_Scrapped_data1.csv", index=False)