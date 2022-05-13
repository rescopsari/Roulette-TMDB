import json, sys

import requests
from requests.structures import CaseInsensitiveDict
from urllib3.exceptions import InsecureRequestWarning
if sys.platform != "win32":
    path = "/opt/flask_app/"
    sys.path.append(path)
    path += "api"
else:
    path = ".."


def curl_json(url):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    resp = requests.get(url, headers=headers, verify=False)

    try:
        xml_data = json.loads(resp.text)
        return xml_data

    except Exception as e:
        print(f"error : {e}")
