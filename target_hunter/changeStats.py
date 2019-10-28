## Python file that changes the value of a field for the current stats. 
## Used to keep track of which stats to display
import json
import sys

jsonFile = open('currentStats.json', 'r')
data = json.load(jsonFile)            # Cursor at end of JSON file
jsonFile.close()                      # Close the JSON file, this removing the cursor

# Which field to write into
field = sys.argv[1]

# Data to be entered
userIn = sys.argv[2]

# Represented in JSON as "FIELD": "userIn",
data[0][field] = userIn

jsonFile = open('currentStats.json', 'w+')
jsonFile.write(json.dumps(data))
jsonFile.close()