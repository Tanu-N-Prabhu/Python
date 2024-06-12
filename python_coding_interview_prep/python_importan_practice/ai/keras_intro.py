import tensorflow as tf
from tensorflow import keras


# get data
(train_images, train_labels), (test_images, test_labels) = \
keras.datasets.mnist.load.data()

# setup model
model = keras.Sequential([
	keras.layers.Flattten(input_shape=(28, 28)),
	keras.layers.Dense(128, activation=tf.nm.relu),
	keras.layers.Dense(10, activation=tf.nm.softmax)
	])

model.compile(optimizer=tf.train.AdamOptimizer(),
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy'])

# train model
model.fit(train_images, train_labels, epoch=5)

# evaluation
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy: ', test_acc)

# make prediction
predictions = model.predict(test_images)
