import csv
import re
from datetime import datetime
import os

csvFilename = 'weblog.csv'
currentDir = os.getcwd()
url = currentDir +"\\" + csvFilename
#part1 and part2
with open(url,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_of_hits = list(csv_reader)
    #print(list_of_hits)
#part3
JPG_Count = 0
PNG_Count = 0
GIF_Count = 0
Other = 0
i = 0
while i < len(list_of_hits):
    if bool(re.search("JPG",list_of_hits[i][0].upper())) == True:
        JPG_Count += 1
    elif bool(re.search("PNG",list_of_hits[i][0].upper())) == True:
        PNG_Count += 1
    elif bool(re.search("GIF",list_of_hits[i][0].upper())) == True:
        GIF_Count += 1
    else:
        Other += 1
    i = i+1
    Total = JPG_Count + PNG_Count + GIF_Count 
print("Image requests account for {0}% of all requests ".format((Total/len(list_of_hits))*100))

#Part 4
Browser_Dict = {'Safari':0,'Chrome':0,'IE':0,'Firefox':0}
Safari_Count = 0
Chrome_Count = 0
Firefox_Count = 0
Other = 0
i = 0
while i < len(list_of_hits):
    if bool(re.search("safari",list_of_hits[i][2].lower())) == True:
        Safari_Count += 1
    elif bool(re.search("chrome",list_of_hits[i][2].lower())) == True:
        Chrome_Count += 1
    elif bool(re.search("firefox",list_of_hits[i][2].lower())) == True:
        Firefox_Count += 1
    else:
        Other += 1
    i = i+1
print("Hits from Safari are: ",Safari_Count)
print("Hits from Chrome are: ",Chrome_Count)
print("Hits from Firefox are: ",Firefox_Count)
print("Hits from Internet Explorer are: ",Other)
Browser_Dict['Safari'] = Safari_Count
Browser_Dict['Chrome'] = Chrome_Count 
Browser_Dict['Firefox'] = Firefox_Count 
Browser_Dict['IE'] = Other 
#print(Browser_Dict)
max_key = max(Browser_Dict, key=Browser_Dict.get)
print("Browser with most hits is : ",max_key)

#Bonus

i = 0
count = 0
hour_track = dict()
for i in range (0,24):
    hour_track[i] = 0
while i < len(list_of_hits):
    dt_object = datetime.strptime(list_of_hits[i][1], "%m/%d/%Y %H:%M")
    for k,v in hour_track.items():
        if (k == dt_object.hour):
            hour_track[k] += 1
    i = i+1

for k,v in hour_track.items():
    print("Hour {0} has {1} hits".format(k,v))