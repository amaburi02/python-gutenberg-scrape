import csv
import os
import requests
from bs4 import BeautifulSoup

def search_books(search_term, csvfile = "pg_catalog.csv"):
    with open(csvfile, encoding="utf8") as csvfile:
        results = []
        pgreader = csv.DictReader(csvfile)
        for row in pgreader:
            title = row['Title']
            if search_term.lower() in title.lower():
                results.append({
                    "id": row["Text#"],
                    "title": row["Title"],
                    "author": row["Authors"]
                })
                if len(results) >= 10:
                    break

    if not results:
        print("Not found")
    return results

def main():
    search_term = input("Enter book title: ")
    results = search_books(search_term)
    for x in results:
        print(x)
    id = input("Enter id of desired book: ")
    url = "https://www.gutenberg.org/cache/epub/" + id + "/pg" + id + ".txt"
    print(url)

if __name__ == "__main__":
    main()