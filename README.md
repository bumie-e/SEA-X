# SEA-X - Detection and Analysis of Plastic Waste


### Future projection

Collaborate with local NGOs to reduce the amount of plastic wastes in water bodies.

### Proposed Solution

An analytical platform that recieves video feed from Drones to identify and analyze plastic waste on water bodies. 

### How does it work?

Leverages a pretrained Yolov5 model to predict plastics found on the water surface

https://user-images.githubusercontent.com/54020973/177602282-13057edf-2b06-420c-b135-9e8589390aa0.mp4

### Website to test the app

It was built with Power apps and Streamlit
https://seax.powerappsportals.com/

### Data Collection

For training: Dataset from Japan: https://zenodo.org/record/4552389

For testing: Gathered data from a nearby river using drones and plastic bottles.

### Data Annotation

LabelImg was used to annotate the images. 

### Yolov5 Model Architecture

![h-consists-of-three-parts-i-backbone](https://user-images.githubusercontent.com/54020973/205670159-361743ef-8bf5-4cc6-98aa-b4a36b019c91.jpg)

### AIM of research poster

![Olubunmi Akinremi PosterA](https://user-images.githubusercontent.com/54020973/205675724-3a8d2d85-87a6-4564-87e7-6ae954b78f40.png)


To propose an efficient way to detect and analyse different plastic types

The paper is divided into two parts
- Detection part
- Analysis part

### Paper Improvement Areas

- Allow for the use of video input


#### Evaluation Results: 
Will be added soon

## Earlier 
### UNet Approach

To acheive the same results from Yolov5 by leveraging a UNet CNN architecture. This research uses the same dataset, preprocessing method but with a UNet model and a extra layer. The results are a displayed differently in that using semantic segmentation to show the mapped areas and a collective accuracy rather than individual predictions.

This is an improvement of a similar poster I presented at Data Scientist Bootcamp 2021 using a different model approach, Efficent Unet. Here's the poster of the previous one.

![Screenshot 2022-07-07 121514](https://user-images.githubusercontent.com/54020973/177760978-fb89f73f-a15f-4e67-997b-d7450ddc8408.png)

Refernce:
https://github.com/ultralytics/yolov5/blob/master/detect.py
https://binginagesh.medium.com/small-object-detection-an-image-tiling-based-approach-bce572d890ca#03ca
https://openaccess.thecvf.com/content_CVPRW_2020/papers/w22/Baheti_Eff-UNet_A_Novel_Architecture_for_Semantic_Segmentation_in_Unstructured_Environment_CVPRW_2020_paper.pdf
