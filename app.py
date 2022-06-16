import streamlit as st
import numpy as np
from PIL import Image
import os
from inference import main


weightpath = 'deploy/best.pt'
source = r'test/dji_export_1655128326394.jpg'
##########
##### Set up sidebar.
##########


## Title.
st.write('# Plastic Detection App')

def getImage():
    main(weightpath, source)


st.write('### Upload File Directory')
imag_url = st.text_input('Add the Video directory', source)


## Subtitle.
st.write('### Results')
if imag_url is not None:
    
    img = main(weightpath, imag_url)

    print('uploaded files-------------------', img)
    for i in os.listdir(img):
        if i.endswith('.mp4'):
            video = open(str(img)+'/'+i, 'rb')
            st.video(video)
        else:
            image = Image.open(str(img)+'/'+i)
            st.image(image)




# Function to make API request        

