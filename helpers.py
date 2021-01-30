from pathlib import Path
from dotenv import load_dotenv
import os
import json


def get_host(prefix):
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    host = os.getenv(prefix + '_HOST')
    port = os.getenv(prefix + '_PORT')
    return host+":"+port


def get_db(prefix):
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    host = os.getenv(prefix + '_HOST')
    port = os.getenv(prefix + '_PORT')
    id = os.getenv(prefix + '_ID')
    password = os.getenv(prefix + '_PASSWORD')
    database = os.getenv(prefix + '_DATABASE')
    config = dict(host=host, port=port, id=id, password=password, database=database)
    return config


def get_vector(prefix):
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    host = os.getenv(prefix + '_HOST')
    port = os.getenv(prefix + '_PORT')
    pf = os.getenv(prefix + '_prefix')
    config = dict(host=host, port=port, prefix=pf)
    return config


def load_json(path):
    with open(path, "r") as file:
        body = json.load(file)
    return body
