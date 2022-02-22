
from bs4 import BeautifulSoup
import requests
import csv
import datetime

# Date-related variables
tday=datetime.date.today()
tday=tday.strftime("%Y%m%d")
# Target website
url="https://x-rates.com/table/?from=EUR&amount=1"
# CSV file
xrate_file=f"xrates_{tday}.csv"
# Fetch website content. Exit script if error occurs
try:
    resp=requests.get(url).text
except Exception as e:
    exit()
# Create soup
src=BeautifulSoup(resp, "lxml")
# Find table of interest
xrate_table=src.find("table", class_="tablesorter ratesTable").findChild("tbody")
# Open CSV file in write mode
with open(xrate_file, "w") as csv_file:
    pen=csv.writer(csv_file)
    # Write header to CSV file
    pen.writerow(["currency (acronym)", "exchange rate (1 EUR)"])
    # Find entries in targeted table
    entries=xrate_table.find_all("tr")
    for entry in entries:
        currency=entry.td.text
        acronym=entry.a["href"][-3:]
        xrate=entry.find("td", class_="rtRates").text
        # Write fields to CSV file
        pen.writerow([f"{currency} ({acronym})", xrate])
        # Print fields to STDOUT
        print(f"{currency} ({acronym}): {xrate}")
