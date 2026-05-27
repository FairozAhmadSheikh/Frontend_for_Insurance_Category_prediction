from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "http://51.21.252.70:8000/predict"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        input_data = {
            "age": int(request.form["age"]),
            "weight": float(request.form["weight"]),
            "height": float(request.form["height"]),
            "income_lpa": float(request.form["income_lpa"]),
            "smoker": request.form["smoker"] == "True",
            "city": request.form["city"],
            "occupation": request.form["occupation"]
        }

        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()