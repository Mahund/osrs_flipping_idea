import json

file = open('name_to_id.json')
data = json.load(file)
file.close()

new_dict = {}
for name, id_ in data.items():
    new_dict[str(id_)] = name

# with open('id_to_name.json', 'w') as fp:
#     json.dump(new_dict, fp)

outfile = open('id_to_name.json', "w")
outfile.write(json.dumps(new_dict, indent=4, sort_keys=True))
outfile.close()