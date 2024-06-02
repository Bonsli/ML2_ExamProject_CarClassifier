# Car Brand Classification

## Project Overview

This project aims to create a foundational application that can identify the make and model of a car from a photograph using machine learning techniques.

## Installation and Setup

### Prerequisites

- Python 3.12.1
- Java Development Kit (JDK)
- Apache Maven
- Node.js (optional, if you have any front-end dependencies that require it)
- Deep Java Library (DJL)

### Setting up a Virtual Environment (Optional but Recommended)

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

### Installing Dependencies

1. Install the necessary Python dependencies using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

2. Ensure you have DJL and other Java dependencies set up. You can manage Java dependencies using Maven by including the necessary dependencies in your `pom.xml` file.


### Data Collection

If you want to check out the used dataset from Kaggle, follow this link: https://www.kaggle.com/datasets/kshitij192/cars-image-dataset
The dataset has two sub-folders (test and train), I combined the files in the two sub-folders into one and deleted a few pictures, so the amount of one brand does not eclipse another one. 


### Scraping Additional Data (Optional)

If you wish to scrape additional car images for more data points or understand how I scraped, you can use the provided scraping script. Ensure you have the required libraries installed (e.g., BeautifulSoup, requests):

1. Install necessary libraries (if not already installed):

    ```bash
    pip install beautifulsoup4 requests
    ```

2. Run the scraping script:

    ```bash
    python scrape_images.py
    ```

 I edited the code so a new Carbrand and Modell (Fiat 500) will be searched, a new folder and subfolder will be generated in the Cars_Dataset folder (which is used in the `Training.java` class) and the first 25 pictures of this website will be scraped. Due to the fact the website only refreshes when you scroll and for that the Selenium is needed, i refrained from using that
 (here a Medium article if more information is wanted https://medium.com/@irfanbasyar.ib/how-to-scrape-data-from-a-webpage-with-infinite-scrolling-using-python-and-beautifulsoup-f3c39e52ae8).

### Training the Model

1. Compile and run the Java application to start the training process:

    Run Training.java

### Starting the Spring Boot Application

1. Ensure your Spring Boot application is set up. Navigate to the project directory and start the application:

    ```bash
    mvn spring-boot:run
    ```
    OR
    Through the Maven Extension in VSCode / playground / Plugins / spring-boot / run

2. The application will start on `localhost:8080`. Open your web browser and go to:

    ```text
    http://localhost:8080
    ```

### Using the Application

1. On the homepage of the application, you will see an option to upload an image. Click on "Choose File" to upload a car image (jpeg, png).

2. I suggest using a Car from the folder "Questionnaire Pictures", because they were used for the questionnaire to validate the models answers with real people. All car pictures in the folder "Cars_Dataset" can be used as well as downloaded pictures of the respective brands mentioned in the folder. 

### Running the Validation Script

To compare the human responses with the model's predictions:

1. Ensure all responses from the questionnaire and model are manually entered into the appropriate format as expected by `calculation.py`. The answers from the questionnaire are saved as screenshots in the "Questionnaire Answers" folder if validation for the data is wanted.

2. Run the validation script:

    ```bash
    python calculation.py
    ```
    OR
    Run button in VSCode while bein in `calculation.py`. 

3. The script will output the accuracy comparison between human responses and the model's predictions and generate a bar chart for visual comparison.

