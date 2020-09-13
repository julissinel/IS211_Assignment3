#!/usr/bin/env python
# coding: utf-8

# In[44]:


import csv


# In[45]:


with open('weblog.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_of_hits = list(csv_reader)
    print(list_of_hits)


# In[118]:


import re

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
print(JPG_Count)
print(PNG_Count)
print(GIF_Count)
print(Other)


# In[121]:


import re

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
print(Safari_Count)
print(Chrome_Count)
print(Firefox_Count)
print(Other)


# In[191]:


from datetime import datetime
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
print(hour_track)


# In[ ]:




