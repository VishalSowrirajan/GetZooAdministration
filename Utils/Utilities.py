import json
import pandas as pd


def convert_to_df(file):
    data = json.loads(file)
    df = pd.json_normalize(data)
    return df


def total_cost(food_expense, zookeeper_expense):
    return food_expense + zookeeper_expense
