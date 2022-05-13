import gzip
import shutil
import sys

import requests

if sys.platform != "win32":
    path = "/opt/flask_app/"
    sys.path.append(path)
else:
    path = ""

def get_all_movies_series_ids(cur_date, type):
    url = f"https://files.tmdb.org/p/exports/{type}_ids_{cur_date}.json.gz"
    filename = url.split("/")[-1]
    with open(path + "json_stockage/" + filename, "wb") as f:
        r = requests.get(url)
        f.write(r.content)

    with gzip.open(filename, 'rb') as f_in:
        with open(f'{path}json_stockage/{type}.json', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)