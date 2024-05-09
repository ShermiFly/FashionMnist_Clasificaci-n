import streamlit as st
import requests

st.title('Clasificador de Imágenes con Streamlit y FastAPI')

uploaded_file = st.file_uploader("Carga una imagen", type=["jpg", "png"])
if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/predict/", files=files)
    prediction = response.json()
    st.image(uploaded_file, caption='Imagen Cargada', use_column_width=True)
    st.write(f"Predicción: {prediction['result']}")
