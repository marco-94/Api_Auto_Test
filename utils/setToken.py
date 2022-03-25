import requests
from config.config import CONFIG_FILE
from ruamel import yaml
from utils import getYaml

data = getYaml.getyamldata()


def get_accessToken():
    headers = {"Content-Type": "application/json"}
    authorizeParams = {
        "scope": "openid",
        "response_type": "code",
        "client_id": "574483092603633664",
        "redirect_url": "https://localhost:8443/uac/",
        "state": "001",
        "auth_type": "BPassword"
    }
    authorizeResponse = requests.get(url=data["beta"] + data["authorize"], params=authorizeParams).json()
    code_key = authorizeResponse['data']['code_key']
    executeJson = {
        "c_name": "BPasswordLogin",
        "input_param": {
            "regionCode": "86",
            "username": data["username"],
            "password": data["password"]
        },
        "code_key": code_key
    }

    executeResponse = requests.post(data["beta"] + data["execute"], json=executeJson, headers=headers).json()
    code = executeResponse['data']['code']
    state = executeResponse['data']['state']
    userId = executeResponse['data']['userId']
    accessJson = {
        "client_id": 585014642717982720,
        "client_secret": "dcb3b27ffe1b47949198b2be37fa9f92",
        "code": code,
        "state": state,
        "userId": userId
    }
    accessTokenresponse = requests.post(data["beta"] + data["accessToken"], headers=headers, json=accessJson).json()
    accessToken = accessTokenresponse['data']['access_token']
    return accessToken


def up_yml(accessToken):
    with open(CONFIG_FILE, 'r', encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.Loader)
        # 修改yml文件中的参数
        content['authorization'] = accessToken
    with open(CONFIG_FILE, 'w', encoding="utf-8") as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)

# up_yml(get_accessToken())