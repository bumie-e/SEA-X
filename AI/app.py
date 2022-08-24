import streamlit as st
import numpy as np
from PIL import Image
import os

from torch import classes
from inference import main
import matplotlib.pyplot as plt


weightpath = r'AI/deploy/best.pt'
vidweightpath = r'AI/deploy/best(former).pt'
source = r'AI/test/60.jpg'
source1 = r'AI/test/219.jpg'
source2 = r'AI/test/221.jpg'
source3 = r'AI/test/220.jpg'

vidsource = r'AI/test/v1.mp4'
vidsource1 = r'AI/test/v2.mp4'
vidsource2 = r'AI/test/v3.mp4'
vidsource3 = r'AI/test/v4.mp4'
vidsource4 = r'AI/test/v5.mp4'

##########
##### Set up sidebar.
##########
### Add background image
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('AI/test/bg.jpg') 

## Title.
st.write('# Plastic Detection App')

with st.sidebar:
    a = st.selectbox('Sample Images', ['Sample Image 1', 'Sample Image 2', 'Sample Image 3', 'Sample Image 4'])
    if a == 'Sample Image 1':
        image = Image.open(source)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source, key=14)
        else: imag_url=None
    elif a == 'Sample Image 2':
        image = Image.open(source1)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source1, key=13)
        else: imag_url=None
    elif a == 'Sample Image 3':
        image = Image.open(source2)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source2, key=12)
        else: imag_url=None
    elif a == 'Sample Image 4':
        image = Image.open(source3)
        st.image(image)
        
        if st.button('Ok'):
            imag_url = st.text_input('Add the File directory', source3, key=11)
        else: imag_url=None

    #Video
    b = st.selectbox('Sample Videos', ['Sample Video 1', 'Sample Video 2', 'Sample Video 3', 'Sample Video 4', 'Sample Video 5'])
    if b == 'Sample Video 1':
        if st.button('Ok', key=1):
            vid_url = st.text_input('Add the File directory', vidsource, key=1)
        else: vid_url=None
    elif b == 'Sample Video 2':
        if st.button('Ok', key=2):
            vid_url = st.text_input('Add the File directory', vidsource1, key=100)
        else: vid_url=None
    elif b == 'Sample Video 3':
        if st.button('Ok', key=3):
            vid_url = st.text_input('Add the File directory', vidsource2, key=3)
        else: vid_url=None
    elif b == 'Sample Video 4':
        if st.button('Ok', key=4):
            vid_url = st.text_input('Add the File directory', vidsource3, key=10)
        else: vid_url=None
    elif b == 'Sample Video 5':
        if st.button('Ok', key=5):
            vid_url = st.text_input('Add the File directory', vidsource4, key=5)
        else: vid_url=None


def getImage():
    main(weightpath, source)


if imag_url is not None:

    ## Subtitle.
    st.write('### Results')

    t1, t2, t3 = st.columns(3)

    img, time, objects_, accuracies = main(weightpath, imag_url)
    containers = 0
    nylon = 0
    st.write('Time taken: ', f'{round(time[1]/60,2)} secs')
    classes = {"plastic_bottle":0, "plastic_container":0, "nylon":0}
    classes["plastic_bottle"] = objects_.count("plastic_bottle")
    classes["plastic_container"] = objects_.count("plastic_container")
    classes["nylon"] = objects_.count("nylon")

    with t1:
        st.metric(label="Plastics Bottle", value=objects_.count("plastic_bottle"))
        st.write("Average Accuracy "+ f"{np.mean(accuracies):.2f}")
    with t2:
        st.metric(label="Plastics Containers", value=objects_.count("plastic_container"))
    with t3:
        st.metric(label="Nylon", value=objects_.count("nylon"))

    print('uploaded files-------------------', img)

    img_data = imag_url.split('/')
    print(img_data)
    image = Image.open(str(img)+'/'+img_data[-1])
    st.image(image)

    names = list(classes.keys())
    values = list(classes.values())

    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Accuracy vs Quantity')
    ax1.hist(accuracies, edgecolor="white", linewidth=0.7)
    ax2.bar(range(len(classes)), values, tick_label=names)
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
        classes = {"plastic_bottle":0, "plastic_container":0, "nylon":0}
        classes["plastic_bottle"] = objects_.count("plastic_bottle")
        classes["plastic_container"] = objects_.count("plastic_container")
        classes["nylon"] = objects_.count("nylon")

        with t1:
            st.metric(label="Plastics Bottle", value=objects_.count("plastic_bottle"))
            st.write("Average Accuracy "+ f"{np.mean(accuracies):.2f}")
        with t2:
            st.metric(label="Plastics Containers", value=objects_.count("plastic_container"))
        with t3:
            st.metric(label="Nylon", value=objects_.count("nylon"))

        print('uploaded files-------------------', img)

        img_data = imag_url.split('/')
        print(img_data)
        image = Image.open(str(img)+'/'+img_data[-1])
        st.image(image)

        names = list(classes.keys())
        values = list(classes.values())

        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle('Accuracy vs Quantity')
        ax1.hist(accuracies, edgecolor="white", linewidth=0.7)
        ax2.bar(range(len(classes)), values, tick_label=names)
        st.pyplot(fig)

# Display Video Output

if vid_url is not None:
    ## Subtitle.
    st.write('### Results')

    vid, time, objects_, accuracies = main(vidweightpath, vid_url)
    containers = 0
    nylon = 0
    
    st.write("Average Accuracy "+ f"{np.mean(accuracies):.2f}")
    st.write('Time taken: ', f'{round(time[1]/60,2)} secs')
    print('uploaded files-------------------', vid)

    img_data = vid_url.split('/')
    print(img_data, vid)

    video_file = open(str(vid)+'/'+img_data[-1], 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

else:
    st.markdown('### Choose a Sample Video or Add a file directory')
    vid_url = st.text_input('Add the File directory', None, key=7)

    if vid_url != 'None':
        ## Subtitle.
        st.write('### Results')

        vid, time, objects_, accuracies = main(vidweightpath, vid_url)
        containers = 0
        nylon = 0

        st.write("Average Accuracy "+ f"{np.mean(accuracies):.2f}")
        st.write('Time taken: ', f'{round(time[1]/60,2)} secs')
        print('uploaded files-------------------', vid)

        img_data = vid_url.split('/')
        print(img_data)

        video_file = open(str(vid)+'/'+img_data[-1], 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)   

