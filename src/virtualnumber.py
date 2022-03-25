import requests
import yaml
import time
from config.config import CONFIG_FILE
from utils.getToken import get_token, up_yml


authorization = up_yml(get_token())
f = open(CONFIG_FILE, "r")
data = yaml.load(f)
time.sleep(2)
headers = {
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "authorization": data['authorization']
}

r = requests.get("https://api-beta.yjyz.com/erp.customer.api/virtualnumber/list", params=data['virtualnumber'],
                 headers=headers)
print(r.text)
