import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

URL = "https://1000mostcommonwords.com/1000-most-common-spanish-words/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table")
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)

df = pd.DataFrame(output_rows)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
df = df.drop(columns = 'Number')

df.to_csv('./data/spanish_vocab.csv')