# Import necessary libraries
import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split
from PIL import Image
from keras.preprocessing.image import img_to_array

IMAGE_WIDTH, IMAGE_HEIGHT, CHANNELS = 256, 256, 3
EPOCHS = 4  # You can adjust this

# Function to load images and labels
def load_images_and_labels(image_paths, label):
    images = []
    labels = []

    for img_path in image_paths:
        img = Image.open(img_path)
        img = img_to_array(img)
        images.append(img)
        labels.append(label)

    return np.array(images), np.array(labels)

# Load and preprocess dataset
# Path to the dog dataset
dog_image_path = 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\dogs'
random_image_path = 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\non-dogs'

# Load dog and non-dog images
dog_images, dog_labels = load_images_and_labels([os.path.join(dog_image_path, f) for f in os.listdir(dog_image_path) if f.endswith('.jpg')], 1)
non_dog_images, non_dog_labels = load_images_and_labels([os.path.join(random_image_path, f) for f in os.listdir(random_image_path) if f.endswith('.jpg')], 0)

# Combine and shuffle the dataset
all_images = np.concatenate((dog_images, non_dog_images), axis=0)
all_labels = np.concatenate((dog_labels, non_dog_labels), axis=0)
shuffle_indices = np.arange(all_images.shape[0])
np.random.shuffle(shuffle_indices)

all_images = all_images[shuffle_indices]
all_labels = all_labels[shuffle_indices]

# Normalize images
all_images = all_images / 255.0

# Split dataset into training and testing
train_data, test_data, train_labels, test_labels = train_test_split(all_images, all_labels, test_size=0.2, random_state=42)

# Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, CHANNELS)),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(train_data, train_labels, epochs=EPOCHS, validation_data=(test_data, test_labels))

# Evaluate model
model.evaluate(test_data, test_labels)

# Save model
model.save('C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\ML Models')