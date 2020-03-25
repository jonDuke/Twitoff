# my_app/routes/iris_routes.py

from flask import Blueprint, request, jsonify, render_template
from sklearn.datasets import load_iris # just to have some data to use when predicting

from my_app.iris_classifier import load_model

iris_routes = Blueprint("iris_routes", __name__)

@iris_routes.route("/iris")
def iris():
    model = load_model()
    X, y = load_iris(return_X_y=True) # just to have some data to use when predicting
    result = model.predict(X[:2, :])
    return str(result)
