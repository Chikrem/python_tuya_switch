import json

file_name = "log.txt"
file = open(file_name, "r")
data = []
order = ["SSID", "RSSI", "type"]

for line in file.readlines():
    details = line.split("|")
    details = [x.strip() for x in details]
    if len(details) >= 3:
        structure = {key: value for key, value in zip(order, details)}
        data.append(structure)


with open("output.json", "w") as output_file:
    json.dump(data, output_file, indent=3)

with open("output.json", "r") as json_file:
    data = json.load(json_file)

rssi_data = {"RSSI": []}

for entry in data:
    rssi = entry.get("RSSI")
    if rssi is not None and isinstance(rssi, (int, float,str)):
        rssi_data["RSSI"].append({"RSSI": rssi})

with open("rssi_values.json", "w") as rssi_file:
    rssi_file.write(json.dumps(rssi_data, indent=3))