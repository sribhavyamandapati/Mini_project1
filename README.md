
# 🏠 House Price Prediction Using Multiple Linear Regression

A Machine Learning web application that predicts house prices based on different house features using **Multiple Linear Regression**. The trained model is integrated with a **Flask** web application and deployed on **Render**, making the prediction system accessible through a public URL.

## 📌 Project Overview

House prices depend on several factors such as the number of bedrooms, bathrooms, living area, lot size, location, condition, grade, and other property characteristics.

The objective of this project is to build a Machine Learning model that learns the relationship between these house features and their prices and then predicts the price of a house based on user-provided inputs.

The project covers the complete Machine Learning workflow:

**Data Collection → Data Preprocessing → Feature Engineering → Train-Test Split → Model Training → Prediction → Evaluation → Model Saving → Flask Application → Deployment**

---

## 🎯 Project Objectives

* Build a house price prediction model.
* Perform data preprocessing and feature engineering.
* Convert categorical data into numerical form.
* Extract useful information from date columns.
* Train a Multiple Linear Regression model.
* Evaluate the model using performance metrics and RMSE.
* Save the trained model using Pickle.
* Develop a Flask web application.
* Deploy the application using Render.
* Provide a publicly accessible house price prediction system.

---

## 📊 Dataset

The project uses a house price dataset containing information about different properties.

### Important Features

| Feature        | Description                                |
| -------------- | ------------------------------------------ |
| `bedrooms`     | Number of bedrooms                         |
| `bathrooms`    | Number of bathrooms                        |
| `sqft_living`  | Living area in square feet                 |
| `sqft_lot`     | Lot size in square feet                    |
| `floors`       | Number of floors                           |
| `waterfront`   | Whether the property has waterfront access |
| `view`         | View rating                                |
| `condition`    | Overall condition of the house             |
| `grade`        | Construction/design grade                  |
| `yr_built`     | Year the house was built                   |
| `yr_renovated` | Year the house was renovated               |
| `city`         | City where the property is located         |
| `country`      | Country/location information               |
| `date`         | Date associated with the property record   |
| `price`        | Target house price                         |

---

# 🔧 Data Preprocessing

Before training the Machine Learning model, the dataset was cleaned and converted into a format that could be understood by the algorithm.

## 1. Categorical Data Conversion

Machine Learning algorithms require numerical input. Therefore, categorical values such as city names were converted into numerical values.

For example:

```text
Seattle   → 0
Kent      → 1
Bellevue  → 2
```

This conversion allowed categorical information to be used as input features by the Machine Learning model.

> **Note:** This project uses numerical label mapping for demonstration. In a production system, One-Hot Encoding would generally be preferred for nominal categories such as city.

---

## 2. Date Feature Extraction

The original dataset contained a date column.

Instead of directly passing the date to the model, it was separated into three numerical features:

```text
day
month
year
```

For example:

```text
2014-06-04
```

was converted into:

```text
year  = 2014
month = 6
day   = 4
```

These numerical features were then used during model training.

---

# 🤖 Machine Learning Algorithm

## Multiple Linear Regression

Multiple Linear Regression is a supervised Machine Learning algorithm used when there is:

* One dependent variable
* Multiple independent variables

The general equation is:

```text
Y = b₀ + b₁X₁ + b₂X₂ + b₃X₃ + ... + bₙXₙ
```

Where:

* `Y` = Predicted value
* `b₀` = Intercept
* `b₁, b₂, ..., bₙ` = Coefficients learned by the model
* `X₁, X₂, ..., Xₙ` = Independent variables

### In This Project

```text
Dependent Variable
        ↓
   House Price
```

The independent variables are the different characteristics of the house.

The model learns how these features are related to the house price during training.

---

# ✂️ Train-Test Split

After preprocessing, the dataset was divided into training and testing datasets using an **80:20 ratio**.

```text
80% → Training Dataset
20% → Testing Dataset
```

Approximately:

```text
Training Data → 3680 rows
Testing Data  → 920 rows
```

### Training Dataset

The training data is used by the model to learn the relationship between house features and house prices.

### Testing Dataset

The testing data contains unseen records and is used to evaluate how well the trained model performs on new data.

---

# 🏋️ Model Training

The `LinearRegression` class from Scikit-learn was used.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

The `fit()` function trains the model.

During training, the model learns:

* Coefficients
* Intercept
* Relationship between input features and house prices

---

# 🔮 Prediction

After training, the `predict()` function is used to generate predictions.

```python
y_pred = model.predict(X_test)
```

The model receives the house features and generates a predicted house price.

Example:

| Actual Price | Predicted Price |
| -----------: | --------------: |
|       450000 |          440000 |
|       600000 |          615000 |
|       300000 |          290000 |

The predicted values are then compared with the actual values to evaluate model performance.

---

# 📈 Model Evaluation

The model was evaluated using both training and testing datasets.

## Training Evaluation

The trained model was evaluated on the training dataset using:

* Training Performance
* Training RMSE

## Testing Evaluation

The trained model was evaluated on the unseen testing dataset using:

* Testing Performance
* Testing RMSE

Testing performance is particularly important because it indicates how well the model can generalize to data that it did not see during training.

---

# 📉 Root Mean Square Error (RMSE)

RMSE stands for **Root Mean Square Error**.

It measures the average magnitude of the prediction error.

The formula is:

```text
RMSE = √(Mean((Actual Value - Predicted Value)²))
```

In this project, RMSE was calculated to measure the difference between actual house prices and predicted house prices.

### Interpretation

```text
Lower RMSE
     ↓
Smaller prediction errors
     ↓
Predictions are generally closer to actual values
```

However, RMSE should always be interpreted together with other model evaluation metrics and the scale of the target variable.

