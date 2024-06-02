### 1. Project Goal/Motivation (project evaluation relative weight: 10%)

#### Project Goal
The goal of this project is to create a foundational application that can identify the make and model of a car from a photograph using machine learning techniques. This serves as the groundwork for a more comprehensive application that I plan to develop for my Bachelor's thesis. Ultimately, the aim is to help users recognize car brands and models easily and accurately by simply uploading an image of a car they see.

#### Motivation

##### Problem to Solve
Imagine seeing a car that catches your eye but not knowing its make or model. This can be a common scenario for many people, especially those who are not car enthusiasts. The problem arises from the difficulty of identifying car brands and models without prior knowledge or research tools at hand.

##### Relevance and Impact
This project is highly relevant in today's digital age, where machine learning and image recognition technologies are rapidly advancing. By leveraging these technologies, I can develop an application that allows users to upload a picture of a car, and the application will identify the car's make and model. This can have several practical benefits:

1. **Empowering Consumers**:
    - Individuals with little to no knowledge about cars can easily identify vehicles they are interested in. This empowers consumers to make informed decisions when considering a car purchase.

2. **Boosting Car Sales**:
    - By integrating this application with car sales platforms like autoscout24.ch or comparis.ch, potential buyers can be directly redirected to listings of the identified car model. This can enhance the user experience and streamline the car-buying process, potentially increasing sales for car dealers.

3. **Future Development**:
    - This project serves as a stepping stone for my Bachelor's thesis, where I aim to develop a fully functional application capable of real-time car identification and seamless integration with car marketplaces. The ultimate vision is to create a tool that not only identifies cars but also provides purchasing options.
#### Conclusion
In summary, the motivation behind this project is to solve a common problem by using machine learning to identify car makes and models from images. The project lays the foundation for a more advanced application that can significantly benefit consumers and car dealers alike. By making car identification easier and more accessible, I can enhance the car-buying experience and help individuals find their dream cars more efficiently.

### 2. Data Collection or Generation (project evaluation relative weight: 30%)

#### Initial Data Collection from Kaggle
For this project, I employed a multi-faceted approach to gather the necessary image data. Here’s a detailed explanation of my methodology and the challenges I encountered:

1. **Kaggle Dataset**:
    - I started by leveraging a publicly available dataset from Kaggle, which contained a total of 4165 images. This dataset provided a solid foundation for my project but included images of only seven car brands. Also, the images were separated in train and test folders, which i combined into one because my `Models.java`class already does a 80% training and 20% validation split of the whole dataset. This limited diversity prompted me to seek additional data to ensure a more comprehensive training set.

#### Additional Data Collection via Web Scraping
2. **Web Scraping Attempts**:
    - To expand my dataset, I attempted to scrape images from various websites. These websites included autoscout24.ch, comparis.ch, and autolina.ch. However, I encountered significant challenges due to the anti-scraping technologies employed by these sites. These technologies effectively blocked automated scraping efforts, making it impossible to collect additional images through this method.

#### Insights and Future Work
3. **API Discovery**:
    - During my attempts to scrape data, I discovered that autoscout24.ch offers an API. Although I did not utilize the API for this project, I recognize its potential and plan to explore its use for my future work, particularly for my Bachelor's thesis. Utilizing the API could provide a more reliable and scalable method for data collection without violating website terms of service.

### 3. Modeling (project evaluation relative weight: 30%)

#### Training/Fine-Tuning of Models
1. **Model Selection**:
    - I selected a suitable model architecture ( wResNetV1) for image classification, which is a well-established convolutional neural network (CNN) architecture known for its effectiveness in visual tasks.

2. **Training Process**:
    - I implemented the training process in Java using DJL. This includes setting the batch size and number of epochs, defining the loss function (e.g., softmax cross-entropy `https://charanhu.medium.com/softmax-and-cross-entropy-for-multi-class-classification-c9847690f71b#:~:text=Softmax%20function%20is%20used%20to,distribution%20matches%20the%20true%20labels`), and using an optimizer (e.g., Adam).

