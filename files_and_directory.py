# import os
# #Get Current Working Directory





import sys

#Get the command-line arguments
print(f"Command-line arguments: {sys.argv}")

#Print the version of Python being used
print(f"Python version: {sys.version}")

sys.exit()


import json
#Convert a python dictionary to a JSON string
data = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(data)
print(f"JSON data: {json_Data}")

#Parse a JSON string into a Python dictionary
parsed_Data = json.loads(json_data)
print(f"Parsed data: {parsed_Data}")

#Write JSON data to a file
with open("data.json", "w") as file:
    json.dump(data,file)