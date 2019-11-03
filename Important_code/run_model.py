import cv2
import tensorflow as tf

CATEGORIES = ["Fire", "No_Fire"]


def prepare(filepath):
    IMG_SIZE = 70  # 50 in txt-based
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)


model = tf.keras.models.load_model("CNN.model")

img = 'ocean.jpg'

f = open("output.txt", "w")
f.write("The file \"" + img + "\" outputs:\n")

prediction = model.predict([prepare(img)])
# print(prediction)  # will be a list in a list.
if(CATEGORIES[int(prediction[0][0])] == 0):
	f.write("This is a fire. RUN!")
else:
	f.write("No fire, ya good!")
