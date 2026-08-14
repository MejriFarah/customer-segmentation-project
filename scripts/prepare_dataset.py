import csv
import zipfile
from io import TextIOWrapper


with zipfile.ZipFile("Dataset.zip") as zip_file:
    with zip_file.open("marketing_campaign.csv") as source:
        with open("marketing_campaign_standardized.csv", "w", newline="", encoding="utf-8") as output:
            reader = csv.reader(TextIOWrapper(source, encoding="utf-8-sig"), delimiter="\t")
            writer = csv.writer(output)
            writer.writerows(reader)
