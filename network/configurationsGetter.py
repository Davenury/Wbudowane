import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = f'{ROOT_DIR}/configuration.json'


def get_configuration() -> dict:
    with open(CONFIG_FILE) as f:
        return json.load(f)

def get_mail() -> str:
    return get_configuration()["email"]


def update_configuration(data: dict):
    keys = get_configuration().keys()
    if data.keys() != keys:
        print("Error not all keys are added")
    else:
        with open(CONFIG_FILE) as f:
            json.dump(data, f)
