import json
import random
import sys

if sys.platform != "win32":
    path = "/opt/flask_app/"
    sys.path.append(path)
else:
    path = ""
from api.curl_json import curl_json
from db_interact.get_api_key import get_api_key
from db_interact.insert_list_item import insert_list_item
from prepare_data.purge_quote import purge_quote
from prepare_data.get_length import get_length


def arrange_data(item_fetched, type):
    if type == "movie":
        title = item_fetched["title"]
        date = item_fetched["release_date"]
        length = item_fetched["runtime"]
        summary = item_fetched["overview"]
        try:
            path_image = 'https://image.tmdb.org/t/p/w500/'+item_fetched["poster_path"]
        except:
            path_image = ""
    else:
        try:
            title = item_fetched["name"]
        except:
            title = None
        try:
            date = item_fetched["first_air_date"] + "---" + item_fetched["last_air_date"]
        except:
            date = None
        try:
            length = get_length(item_fetched["episode_run_time"])
        except:
            length = None
        summary = ""
        try:
            path_image = 'https://image.tmdb.org/t/p/w500/'+item_fetched["poster_path"]
        except:
            path_image = ""

    return [title, date, length, summary, path_image]


def prep_data_insertion(item_fetched, type):
    categories = ""

    for cat in item_fetched["genres"]:
        categories += cat["name"] + "/"
    categories = categories[:-1]
    data_prepared = arrange_data(item_fetched,type)
    dict_to_return = {"title": data_prepared[0],
                      "year": data_prepared[1],
                      "length": data_prepared[2],
                      "summary": data_prepared[3],
                      "category": categories,
                      "nb_likes": random.randint(1, 100),
                      "path_image" : data_prepared[4]
                      }
    return dict_to_return


def prep_data_to_insert(raw_data, id_explore):
    to_insert = [id_explore]
    for key in raw_data:
        to_insert.append(raw_data[key])

    to_insert = purge_quote(to_insert)
    return to_insert


def get_random(type):
    base_url = "https://api.themoviedb.org/3/"
    language = "language=fr-Fr"
    api_key = get_api_key()
    item_fetched = {}

    while len(item_fetched) < 4:
        id_explore = random.randint(2, 150000)
        item_fetched = curl_json(f"{base_url}{type}/{id_explore}?api_key={api_key}&{language}")

    dict_to_return = prep_data_insertion(item_fetched, type)

    insert_list_item(prep_data_to_insert(dict_to_return, id_explore), type)

    return json.dumps(dict_to_return)
