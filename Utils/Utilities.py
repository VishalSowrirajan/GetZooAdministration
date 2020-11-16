import json
import pandas as pd


def convert_to_df(file):
    try:
        data = json.loads(file)
        df = pd.json_normalize(data)
        return df
    except Exception as e:
        print('Exception due to: {}'.format(e))


def total_cost(food_expense, zookeeper_expense):
    return food_expense + zookeeper_expense
