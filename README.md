# Text Classification System using Django & Scikit-learn

A Django web application that classifies user-entered text into one of the categories from the 20 Newsgroups dataset using a trained Support Vector Machine (SVM) model.

## Features

- Enter text through a web interface
- Predicts the text category using a trained ML model
- Built using Django
- Uses Scikit-learn's TF-IDF Vectorizer and SVM classifier
- Clean and minimal user interface

## Technologies Used

- Python
- Django
- Scikit-learn
- HTML
- CSS
- Pickle

## Machine Learning Workflow

1. Train the model using the training script.
2. Save the trained model, vectorizer, and target names as `.pickle` files.
3. Django loads these files during runtime.
4. User enters text through the web page.
5. The application predicts and displays the category.

## Project Structure

```text
text_classification_project/
│
├── classifier/
│   ├── ml_models/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── text_classification_project/
├── manage.py
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Sample Input & Output

### Sample Input

```
NASA successfully launched a new satellite into space.
```

### Predicted Output

```
sci.space
```

---

## Author

Josefa Stephane S.