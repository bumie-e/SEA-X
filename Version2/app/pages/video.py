import cv2
import streamlit as st
from ultralytics import YOLO
import tempfile

# Replace the relative path to your weight file
#model_path = '../runs/detect/train4/weights/best.pt'
model_path = 'models/best.pt'
video_path = "images/dji_export_1655129117122.mp4"

# Setting page layout
st.set_page_config(
    page_title="Waste Analysis",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)

# Creating sidebar
with st.sidebar:
    st.header("Image/Video Config")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting videos
    f = st.file_uploader("Upload file", type=["mp4"])


    # Model Options
    confidence = float(st.slider(
        "Select Model Confidence", 25, 100, 40)) / 100
    
    #Video
    b = st.selectbox('Sample Videos', ['Sample Video 1'])
    if b == 'Sample Video 1':
        f = video_path

# Creating main page heading
st.title("Waste Analysis")

try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(
        f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)
# st.write("Model loaded successfully!")

if f is not None:
    #with open(str(source_vid), 'rb') as video_file:
    # video_bytes = source_vid.read()
    # if video_bytes:
    #     st.video(video_bytes)
    if 'images/' in f:
        filename = f
    else:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(f.read())
        filename = tfile.name

    if st.sidebar.button('Detect Objects'):
        vid_cap = cv2.VideoCapture(filename)
        st_frame = st.empty()
        while (vid_cap.isOpened()):
            success, image = vid_cap.read()
            if success:
                image = cv2.resize(image, (720, int(720*(9/16))))
                res = model.predict(image, conf=confidence)
                result_tensor = res[0].boxes
                res_plotted = res[0].plot()
                st_frame.image(res_plotted,
                               caption='Detected Video',
                               channels="BGR",
                               use_column_width=True
                               )
            else:
                vid_cap.release()
                break