from django import forms

class RecipesForm(forms.Form):
    name = forms.CharField(max_length=100)
    ingredients = forms.CharField(max_length=250)
    recipe = forms.CharField(max_length=1000)