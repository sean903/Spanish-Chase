{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import csv\n",
    "import pandas as pd\n",
    "\n",
    "URL = \"https://1000mostcommonwords.com/1000-most-common-spanish-words/\"\n",
    "page = requests.get(URL)\n",
    "\n",
    "soup = BeautifulSoup(page.content, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "table = soup.find(\"table\")\n",
    "output_rows = []\n",
    "for table_row in table.findAll('tr'):\n",
    "    columns = table_row.findAll('td')\n",
    "    output_row = []\n",
    "    for column in columns:\n",
    "        output_row.append(column.text)\n",
    "    output_rows.append(output_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(output_rows)\n",
    "new_header = df.iloc[0] #grab the first row for the header\n",
    "df = df[1:] #take the data less the header row\n",
    "df.columns = new_header #set the header row as the df header\n",
    "df = df.drop(columns = 'Number')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('./data/spanish_vocab.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
