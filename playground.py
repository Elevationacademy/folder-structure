import json

some_data = {"animal": "Lion", "job_description": "King"}
with open("new_file.json", "w") as f:
    json.dump(some_data, f)
