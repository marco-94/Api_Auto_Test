import yaml
from config.config import CONFIG_FILE

def getyamldata():
    f = open(CONFIG_FILE, "r", encoding='utf-8')
    data = yaml.load(f.read(), Loader=yaml.Loader)
    return data
