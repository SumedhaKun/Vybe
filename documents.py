#!/usr/bin/env python
# coding: utf-8

# In[153]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

data = pd.read_csv("Spotify-2000.csv")

X = data["Energy"]
y = data["Loudness (dB)"]


plt.plot(y, X)
plt.show()

slope = y/X

data = pd.DataFrame(data)
data.insert(5, "Slope", slope)

#data.drop(columns = ["Artist", "Top Genre", "Year", "Beats Per Minute (BPM)", "Danceability", "Liveness", "Valence", "Acousticness", "Speechiness", "Popularity"])

#emotion = "";
#emot = data.insert(4, "emotion", "")
#for row in data[:5]:
    #print(data["Slope"])
    #if (data["Slope"].any() >= 0.5):
        #emotion = "happy"
    #else:
        #emotion = "sad"
    #p = array[row][""]
    #data[row]["emotion"]=[row]["emotion"][emotion]

em = data[:1].insert(4, "Emotion", "happy")
em1 = data[1:2].insert(4, "Emotion", "sad")

print (data)

X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)


# In[ ]:





# In[ ]:





# In[ ]:




