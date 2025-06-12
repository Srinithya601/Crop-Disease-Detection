import streamlit as st
from PIL import Image
from src.predict import predict_image
st.title(" CROP DISEASE DETECTION")
uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf Image", use_column_width=True)
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    label, confidence = predict_image("temp.jpg")
    st.write(f"### Prediction: {label} ({confidence*100:.2f}%)")