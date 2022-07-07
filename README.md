# SEA-X - Detection and Analysis of Plastic Waste


### What we aim to do

Reduce the amount of plastic wastes in the ocean

### How are we doing that?

A platform that combines Drones and GIS technology, leveraging AI to identify and analyze plastic waste on water bodies

### How does it work?

Leveraging a cutomoised Yolov5 model with annotated images labelled with LabelImg, gathered data from a nearby river to collect data.
https://user-images.githubusercontent.com/54020973/177602282-13057edf-2b06-420c-b135-9e8589390aa0.mp4

### Website to test the app

It was built with power apps and deployed with Streamlit
https://seax.powerappsportals.com/

### Model Architecture

### AIM of research poster

To compare the results from a Yolov5 and Effi-UNet model by applying both to detection and analysis of plastic waste.

#### Benchmark results: 
Will be added soon

### YOLOv5 Approach

### UNet Approach

Tried to acheive the same results from Yolov5 by leveraging a UNet CNN architecture. This research uses the same dataset, preprocessing method but with a UNet model and a extra layer. The results are a displayed differently in that using semantic segmentation to show the mapped areas and a collective accuracy rather than individual predictions.

A similar poster was presented at Data Scientist Bootcamp 2019, but this one has been improved using a different approach, Efficent Unet. Here's the poster of the previous one.

![Screenshot 2022-07-07 121514](https://user-images.githubusercontent.com/54020973/177760978-fb89f73f-a15f-4e67-997b-d7450ddc8408.png)

Refernce:

https://openaccess.thecvf.com/content_CVPRW_2020/papers/w22/Baheti_Eff-UNet_A_Novel_Architecture_for_Semantic_Segmentation_in_Unstructured_Environment_CVPRW_2020_paper.pdf