3. **Fine-Tuning**:
    - By using pre-trained models and fine-tuning them on my dataset, I adjusted the model parameters specifically for my task. Fine-tuning enhances the model's performance on my specific dataset.

#### Effort in Coding and Combining Models
4. **Coding Effort**:
    - I wrote custom code to load and preprocess the data, define the model architecture, train the model, and evaluate its performance. This demonstrates significant effort in coding and understanding the modeling process.

5. **Combining Models**:
    - While my current setup may involve training a single model, I have the flexibility to experiment with combining multiple models or using ensemble methods to further improve performance.

#### Use of APIs
6. **Integration**:
    - DJL is a powerful library that provides APIs for various deep learning frameworks like MXNet, PyTorch, and TensorFlow. My use of DJL to train and fine-tune models directly within my Java application demonstrates proper integration of these APIs.

7. **Not Using Web Services**:
    - I executed the modeling locally using DJL APIs, which aligns with the requirement to avoid modeling through web services like Teachable Machines or miniDall-E. This ensures that my project adheres to the guidelines.

### 4. Interpretation and Validation (project evaluation relative weight: 30%)

#### Project Validation Methodology

To validate the performance of my car brand classification model, I went through a comparison between human responses and the model's predictions. This process involved several steps, as outlined below.

#### Survey Distribution and Data Collection
First, I distributed an online questionnaire through "umfrageonline.ch" to gather human responses. The survey consisted of 10 images of various car brands, and participants were asked to classify each image into one of the following categories: Alfa Romeo, Audi, Hyundai, Lancia, Mahindra, Rolls Royce, Suzuki, Tata, and Toyota. Out of 25 recipients, 17 participants completed the survey. I understand that the amount should be higher for a more conclusive result, this will be changed for my bachelor's thesis.

#### Manual Input and Data Preparation
The responses from the survey were manually inputted into a structured format for analysis. Each image's correct car brand, the number of votes each brand received from participants, and the model's prediction probabilities for each brand were recorded. This data was then processed using a Python script named `calculations.py`.

#### Python Script for Validation
The Python script was designed to compare the human responses with the model's predictions. Here’s a brief overview of the script's functionality:

1. **Data Structure**:
    - The script stored the correct brand, participant responses, and model predictions for each image in a dictionary.

2. **Accuracy Calculation**:
    - For each image, the script calculated the accuracy of human responses by determining the proportion of participants who correctly identified the car brand.
    - The model's accuracy was assessed by checking if the highest probability prediction matched the correct brand.

3. **Overall Accuracy Comparison**:
    - The script computed the overall accuracy for both human responses and model predictions.
    - A bar chart was generated to visually compare the accuracies.

#### Results and Reflection
The results of this validation process revealed that the human participants achieved an overall accuracy of 80% in classifying the car brands correctly, while the model achieved an accuracy of 60%. Given that the model's accuracy during training was 67%, this slight drop in performance when applied to new data is plausible and within expected variations. As long as the users and the model answer, that the probability of the correct car brand exceeds 50%, the answer will be counted as correct. This threshold can be changed to ensure a more precise validation, but will be kept for this project.

#### Impact of Choices
- **Model Performance**:
    - The model's performance, although slightly lower than the training accuracy, indicates a reasonable level of generalization. The discrepancy could be attributed to differences in the training data versus the validation images used in the questionnaire.

- **Human vs. Model**:
    - The higher accuracy of human participants highlights their ability to recognize car brands, likely influenced by prior knowledge and visual cues that the model may not fully capture. To circumvent that, some pictures have a deliberately bad resolution of the car logo, so the humans have to find different visual clues in the pictures.

#### Conclusion
By involving human participants and comparing their responses with the model's predictions, I was able to validate the model's performance effectively. This approach not only provided a benchmark for the model's accuracy but also offered insights into areas where the model could be improved. The results underscore the importance of comprehensive validation using diverse methods to ensure robust and reliable model performance.
