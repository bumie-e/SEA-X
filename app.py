import streamlit as st
import numpy as np
from PIL import Image
import os

from torch import classes
from inference import main
import matplotlib.pyplot as plt


weightpath = r'deploy/best.pt'
source = r'test/60.jpg'
source1 = r'test/57.jpg'
source2 = r'test/54.jpg'
source3 = r'test/50.jpg'

##########
##### Set up sidebar.
##########


## Title.
st.write('# Plastic Detection App')

with st.sidebar:
    a = st.selectbox('Sample Images', ['Sample Image 1', 'Sample Image 2', 'Sample Image 3', 'Sample Image 4'])
    if a == 'Sample Image 1':
        image = Image.open(source)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source)
        else: imag_url=None
    elif a == 'Sample Image 2':
        image = Image.open(source1)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source1)
        else: imag_url=None
    elif a == 'Sample Image 3':
        image = Image.open(source2)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source2)
        else: imag_url=None
    elif a == 'Sample Image 4':
        image = Image.open(source3)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source3)
        else: imag_url=None

def getImage():
    main(weightpath, source)





#arr = np.random.normal(1, 1, size=100)



if imag_url is not None:

    ## Subtitle.
    st.write('### Results')

    t1, t2, t3 = st.columns(3)
    c1, c2 = st.columns(2)


    img, time, objects_, accuracies = main(weightpath, imag_url)
    containers = 0
    nylon = 0
    st.write('Time taken: ', f'{round(time[1]/60,2)} secs')
    #st.write('Classes: ', objects_)
    #st.write('Accuracies: ', accuracies)

    with t1:
        st.metric(label="Plastics Bottle", value=len(objects_))
        st.write("Average Accuracy "+ f"{np.mean(accuracies):.2f}")
    with t2:
        st.metric(label="Plastics Containers", value=containers)
    with t3:
        st.metric(label="Nylon", value=nylon)

    print('uploaded files-------------------', img)

    with c1:
        img_data = imag_url.split('\\')
        print(img_data)
        image = Image.open(str(img)+'/'+img_data[-1])
        st.image(image)
    # with c1:

    #     for i in os.listdir(img):
    #         if i.endswith('.mp4'):
    #             video = open(str(img)+'/'+i, 'rb')
    #             st.video(video)
    #         else:
    #             image = Image.open(str(img)+'/'+i)
    #             st.image(image)

    with c2:
        fig, ax = plt.subplots()
        ax.hist(accuracies, edgecolor="white", linewidth=0.7)

        st.pyplot(fig)

else:
    st.markdown('### Choose a Sample Image or Add a file directory')
    imag_url = st.text_input('Add the File directory', None)

    if imag_url != 'None':
        ## Subtitle.
        st.write('### Results')

        t1, t2, t3 = st.columns(3)
        c1, c2 = st.columns(2)


        img, time, objects_, accuracies = main(weightpath, imag_url)
        containers = 0
        nylon = 0
        st.write('Time taken: ', f'{round(time[1]/60,2)} secs')
        #st.write('Classes: ', objects_)
        #st.write('Accuracies: ', accuracies)

        with t1:
            st.metric(label="Plastics Bottle", value=len(objects_))
            st.write("Average Accuracy "+ f"{np.mean(accuracies):.2f}")
        with t2:
            st.metric(label="Plastics Containers", value=containers)
        with t3:
            st.metric(label="Nylon", value=nylon)

        print('uploaded files-------------------', img)

        with c1:
            img_data = imag_url.split('\\')
            print(img_data)
            image = Image.open(str(img)+'/'+img_data[-1])
            st.image(image)

        with c2:
            fig, ax = plt.subplots()
            ax.hist(accuracies, edgecolor="white", linewidth=0.7)

            st.pyplot(fig)

# Function to make API request        

