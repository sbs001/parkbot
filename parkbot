import sys
import json
 
with open('airgarage-data.json') as file:
   data = json.load(file)

args = sys.argv

if (len(args) < 4):
    print('Please, insert valid arguments')
elif (args[1] != 'airgarage-data.json'):
   print('File',args[1], 'not found. Please, try again')

elif (args[2] == 'locate'):
   results = []
   for slot in data:
      if (slot['address']['state'] == args[3]):
        results.append(slot['name'])
   print(', '.join(results))

elif (args[2] == 'find_price_hourly_lte'):
   results = []
   for slot in data:
      if (slot['price_hourly'] <= int(args[3])):
        results.append(slot['name'])
   print(', '.join(results))

elif (args[2] == 'find_price_hourly_gt'):
   results = []
   for slot in data:
      if (slot['price_hourly'] > int(args[3])):
        results.append(slot['name'])
   print(', '.join(results))