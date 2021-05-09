import requests
# Import required libraries

# Get the names of cities (abbreviation only the first three letters must be entered) for example: London, lon.
nameCity = input("Please Enter name city for weather check: [teh]ran ::> ")
URLForFindCity = f"https://www.metaweather.com/api/location/search/?query={nameCity}"
'''
URL required to send requests to API service provider "www.metaweather.com"
Note: This request is in the source code. And in the continuation of the program, 
to send the ID of each city and get information, it will definitely send more requests
'''
response = requests.get(URLForFindCity)
data = response.text
convert = str(data)
# This part of the program becomes very simple if we use "regex" :)
# Remove annoying characters from the list
dataWithout = convert.replace("[{" , '')
newData = dataWithout.replace("}]",'')
var = newData.replace("}", '')
var2 = var.replace("{", '')
# Use the replace method
# As you know the properties of strings, they are immutable.
# Convert string to list by split method
heng = var2.split(',')
IDAndProcContDict = dict()
# Convert data to a dictionary for easy access to arguments
for init in heng:
    # Each content becomes a new temporary list to build the dictionary
    splitWith = init.split(":")
    if len(splitWith) == 1:
        continue
    else:
        IDAndProcContDict[splitWith[0]] = splitWith[1]

# woeid ID
# Where On Earth ID
try:
    Woeid = int(IDAndProcContDict['"woeid"'])
except:
    print("city Not Found")

#Send a request and receive Weather information about this city
URLWeather = f"https://www.metaweather.com/api/location/{Woeid}"
responseFrom = requests.get(URLWeather)
responseData = str(responseFrom.text)

#Converting Response to Accessible Data Tip is easier with Json :)
dataweather = responseData.split(",")
dataTemp = dict()
for i in range(0 , len(dataweather)):
    splity = dataweather[i].split(":")
    if len(splity) <= 1:
        continue
    dataTemp[splity[0]] = splity[1]

# output Weather Data
y = dataTemp['"min_temp"']
s = dataTemp['"wind_speed"']
dataFinal = f"Minimum Temperatur : {y} C - wind speed : {s} KNOT"
print(dataFinal)