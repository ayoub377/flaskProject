import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf


def getPrediction(filename):

    model = tf.keras.models.load_model \
        ("./static/models/best_model.h5")
    img = load_img('./static/uploads/' + filename, target_size=(150, 150))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, axis=0)
    answer = model.predict(img)
    probability = model.predict(img)
    probability_results = 0

    if answer > 0.5:
        answer = "Recycle"
        probability_results = probability[0][0]
    else:
        answer = "Organic"
        probability_results = probability[0][0]

    answer = str(answer)
    probability_results = str(probability_results)

    values = [answer, probability_results, filename]
    return values[0], values[1], values[2]
