from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


# ---------------------------------------
# Load trained model
# ---------------------------------------

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# ---------------------------------------
# Home page
# ---------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------
# Prediction
# ---------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # 1. Bedrooms
        bedrooms = float(request.form["bedrooms"])

        # 2. Bathrooms
        bathrooms = float(request.form["bathrooms"])

        # 3. Sqft Living
        sqft_living = float(request.form["sqft_living"])

        # 4. Sqft Lot
        sqft_lot = float(request.form["sqft_lot"])

        # 5. Floors
        floors = float(request.form["floors"])

        # 6. Waterfront
        waterfront = float(request.form["waterfront"])

        # 7. View
        view = float(request.form["view"])

        # 8. Condition
        condition = float(request.form["condition"])

        # 9. Sqft Above
        sqft_above = float(request.form["sqft_above"])

        # 10. Sqft Basement
        sqft_basement = float(request.form["sqft_basement"])

        # 11. Year Built
        yr_built = float(request.form["yr_built"])

        # 12. Year Renovated
        yr_renovated = float(request.form["yr_renovated"])


        # ---------------------------------------
        # 13. City
        # ---------------------------------------

        city_name = request.form["city"]

        city_mapping = {
            "Algona": 0,
            "Auburn": 1,
            "Bellevue": 2,
            "Black Diamond": 3,
            "Bothell": 4,
            "Burien": 5,
            "Carnation": 6,
            "Clyde Hill": 7,
            "Covington": 8,
            "Des Moines": 9,
            "Duvall": 10,
            "Enumclaw": 11,
            "Fall City": 12,
            "Federal Way": 13,
            "Hunts Point": 14,
            "Issaquah": 15,
            "Kenmore": 16,
            "Kent": 17,
            "Kirkland": 18,
            "Lake Forest Park": 19,
            "Maple Valley": 20,
            "Medina": 21,
            "Mercer Island": 22,
            "Milton": 23,
            "Newcastle": 24,
            "Normandy Park": 25,
            "North Bend": 26,
            "Pacific": 27,
            "Preston": 28,
            "Ravensdale": 29,
            "Redmond": 30,
            "Renton": 31,
            "Sammamish": 32,
            "SeaTac": 33,
            "Seattle": 34,
            "Shoreline": 35,
            "Skykomish": 36,
            "Snoqualmie": 37,
            "Snoqualmie Pass": 38,
            "Tukwila": 39,
            "Vashon": 40,
            "Woodinville": 41
        }

        # Check whether city exists
        if city_name not in city_mapping:
            return render_template(
                "index.html",
                prediction="Invalid city name"
            )

        city = city_mapping[city_name]


        # ---------------------------------------
        # 14. Country
        # ---------------------------------------

        country_name = request.form["country"]

        country_mapping = {
            "USA": 0
        }

        if country_name not in country_mapping:
            return render_template(
                "index.html",
                prediction="Invalid country name"
            )

        country = country_mapping[country_name]


        # ---------------------------------------
        # 15. Year
        # ---------------------------------------

        year = float(request.form["year"])


        # ---------------------------------------
        # 16. Month
        # ---------------------------------------

        month = float(request.form["month"])


        # ---------------------------------------
        # 17. Date
        # ---------------------------------------

        date = float(request.form["date"])


        # ---------------------------------------
        # Create input array
        # ---------------------------------------

        input_data = np.array([[
            bedrooms,          # 1
            bathrooms,         # 2
            sqft_living,       # 3
            sqft_lot,          # 4
            floors,            # 5
            waterfront,        # 6
            view,              # 7
            condition,         # 8
            sqft_above,        # 9
            sqft_basement,     # 10
            yr_built,          # 11
            yr_renovated,      # 12
            city,              # 13
            country,           # 14
            year,              # 15
            month,             # 16
            date               # 17
        ]])


        print("Input Data:")
        print(input_data)

        print("Number of features:", input_data.shape[1])


        # ---------------------------------------
        # Prediction
        # ---------------------------------------

        prediction = model.predict(input_data)[0]

        prediction = round(prediction, 2)


        # ---------------------------------------
        # Send prediction to HTML
        # ---------------------------------------

        return render_template(
            "index.html",
            prediction=prediction
        )


    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {e}"
        )


# ---------------------------------------
# Run application
# ---------------------------------------

if __name__ == "__main__":
    app.run(debug=True)