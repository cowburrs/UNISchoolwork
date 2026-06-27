import json
import sys

from pyzotero import zotero

with open("pytero.json") as f:
    config = json.load(f)

zot = zotero.Zotero(config["user_id"], config["library_type"], sys.argv[1])

bib = zot.everything(zot.top(format="bibtex"))
bib = zot.everything(zot.collection_items(config["library_key"], format="bibtex"))

for c in zot.collections():
    print(c["data"]["name"], "->", c["key"])
