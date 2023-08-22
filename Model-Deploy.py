import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import pandas 
from tensorflow import keras

center_path = 'Image_for_deploy/Center/'
donut_path = 'Image_for_deploy/Donut/'
edgeLoc_path = 'Image_for_deploy/Edge-Loc/'
edgeRing_path = 'Image_for_deploy/Edge-Ring/'
loc_path = 'Image_for_deploy/Loc/'
edgeLoc_path = 'Image_for_deploy/Edge-Loc/'
nearFull_path = 'Image_for_deploy/Near-full/'
random_path = 'Image_for_deploy/Random/'
scratch_path = 'Image_for_deploy/Scratch/'
none_path = 'Image_for_deploy/none/'

paths = [center_path,
  donut_path,
  edgeLoc_path,
  edgeRing_path,
  loc_path,
  nearFull_path,
  random_path,
  scratch_path,
  none_path]

failureTypes = ['Center',
  'Donut',
  'Edge-Loc',
  'Edge-Ring',
  'Loc',
  'Near-full',
  'Random',
  'Scratch',
  'none']

imagesDisplay = dict()
imagesDeploy = dict()

for i in range(len(failureTypes)):
  imagesDeploy[failureTypes[i]] = []
  imagesDisplay[failureTypes[i]] = []
  for j in range(10):
    image = tf.keras.utils.load_img(paths[i]+str(j)+'.png')
    imagesDeploy[failureTypes[i]].append(image)
    image = image.resize((100, 100))
    imagesDisplay[failureTypes[i]].append(image)
    
model_path = 'Models/model0_1'
model = keras.models.load_model(model_path)

if 'all_pr' not in st.session_state:
  st.session_state.all_pr = ''
  
if 'class_pr' not in st.session_state:
  st.session_state.class_pr = ''

st.set_page_config(layout = "wide")

def prediction(im):
  im = np.asarray(im)
  im = np.expand_dims(im, axis=0)
  all_pr = model.predict(im)
  class_pr = failureTypes[np.argmax(all_pr)]
  print_all_pr = pandas.DataFrame(all_pr, columns=failureTypes)
  st.session_state.all_pr = print_all_pr
  st.session_state.class_pr = class_pr

if __name__ == '__main__':
    st.title("WM-811K WaferMap")
    st.subheader("Semiconductor Wafermap Failure Detection and Recognition")

    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(to right, #0099CC, #66CCFF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subheader {
            font-size: 24px;
            text-align: center;
            margin-top: -20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
    "Welcome to the **WM-811K WaferMap** analysis platform. This tool employs a **Convolutional Neural Network (CNN)** to "
    "identify and classify defect types in semiconductor wafermaps.\n"
    "Wafermaps are essential in semiconductor manufacturing to detect flaws and imperfections in wafers. Our CNN model helps "
    "automate the process of recognizing different types of defects.\n\n"
    "The model is trained to detect 9 different failure types:\n"
    "**Center**, **Donut**, **Edge-Loc**, **Edge-Ring**, **Loc**, **Near-full**, **Random**, **Scratch**, and **None**.\n\n"
    "Each failure type corresponds to a specific pattern or anomaly that can occur on a semiconductor wafer.\n\n"
    "By selecting a failure type, you can explore images associated with that specific defect and see how the model's predictions "
    "align with human judgment. This interactive platform provides insights into the capabilities of the CNN model and its "
    "ability to assist in quality control within semiconductor production lines."
)


    st.write("##")
    
    # Create a centered container for the content
    content_container = st.container()

    with content_container:
        col1, col2 = st.columns([1, 5])

        with col1:
            st.subheader("Failure Types")
            selectedType = st.selectbox("", failureTypes)
            st.write("")

        col1, col2, col3, col4, col5 = st.columns(5)
        cols = [col1, col2, col3, col4, col5]

        buttons = []

        for i in range(len(cols)):
            with cols[i]:
                st.image(imagesDisplay[selectedType][i])
                buttons.append(st.button('Image '+str(i), on_click=prediction, args=(imagesDeploy[selectedType][i],)))
                st.write('##')
                st.image(imagesDisplay[selectedType][i+5])
                buttons.append(st.button('Image '+str(i+5), on_click=prediction, args=(imagesDeploy[selectedType][i+5],)))

        st.write('##')
        st.markdown("---")
        st.subheader("Probability of Failure Types")
        for i in range(len(buttons)):
            if buttons[i]:
                st.write(st.session_state.all_pr)

        st.subheader("Predicted Failure Type")
        for i in range(len(buttons)):
            if buttons[i]:
                st.write(st.session_state.class_pr)

    st.sidebar.markdown(
        """
        <style>
        .sidebar-header {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 15px;
            background: linear-gradient(to right, #0099CC, #66CCFF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.write("## Project Contributors", unsafe_allow_html=True)
    st.sidebar.write("Anish De, Sayan Dey, Kankana Basak, Bijit Sen")
