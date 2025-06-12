import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
class_names = []
model = load_model("models/model.h5")
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.
    preds = model.predict(img_array)
    class_idx = np.argmax(preds)
    return class_names[class_idx], preds[0][class_idx]