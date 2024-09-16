
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.berkeleycitycollege.edu/searchable-summer-fall-2024-classes/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table')
if not table:
    print("Table not found on the page.")
else:

    rows = table.find_all('tr')
    column_indices = [0, 4, 10]
    data = []
    for row in rows:
        cells = row.find_all('td')

        # Extract data from the specified columns
        row_data = []
        for index in column_indices:
            if len(cells) > index:
                cell_data = cells[index].get_text(strip=True)
                row_data.append(cell_data)
            else:
                row_data.append('')  # Append empty if the column is missing
        data.append(row_data)

    df = pd.DataFrame(data, columns=['Class Name', 'Days', 'Times'])  # Adjust column names as needed
    df.to_csv('extracted_data.csv', index=False)

    print("Data extraction complete. Data saved to extracted_data.csv.")