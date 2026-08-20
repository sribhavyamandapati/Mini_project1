
# 🏠 House Price Prediction Using Multiple Linear Regression

## 📌 Project Overview

This project is a **House Price Prediction System** developed using **Multiple Linear Regression**.

Multiple Linear Regression is a supervised machine learning algorithm used to predict **one dependent variable using multiple independent variables**.

In this project:

- **Dependent Variable:** House Price
- **Independent Variables:** House-related features such as bedrooms, bathrooms, living area, lot area, floors, waterfront, view, condition, grade, year built, city, country, date-related features, etc.

The model learns the relationship between these input features and house prices and predicts the price of a new house based on the given inputs.

---

## 📊 Dataset

The dataset was downloaded from **Kaggle**.

The dataset contains approximately:

- **4600 rows**
- **16 columns**

Each row represents information about a house.

The dataset contains numerical, categorical, and date-related information.

---

## 🔧 Data Preprocessing

Before training the machine learning model, data preprocessing was performed.

### 1. Converting Categorical Data

The dataset contained categorical columns such as:

- `city`
- `country`

These categorical values were converted into numerical representations so that they could be used by the machine learning model.

Example:

```text
Seattle  → 0
Kent     → 1
Bellevue → 2

This conversion allowed the categorical information to be used by the machine learning model.

2. Date Conversion

The dataset contained a date column.

The date was converted into three separate columns:

day
month
year

For example:

2014-06-04

was converted into:

year  = 2014
month = 6
day   = 4

These columns were then used as numerical features during model training.

🤖 Multiple Linear Regression

Multiple Linear Regression is a supervised machine learning algorithm used when there is:

One dependent variable
Multiple independent variables

The general equation is:

Y = b0 + b1X1 + b2X2 + b3X3 + ... + bnXn

Where:

Y = Predicted value
b0 = Intercept
b1, b2, ... bn = Coefficients learned by the model
X1, X2, ... Xn = Independent variables

In this project:

Dependent Variable   → House Price
Independent Variables → House Features

The model learns the relationship between the independent variables and the house price during training.

✂️ Train-Test Split

After preprocessing, the dataset was divided into training and testing data using an 80:20 ratio.

80% → Training Dataset
20% → Testing Dataset

Approximately:

Training Data → 3680 rows
Testing Data  → 920 rows

The training data is used to train the model, while the testing data is used to evaluate the model on unseen data.

🏋️ Model Training

The LinearRegression class from the scikit-learn library was used.

from sklearn.linear_model import LinearRegression


model = LinearRegression()


model.fit(X_train, y_train)

The fit() function is used to train the model.

During training, the model learns the coefficients and intercept that represent the relationship between the input features and the house price.

🔮 Prediction

After training the model, the predict() function is used to generate predictions.

y_pred = model.predict(X_test)

The model takes the input features and predicts the house price.

For example:

Actual Price       Predicted Price
-----------------------------------
450000             440000
600000             615000
300000             290000

The predicted values are compared with the actual values to evaluate the model.

📈 Model Evaluation

After training the model, I evaluated the model in two stages.

Training Performance

The trained model was tested using the training dataset.

The following values were calculated:

Training Performance
Training RMSE
Testing Performance

The trained model was then evaluated using the testing dataset.

The following values were calculated:

Testing Performance
Testing RMSE

Testing performance is important because it shows how well the model performs on data that was not used during training.

📉 Root Mean Square Error (RMSE)

RMSE stands for Root Mean Square Error.

It measures the difference between the actual values and the predicted values.

The formula is:

RMSE = √(Mean((Actual Value - Predicted Value)²))

In this project, RMSE was calculated manually to measure the difference between the actual house prices and predicted house prices.

A lower RMSE generally indicates that the predicted values are closer to the actual values.

💾 Model Saving

After training the model, the trained model was saved using Python's pickle module.

import pickle


with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

The saved model can be loaded later without training the model again.

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

This allows the Flask application to use the already-trained model for making predictions.

🌐 Flask Web Application

After developing the machine learning model, a web application was created using Flask.

The application allows users to enter house-related information and receive a predicted house price.

Application Workflow
User enters house details
          ↓
Flask Web Application
          ↓
Receive Input Data
          ↓
Load Trained ML Model
          ↓
Pass Input Features to Model
          ↓
Predict House Price
          ↓
Display Predicted Price
📦 Requirements

The required Python libraries were added to the requirements.txt file.

The project uses libraries such as:

Flask
numpy
pandas
scikit-learn
gunicorn

The requirements.txt file allows the deployment platform to install all required dependencies automatically.

🚀 Deployment

The Flask application was deployed using Render.

The deployment process was:

Develop Project
      ↓
Create Flask Application
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
Get Public URL

After successful deployment, Render provides a public URL.

Using this URL, anyone can access the house price prediction application through a web browser without manually running the Python code every time.

📄 Procfile

A Procfile was created to specify how the Flask application should be started on Render.

Example:

web: gunicorn app:app

Here:

app before : represents the Python file app.py
app after : represents the Flask application object
🔗 Live Application
https://mini-project1-1-vn92.onrender.com

💻 GitHub Repository

GitHub Repository:
https://github.com/sribhavyamandapati/Mini_project1

📁 Project Structure
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
🛠️ Technologies Used
Programming Language
Python
Machine Learning
Scikit-learn
Multiple Linear Regression
Data Processing
Pandas
NumPy
Web Development
Flask
HTML
CSS
Model Saving
Pickle
Deployment
Gunicorn
Render
Version Control
Git
GitHub
⭐ Key Features
House price prediction using Machine Learning
Multiple Linear Regression
Data preprocessing
Categorical data conversion
Date feature extraction
80:20 train-test split
Model training using fit()
Prediction using predict()
Training performance evaluation
Testing performance evaluation
RMSE calculation
Trained model saved using Pickle
Flask web application
GitHub integration
Render deployment
Publicly accessible web application
🔮 Future Improvements

The project can be improved in the future by:

Using One-Hot Encoding for categorical variables such as city.
Comparing Multiple Linear Regression with other regression algorithms such as:
Random Forest Regression
Decision Tree Regression
Gradient Boosting
XGBoost
Performing feature selection.
Performing additional feature engineering.
Improving model performance.
Adding data visualization.
Adding more regression evaluation metrics.
Improving the user interface.
Adding proper input validation.
Adding a database to store prediction history.


🔄 Complete Project Workflow
                         Kaggle Dataset
                              ↓
                       Data Collection
                              ↓
                      Data Preprocessing
                              ↓
                ┌─────────────┴─────────────┐
                ↓                           ↓
        Categorical Data                Date Column
        city, country               day, month, year
                ↓                           ↓
                └─────────────┬─────────────┘
                              ↓
                       Prepare Features
                              ↓
                 Independent Variables (X)
                              +
                  Dependent Variable (Y)
                              ↓
                       Train-Test Split
                              ↓
                           80 / 20
                              ↓
                 Multiple Linear Regression
                              ↓
                        model.fit()
                              ↓
                       Model Training
                              ↓
             ┌────────────────┴────────────────┐
             ↓                                 ↓
      Training Dataset                  Testing Dataset
             ↓                                 ↓
       Predictions                       Predictions
             ↓                                 ↓
  Performance + RMSE              Performance + RMSE
             └────────────────┬────────────────┘
                              ↓
                     Save Trained Model
                              ↓
                            Pickle
                              ↓
                     Flask Web Application
                              ↓
                       GitHub Repository
                              ↓
                            Render
                              ↓
                   Public Application URL


📌 Conclusion

This project demonstrates the complete Machine Learning workflow, starting from dataset collection and preprocessing to model training, evaluation, web application development, and deployment.

The project uses Multiple Linear Regression to predict house prices based on multiple independent variables.

The trained model was integrated with a Flask web application, uploaded to GitHub, and deployed using Render.

The deployed application provides a simple way for users to enter house details and obtain a predicted house price.
