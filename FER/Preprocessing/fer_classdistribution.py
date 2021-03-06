import os
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

"""## Separating data"""

data_org = pd.read_csv("fer2013/fer2013.csv")
data_org.head()

data_org

data_org.emotion.unique()

data_org.groupby(['Usage']).count()

for i, data in data_org.groupby('Usage'):
    data.to_csv("{}.csv".format(i))

test_private = pd.read_csv("PrivateTest.csv")
test_private

test_public = pd.read_csv("PublicTest.csv")
test_public

train = pd.read_csv("Training.csv")
train

"""## Emotion Distribution"""

emotion_label = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

import seaborn as sns
#sns.set_theme(style="darkgrid")
ax1 = sns.countplot(x="emotion", data=train, palette= "Set3")
ax1.set_title("Training Data Emotion Distribution");
ax1.set_xticklabels(emotion_label.values())

ax2 = sns.countplot(x="emotion", data=test_public, palette="Set2")
ax2.set_title("Test Data Emotion Distribution");
ax2.set_xticklabels(emotion_label.values())

ax3 = sns.countplot(x="emotion", data=test_private, palette="Set1")
ax3.set_title("Validation Data Emotion Distribution");
ax3.set_xticklabels(emotion_label.values())

"""### Separating Training Data based on Emotions"""

emotion_split = train.groupby(['emotion']).count()
emotion_split

for j, dx in train.groupby('emotion'):
    dx.to_csv("{}.csv".format(j))

#sample
disgust = pd.read_csv("1.csv")
disgust.head()

"""### Separating Testing Data based on Emotions"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My Drive/facial_expression/test

for i, data in test_public.groupby('emotion'):
    data.to_csv("{}.csv".format(i))

#sample
happy = pd.read_csv("3.csv")
happy.head()

"""### Separating Validation data based on emotions"""

for i, data in test_private.groupby('emotion'):
    data.to_csv("{}.csv".format(i))

#sample
neutral = pd.read_csv("6.csv")
neutral.head()
