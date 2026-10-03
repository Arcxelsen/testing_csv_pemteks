import os
import pandas as pd
from bs4 import BeautifulSoup
from curl_cffi import requests

SAVE_DIR = "Any/FIX"
os.makedirs(SAVE_DIR, exist_ok=True)

url = "https://growtopia.fandom.com/wiki/Growtopia_Wiki"

resp = requests.get(url, impersonate="chrome")
print("Status Code:", resp.status_code)

if resp.status_code == 200: 
    soup = BeautifulSoup(resp.text, "html.parser")
    items_data = []

    for a_tag in soup.find_all("a"):
        title = a_tag.text.strip()
        href = a_tag.get("href", "")

        if title and href.startswith("/wiki/"):
            link = "https://growtopia.fandom.com" + href
            items_data.append({"Item_Name": title, "Wiki_Link": link})

    if items_data:
        df_wiki = pd.DataFrame(items_data).drop_duplicates()
        file_out = os.path.join(SAVE_DIR, "gt_wiki_TP.csv")
        df_wiki.to_csv(file_out, index=False)
        print(
            f"{len(df_wiki)} data Wiki disimpan ke '{file_out}'"
        )
else:
    print("gagal tembus.")

