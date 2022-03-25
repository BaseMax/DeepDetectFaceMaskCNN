import numpy as np
from keras.models import Sequential
from matplotlib import pyplot as plt
from keras.callbacks import ModelCheckpoint
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Activation, Flatten, Dropout

# Load numpy arrays
data = np.load('data.npy')
target = np.load('target.npy')

model = Sequential()

# The first CNN layer followed by Relu and MaxPooling layers
model.add(Conv2D(200, (3, 3), input_shape = data.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

# The second convolution layer followed by Relu and MaxPooling layers
model.add(Conv2D(100, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

# The Final layer with two outputs for two categories
model.add(Flatten())
model.add(Dropout(0.5)) # Flatten layer to stack the output convolutions from second convolution layer
model.add(Dense(50, activation = 'relu')) # Dense layer of 64 neurons
model.add(Dense(2, activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

train_data, test_data, train_target, test_target = train_test_split(data, target, test_size = 0.1)

checkpoint = ModelCheckpoint('model-{epoch:03d}.model', monitor = 'val_loss', verbose = 0, save_best_only = True, mode = 'auto')
history = model.fit(train_data, train_target, epochs = 20, callbacks = [checkpoint], validation_split = 0.2)

# show loss
plt.plot(history.history['loss'], 'r', label = 'training loss')
plt.plot(history.history['val_loss'], label = 'validation loss')
plt.xlabel('# epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

# show accuracy
plt.plot(history.history['accuracy'], 'r', label = 'training accuracy')
plt.plot(history.history['val_accuracy'], label = 'validation accuracy')
plt.xlabel('# epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

# evaluate
print(model.evaluate(test_data, test_target))
