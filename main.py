import requests
from utils import (
    profit_calculator,
    get_request_json,
    ID_TO_NAME_DICT
)

ELEMENT_AMOUNT = 15 # Remove magic number
json_resp = get_request_json()
unordered_list = []

for item_id, item_dict in json_resp.items():
    result = profit_calculator(item_id, item_dict, ID_TO_NAME_DICT)
    unordered_list.append(result)

ordered_list = sorted(unordered_list, key=lambda item_dict: item_dict[1])

for item in ordered_list[0: ELEMENT_AMOUNT]:
    print(item)
