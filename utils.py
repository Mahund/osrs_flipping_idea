import json
import requests

ID_TO_NAME_DICT = json.load(open('id_to_name.json'))

def profit_calculator(item_id, item_dict, id_to_name_dict):
    item_profit = 0
    if item_dict['high'] and item_dict['low']:
        item_profit = item_dict['high'] - item_dict['low']
    return (id_to_name_dict[str(item_id)], item_profit, item_id)

def get_request_json():
    resp = requests.get('https://prices.runescape.wiki/osrs/latest')
    return resp.json()