import os
import pickle

from django.shortcuts import render

from .forms import PredictionForm


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "20newsgroups.pickle")
VECTORIZER_PATH = os.path.join(BASE_DIR, "ml_models", "20newsgroups_fitted_vectorizer.pickle")
TARGET_PATH = os.path.join(BASE_DIR, "ml_models", "20newsgroups_target_names.pickle")


with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

with open(VECTORIZER_PATH, "rb") as file:
    vectorizer = pickle.load(file)

with open(TARGET_PATH, "rb") as file:
    target_names = pickle.load(file)


def index(request):

    prediction = None

    form = PredictionForm()

    if request.method == "POST":

        form = PredictionForm(request.POST)

        if form.is_valid():

            text = form.cleaned_data["text"]

            text_vector = vectorizer.transform([text])

            predicted = model.predict(text_vector)

            prediction = target_names[predicted[0]]

    return render(
        request,
        "classifier/index.html",
        {
            "form": form,
            "prediction": prediction
        }
    )