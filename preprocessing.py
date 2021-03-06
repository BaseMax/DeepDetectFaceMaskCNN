import cv2, os
import numpy as np
from keras.utils import np_utils

img_size = 100
data_path = 'dataset'

data = []
target = []
categories = os.listdir(data_path)
labels = [i for i in range(len(categories))]
label_dict = dict(zip(categories,labels))

print(label_dict)
print(categories)
print(labels)

for category in categories:
    folder_path = os.path.join(data_path, category)
    names = os.listdir(folder_path)

    for name in names:
        img_path = os.path.join(folder_path, name)
        img = cv2.imread(img_path)
        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)           
            resized = cv2.resize(gray, (img_size, img_size))
            data.append(resized)
            target.append(label_dict[category])
        except Exception as e:
            print('Exception Error:', e)

data = np.array(data) / 255.0
data = np.reshape(data, (data.shape[0], img_size, img_size, 1))
target = np.array(target)

new_target = np_utils.to_categorical(target)

np.save('data', data)
np.save('target', new_target)
