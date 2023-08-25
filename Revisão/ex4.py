import sys

import requests

band = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

result = band.json()


for c in result["results"]:
    print(c["trackName"])
