# AI-Based Crop Disease Detection

#  Crop Disease Detection Using Deep Learning

A deep learning-based image classification system to detect crop diseases through leaf images. The project leverages CNN and pretrained models to enable accurate diagnosis of 38 disease classes across 15 crop types. Deployed as a Flask-based web application on **Heroku**.

---

🔗 Table of Contents

1. Project Title 
2. Problem Statement  
3. Project Description  
4. Assumptions  
5. Technologies and Tools Used 
6. Advantages 
7. Future Scope  
8. Conclusion  
9. Dataset

---

## Project Title

**Crop Disease Detection through Leaf Image Classification**

In agriculture, leaf diseases pose a serious threat to crop yield and quality. Early and accurate identification can help mitigate losses. This project introduces an automated image classification model to identify diseases in specific crops using deep learning.

---

##  Problem Statement

Diseases on crop leaves can drastically affect productivity, leading to economic setbacks, especially in agriculture-driven countries. Manual detection is time-consuming, inconsistent, and requires expertise. This project aims to automate disease detection to:

- Aid farmers with instant diagnosis.
- Reduce crop loss due to delayed identification.
- Enhance precision agriculture practices.

---

##  Project Description

This deep learning model classifies leaf images into disease categories using a **Convolutional Neural Network (CNN)**, enhanced with **pretrained AlexNet weights** for efficient and accurate feature extraction.

### Key Steps:

- **Image Acquisition**  
  Leaf images are captured in real time with a white background for improved contrast and segmentation.

- **Image Preprocessing**  
  Images are resized and normalized using interpolation and batch normalization.

- **Feature Extraction**  
  CNN layers automatically extract features from the images, reducing dimensionality using max pooling and dropout.

- **Model Training**  
  Using Keras and TensorFlow, pretrained layers are frozen while custom layers are trained. Hyperparameters are tuned for performance.

- **Image Classification**  
  Based on patterns like color, density, and texture, CNN classifies the image into one of the 38 disease categories.

- **Web App with Flask**  
  A simple web interface is created using Flask (with HTML/CSS/JS) to allow users to upload images and receive predictions.

- **Deployment on Heroku**  
  The app is deployed using **Heroku**, with model files stored via Git LFS due to large file size (~124MB). Continuous integration is configured for seamless updates.

---

🔗  Assumptions

- The model currently supports **15 crops** and **38 diseases** (specific classes trained).
- It only classifies **predefined crops and disease types**.

*Example (not exhaustive):*

| Crop | Disease Examples |
|------|------------------|
| Apple | Apple Scab, Black Rot |
| Corn | Cercospora Leaf Spot, Common Rust |
| Grape | Black Rot, Leaf Blight |
| ...  | ... |

> For complete class list, see the dataset file or model configuration.

---

🔗  Technologies and Tools Used

| Tool/Library       | Purpose |
|--------------------|---------|
| **Keras**          | High-level deep learning API |
| **TensorFlow**     | Backend engine for Keras |
| **Jupyter Notebook** | Development environment |
| **Google Colab**   | Training with free GPU support |
| **Kaggle**         | Dataset hosting and experiments |
| **Python**         | Primary programming language |
| **Flask**          | Web framework for app |
| **HTML/CSS/JS**    | Frontend for the web app |
| **GitHub**         | Code hosting and version control |
| **Git LFS**        | For large file storage on GitHub |
| **Heroku CLI**     | App deployment on Heroku server |

---

🔗  Advantages

-  **Fast** and **automated diagnosis** of crop diseases
-  Reduces dependency on human expertise
-  Boosts **precision agriculture** practices
-  Global accessibility via web application

---

🔗  Future Scope

- Add **treatment suggestions** for detected diseases.
- Include **more crop types and diseases**.
- Introduce **local language support** for better farmer usability.
- Mobile version with **offline capabilities**.

---

🔗  Conclusion

In conclusion, this crop disease detection project demonstrates the effective application of deep learning techniques, particularly Convolutional Neural Networks (CNNs), in solving real-world agricultural problems.This deep learning-based system simplifies the crop disease detection process, providing farmers and researchers with a one-click solution to identify diseases and take preventive actions promptly. While currently limited to a fixed number of crops, it lays a strong foundation for scalable precision agriculture tools.

---

🔗  Dataset

* Dataset Link-> https://www.kaggle.com/datasets/emmarex/plantdisease

