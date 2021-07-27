import sys
import json
 
with open('airgarage-data.json') as file:
   data = json.load(file)

args = sys.argv

if (len(args) == 1):
    print('Please, insert valid arguments')
elif (args[1] != 'airgarage-data.json'):
   print('File',args[1], 'not found. Please, try again')
    