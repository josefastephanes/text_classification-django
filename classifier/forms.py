from django import forms


class PredictionForm(forms.Form):
    text = forms.CharField(
        label="Enter Text",
        widget=forms.Textarea(attrs={
            "rows": 8,
            "placeholder": "Type your text here..."
        })
    )