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

def get_download_url(id):
    url = f"https://www.gutenberg.org/cache/epub/{id}"

    #html
    html_url = f"{url}/pg{id}.html"
    response = requests.head(html_url)
    if response.status_code == 200:
        print("HTML url works")
        return html_url
    #txt
    txt_url = f"{url}/pg{id}.txt"
    response = requests.head(txt_url)
    if response.status_code == 200:
        print("Txt URL works")
        return txt_url

def main():
    search_term = input("Enter book title: ")
    results = search_books(search_term)
    for x in results:
        print(x)
    id = input("Enter id of desired book: ")
    url = get_download_url(id)
    print(url)
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    print(soup.get_text())

if __name__ == "__main__":
    main()