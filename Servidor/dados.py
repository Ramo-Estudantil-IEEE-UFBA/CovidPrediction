import pandas as pd
import io
import requests

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'


def todos():
    s = requests.get(url).content
    c = pd.read_csv(io.StringIO(s.decode('utf-8')))
    return c