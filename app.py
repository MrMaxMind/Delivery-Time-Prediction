from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the trained XGBoost model
with open('best_xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data from user input and cast each input explicitly to the correct data type
    try:
        multiple_deliveries = int(request.form['multiple_deliveries'])
        age = int(request.form['age'])
        vehicle_condition = int(request.form['vehicle_condition'])
        delivery_person_ratings = float(request.form['delivery_person_ratings'])
        order_prepare_time = int(request.form['order_prepare_time'])
        weather_conditions = int(request.form['weather_conditions'])
        type_of_vehicle = int(request.form['type_of_vehicle'])
        festival = int(request.form['festival'])
        city = int(request.form['city'])
        road_traffic_density = int(request.form['road_traffic_density'])
        date = int(request.form['date'])  # Since date is between 1-30, cast it to int

        # Combine all inputs into a NumPy array, ensuring dtype=float to avoid Unicode issues
        input_features = np.array([[multiple_deliveries, age, vehicle_condition, delivery_person_ratings,
                                    order_prepare_time, weather_conditions, type_of_vehicle, festival, 
                                    city, road_traffic_density, date]], dtype=float)

        # Make prediction
        prediction = model.predict(input_features)

        # Return the prediction to be displayed on the webpage
        return render_template('index.html', prediction_text=f'Estimated Delivery Time: {prediction[0]} minutes')

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
