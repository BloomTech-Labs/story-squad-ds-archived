from sys import stdin, stdout
from json import loads, dumps
from decouple import config
import pandas as pd


def make_match(df):
    temp = {
        "match_1": {
            "team_1": ["user_1", "user_2"],
            "team_2": ["user_3", "user_4"]}
            }
    return dumps(temp)

def make_df(data_in):
    data = loads(data_in)
    df = pd.DataFrame(data).T
    return df

def main(data_in):
    df = make_df(data_in)
    matches = make_match(df)
    return matches



data_in = stdin.read()

output = main(data_in)

stdout.write(output)