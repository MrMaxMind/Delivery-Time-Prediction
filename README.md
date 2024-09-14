# Delivery Time Prediction Web App

Welcome to the Delivery Time Prediction Web App repository. This project aims to predict delivery times for orders based on various factors such as delivery person details, weather, traffic density, and more using machine learning. Below are instructions for setting up the project, its features, and deployment on Render using Docker.

---

<div align="center">
  <img src="./delivery_image.png" alt="Delivery Image" style="border:none;">
</div>

## Overview

This project is built to predict the time taken for deliveries using a trained XGBoost model. Users can input delivery details (e.g., multiple deliveries, vehicle condition, weather) and get a prediction for the expected delivery time. The project includes a Flask backend, an interactive frontend, and uses Docker for deployment.

---

## Features

- `Data Preprocessing`: Handles missing values, encodes categorical variables, and normalizes data.
- `Model Building`: Trains an XGBoost model and saves the best model for deployment.
- `Model Evaluation`: Uses metrics like MAE, MSE, and R-squared for evaluation.
- `Web Application`: Provides an interactive web interface for users to input data and predict delivery times.
- `Render Deployment`: The project can be easily deployed using Render’s cloud platform with Docker.

---

## Contents

- `app.py`: Flask backend for model loading and predictions.
- `best_xgb_model.pkl`: Pretrained XGBoost model file.
- `notebooks/food_delivery_time_prediction.ipynb`: Jupyter notebook used to preprocess data, train, and save the model.
- `templates/index.html`: Frontend HTML form for user input.
- `static/style.css`: Custom CSS for styling the frontend.
- `requirements.txt`: List of required Python dependencies.
- `Dockerfile`: Configuration file for Docker to containerize the web app.

---

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/Delivery-Time-Prediction.git
   cd Delivery Time Prediction
   
2. **Install the required packages**:
   Ensure you have Python 3.x installed. Install dependencies by running:
   ```bash
   pip install -r requirements.txt
   
4. **Run the Jupyter Notebook**:
   Train the XGBoost model using the provided notebook if necessary:
   ```bash
   notebooks/food_delivery_time_prediction.ipynb

5. **Run the Flask App**:
   To start the web app locally:
   ```bash
   python3 app.py
   Open your web browser and go to `http://127.0.0.1:5000/`

---

## Deployment Instructions

### 1. Model Training: 

Train the model using the provided Jupyter notebook and save the trained model as best_xgb_model.pkl.

### 2. Deploy the App on Render:

- Push your project to GitHub.
- Create a new web service on Render, connecting it to your GitHub repository.
- Ensure app.py is set as the entry point and requirements.txt includes all dependencies.

### 3. Configure the Environment:

- Add the necessary environment variables if required.
- Deploy the app, and Render will automatically start your service.

---

## Key Insights

- Successfully trained and deployed an XGBoost model for delivery time predictions.
- Frontend designed with Bootstrap for user-friendly input and prediction display.
- Seamlessly deployable on Render using Docker for containerization.

---

## Tools and Libraries

- Flask: For the web backend.
- Pandas: For data manipulation and analysis.
- Scikit-learn: For implementing machine learning models.
- XGBoost: For gradient boosting algorithms.
- Matplotlib and Seaborn: For data visualization.
- HTML, CSS, JavaScript: For creating the frontend interface.

---

## Contributing
If you have suggestions or improvements, feel free to open an issue or create a pull request.

---

## *Thank you for visiting! If you find this project useful, please consider starring the repository. Happy coding!*
