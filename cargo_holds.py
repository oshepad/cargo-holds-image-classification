# https://www.youtube.com/watch?v=Q1NC3NbmVlc

import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np



# ignore warning when uploading
st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('../data/my_model2.hdf5')
    return model
model=load_model()
st.title('Cargo Holds')

file = st.file_uploader('Please upload your cargo hold', type=['jpg', 'png'])

def import_and_predict(image_data, model):
    size = (256, 256)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)

    return prediction

if file is None:
    st.text("Please upload an image file in jpg or png type.")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    class_names=['clean', 'dirty']
    string = "This cargo hold is most likely: " + class_names[np.argmax(predictions)]
    st.success(string)

# ngrok to host?

# !ngrok authtoken
# !nohup streamlit run cargo_holds.py
# from pyngrok import ngrok
# url = ngrok.connect(port=8501)
# url
# ! cat /content/nhup.out