---

# 💾 Model Saving

After training, the trained Machine Learning model was saved using Python's `pickle` module.

```python
import pickle

with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)
```

The saved model can later be loaded without retraining.

```python
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)
```

This makes it possible for the Flask application to use the already-trained model for predictions.

---

# 🌐 Flask Web Application

The trained Machine Learning model was integrated into a Flask web application.

The application provides an interface where users can enter house-related information and receive a predicted house price.

## Application Workflow

```text
User enters house details
          ↓
   Flask Web Application
          ↓
     Receive Input
          ↓
   Load Trained Model
          ↓
    Prepare Features
          ↓
     Model Prediction
          ↓
   Predicted House Price
          ↓
    Display Result
```

---

# 📦 Requirements

The project uses the following Python libraries:

```text
Flask
NumPy
Pandas
Scikit-learn
Gunicorn
```

These dependencies are specified in `requirements.txt`.

Example:

```text
Flask
numpy
pandas
scikit-learn
gunicorn
```

The deployment platform uses this file to install the required dependencies automatically.

---

# 🚀 Deployment

The Flask application was deployed using **Render**.

### Deployment Process

```text
Develop ML Project
        ↓
Create Flask Application
        ↓
Save Trained Model
        ↓
Create requirements.txt
        ↓
Create Procfile
        ↓
Upload Project to GitHub
        ↓
Connect GitHub Repository to Render
        ↓
Deploy Application
        ↓
Generate Public URL
```

After deployment, the application can be accessed through a web browser without manually running the Python program locally.

---

# 📄 Procfile

The project uses a `Procfile` to specify how the Flask application should be started.

```text
web: gunicorn app:app
```

Here:

```text
app.py
  ↓
Python file name = app

Flask object
  ↓
app = Flask(__name__)
```

Therefore:

```text
app:app
```

means:

```text
Python file : Flask application object
```

---

# 📁 Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
├── Procfile
├── README.md
│
└── templates/
    └── index.html
```

### File Description

| File                    | Purpose                              |
| ----------------------- | ------------------------------------ |
| `app.py`                | Flask backend and prediction logic   |
| `house_price_model.pkl` | Saved trained Machine Learning model |
| `requirements.txt`      | Required Python dependencies         |
| `Procfile`              | Deployment start command             |
| `README.md`             | Project documentation                |
| `index.html`            | User interface                       |

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Multiple Linear Regression

### Data Processing

* Pandas
* NumPy

### Web Development

* Flask
* HTML
* CSS

### Model Serialization

* Pickle

### Deployment

* Gunicorn
* Render

### Version Control

* Git
* GitHub

---

# ⭐ Key Features

* 🏠 House price prediction
* 🤖 Multiple Linear Regression
* 📊 Data preprocessing
* 🔢 Categorical data conversion
* 📅 Date feature extraction
* ✂️ 80:20 train-test split
* 🏋️ Model training using `fit()`
* 🔮 Prediction using `predict()`
* 📈 Training performance evaluation
* 📊 Testing performance evaluation
* 📉 RMSE calculation
* 💾 Model saving using Pickle
* 🌐 Flask web application
* 📦 Dependency management using `requirements.txt`
* 🔗 GitHub integration
* 🚀 Render deployment
* 🌍 Publicly accessible application

---

# 🔄 Complete Project Workflow

```text
                    Kaggle Dataset
                         ↓
                  Data Collection
                         ↓
                 Data Preprocessing
                         ↓
              Feature Engineering
                    ↙          ↘
          Categorical Data     Date Column
          city, country        day/month/year
                    ↘          ↙
                  Prepare Features
                         ↓
              Independent Variables (X)
                         +
               Dependent Variable (Y)
                         ↓
                  Train-Test Split
                         ↓
                       80/20
                         ↓
              Multiple Linear Regression
                         ↓
                    model.fit()
                         ↓
                  Model Training
                         ↓
              ┌──────────┴──────────┐
              ↓                     ↓
       Training Dataset       Testing Dataset
              ↓                     ↓
         Predictions            Predictions
              ↓                     ↓
      Performance + RMSE    Performance + RMSE
              └──────────┬──────────┘
                         ↓
                 Save Trained Model
                         ↓
                       Pickle
                         ↓
                Flask Web Application
                         ↓
                    GitHub
                         ↓
                     Render
                         ↓
                Public Application
```

---

# 🔮 Future Improvements

The project can be further improved by:

### Machine Learning Improvements

* Use **One-Hot Encoding** for categorical variables.
* Compare Multiple Linear Regression with:

  * Random Forest Regression
  * Decision Tree Regression
  * Gradient Boosting
  * XGBoost
* Perform feature selection.
* Perform additional feature engineering.
* Experiment with feature scaling where appropriate.
* Tune model parameters for alternative regression algorithms.
* Add cross-validation.

### Evaluation Improvements

* Add MAE.
* Add MSE.
* Add R² Score.
* Compare multiple models.
* Visualize actual vs predicted prices.
* Analyze residual errors.

### Application Improvements

* Add input validation.
* Improve the user interface.
* Add responsive design.
* Add prediction history.
* Add a database.
* Add authentication.
* Add data visualization.
* Improve error handling.
---

# 📊 Project Highlights

```text
Machine Learning Algorithm
        ↓
Multiple Linear Regression

Data Processing
        ↓
Pandas + NumPy

Model Training
        ↓
Scikit-learn

Model Storage
        ↓
Pickle

Web Application
        ↓
Flask

Deployment
        ↓
Render

Version Control
        ↓
Git + GitHub
```

---
---

# ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

**Live Application:**
https://mini-project1-1-vn92.onrender.com

**GitHub Repository:**
https://github.com/sribhavyamandapati/Mini_project1

