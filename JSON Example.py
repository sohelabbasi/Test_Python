JSON_Data = {

    "FirstName" : "Syed",
    "LastName" : "Haq",
    "Gender" : "Male"
    }
print(JSON_Data["FirstName"])

import json
with open("datatest_file.json", "w+") as write_file:
    json.dump(JSON_Data, write_file)
print(JSON_Data["FirstName"])

