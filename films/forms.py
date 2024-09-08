from django import forms


class SearchFilmForm(forms.Form):
    name = forms.CharField(max_length=30)
