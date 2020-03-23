from django import forms
from . import models

class SearchForm(forms.ModelForm):
    class meta:
        model = models.Search
        fields = ("search_engine, keyword")



