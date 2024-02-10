# Import required libraries

import streamlit as st
import PIL
from ultralytics import YOLO
from PIL import Image
import os
import openai
from decouple import config

# Setting page layout
st.set_page_config(
    page_title="Waste Analysis",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)

model_path = 'models/best.pt'
source = r'images/dji_export_1655128271450.jpg'
source1 = r'images/dji_export_1655128296982.jpg'
source2 = r'images/dji_export_1655128303764.jpg'
source3 = r'Version2/app/images/dji_export_1655129123132.jpg'

# Creating sidebar
with st.sidebar:
    st.header("Image/Video Config")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    # Model Options
    confidence = float(st.slider(
        "Select Model Confidence", 25, 100, 40)) / 100
    
    st.write('Select image samples')
    a = st.selectbox('Sample Images', ['Sample Image 1', 'Sample Image 2', 'Sample Image 3', 'Sample Image 4'])
    if a == 'Sample Image 1':
        image = Image.open(source)
        st.image(image)

        source_img = source
    elif a == 'Sample Image 2':
        image = Image.open(source1)
        st.image(image)
        
        source_img = source1
    elif a == 'Sample Image 3':
        image = Image.open(source2)
        st.image(image)
        
        source_img = source2
    elif a == 'Sample Image 4':
        image = Image.open(source3)
        st.image(image)
        source_img = source3

# Creating main page heading
st.title("Waste Analysis")

# Creating two columns on the main page
col1, col2 = st.columns(2)

# Adding image to the first column if image is uploaded
with col1:
    if source_img != None:
        # Opening the uploaded image
        uploaded_image = PIL.Image.open(source_img)
        # Adding the uploaded image to the page with a caption
        st.image(source_img,
                 caption="Uploaded Image",
                 use_column_width=True
                 )
    
        
try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(
        f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

def explainAI():
    
    openai.api_key = config("APIKEY")
    openai.api_base = config("ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
    openai.api_type = 'azure'
    openai.api_version = '2023-05-15' # this might change in the future

    deployment_name=config("DEPLOYMENTNAME") #This will correspond to the custom name you chose for your deployment when you deployed a model. 

    res = model(uploaded_image)
    #print(res[0].tojson())
    prompt = f"You have been handed over the results of a computer vision model built by the data science team and you have been asked to present the results to the board. Explain only 'name' and 'confidence'. Here is the data{res[0].tojson()}"
    
    
    # Send a completion call to generate an answer
    print('Sending a test completion job')
    response = openai.Completion.create(engine=deployment_name, prompt=prompt, max_tokens=70)
    text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
    st.write('AI Analysis of the Results')
    st.write(text)
    print(text)

if st.sidebar.button('Detect Objects'):
    res = model.predict(uploaded_image,
                        conf=confidence
                        )
    speed = res[0].speed
    res_plotted = res[0].plot()[:, :, ::-1]
    #print(res)
    with col2:
        st.image(res_plotted,
                 caption='Detected Image',
                 use_column_width=True
                 )
        explainAI()
        try:
            with st.expander("Detection Results"):
                for spe in speed:
                    st.write(spe, round(speed[spe], 2))
        except Exception as ex:
            st.write("No image is uploaded yet!")



