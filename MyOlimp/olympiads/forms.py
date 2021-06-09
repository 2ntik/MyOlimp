from django import forms


class OlympiadSearchForm(forms.Form):
    string = forms.CharField()
