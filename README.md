# **Rainfall Prediction Using Machine Learning**

This project aims to predict whether it will rain tomorrow using historical weather data from the **weatherAUS** dataset (sourced from [Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)). The prediction is modeled as a binary classification problem, where various machine learning algorithms are applied, and the best-performing model is deployed using Streamlit for an interactive user experience.

## **Table of Contents**

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling](#modeling)
- [Model Evaluation](#model-evaluation)
- [Deployment](#deployment)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

---

## **Project Overview**

The objective of this project is to predict rainfall for the next day based on weather data from various Australian cities. Key steps in the project include:

- Exploratory Data Analysis (EDA) to clean and understand the data.
- Feature engineering and selection.
- Training multiple machine learning models: **XGBClassifier**, **RandomForestClassifier**, **LogisticRegression**, **KNeighborsClassifier**, and **GaussianNB**.
- Comparing models based on performance metrics and selecting the best one.
- Deploying the best-performing model using **Streamlit** to create an interactive web application.

## **Dataset**

The dataset used for this project is **weatherAUS**, which contains daily weather observations from various locations in Australia. The dataset can be found on Kaggle: [WeatherAUS Dataset](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package).

### **Target Variable:**
- **RainTomorrow:** A binary variable indicating whether it will rain the next day.

### **Feature Variables:**
- Temperature, humidity, wind speed, atmospheric pressure, and other weather-related metrics.

## **Features**

- **Rainfall Prediction**: Predict if it will rain tomorrow based on today's weather data.
- **Interactive User Interface**: Enter weather data manually or use sliders for predictions.
- **Real-Time Prediction**: Instantly predict the probability of rain using the trained model.
- **Visualization**: Display feature importance or key metrics in the Streamlit app.

## **Installation**

### **Requirements**

Before running the project, ensure you have the following dependencies installed:

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- streamlit

### **Installation Steps**

1. Clone the repository:
   ```bash
   git clone https://github.com/Sachin8871/Rainfall-Prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rainfall-prediction
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

To run the Streamlit application locally:

1. Ensure all required dependencies are installed.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. The app will be available at `http://localhost:8501/` in your browser.

In the app, you can input weather parameters (like temperature, humidity, etc.) to predict whether it will rain tomorrow.

## **Modeling**

Several machine learning algorithms were used for the prediction task, including:

- **XGBoost (XGBClassifier)**
- **RandomForestClassifier**
- **LogisticRegression**
- **KNeighborsClassifier**
- **GaussianNB**

Each model was evaluated using metrics such as **Accuracy**, **Precision**, **Recall**, **F1-Score**, and **ROC-AUC**.

## **Model Evaluation**

After training and evaluating all models, **XGBClassifier** emerged as the best-performing model with the following metrics:

Accuracy: 85.63%
Precision
False (No Rain): 0.88
True (Rain): 0.72
Recall
False (No Rain): 0.94
True (Rain): 0.56
F1-Score
False (No Rain): 0.91
True (Rain): 0.63


## **Deployment**

The project is deployed using **Streamlit** to create an interactive web application where users can input weather parameters and get predictions. The app provides real-time feedback and predictions for whether it will rain tomorrow.

To run the app, use the following command:
```bash
streamlit run app.py
```
-**Streamlit App**: [https://rainfall-prediction-lobkjmcpdg8axhje5ungim.streamlit.app/]

## **Future Work**

Some possible future improvements and extensions for this project include:

- **Real-Time Data Integration**: Integrate live weather data APIs to provide up-to-date predictions.
- **Improved Model Performance**: Experiment with other advanced models or ensemble methods to boost accuracy.
- **Data Enrichment**: Add more features, such as climate indices or satellite data, for better predictions.
- **Enhanced UI/UX**: Improve the visual design and add more interactive features to the Streamlit app.

---

### **Contact**

If you have any questions or suggestions, feel free to reach out to me at:

- **Email**: [sachindhakad211023@gmail.com]
- **LinkedIn**: [https://www.linkedin.com/in/sachin-kumar88/]
- **GitHub**: [https://github.com/Sachin8871]
