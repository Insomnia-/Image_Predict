import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
from classify import predict


st.title('''David Jiao'first Image Predict App 👁''')

uploaded_file = st.file_uploader("Choose an image to upload...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying... ")
    bar = st.progress(0)
    label = predict(uploaded_file)
    bar.progress(100)
    st.write('Here is the prediction result: %s (%.2f%%)' % (label[1], label[2]*100))