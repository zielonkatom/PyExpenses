from django import forms
from datetime import date

# CATEGORIES = (
#     ('home', 'Home & Bills'),
#     ('transport', 'Transport'),
#     ('essentials', 'Essentials'),
#     ('clothes', 'Clothes & Shoes'),
#     ('health', 'Health & Beauty'),
#     ('education', 'Education'),
#     ('fun', 'Entertainment & Travel'),
#     ('cash', 'Cash')
# )
#
#
# class ExpeneseForm(forms.Form):
#     amount = forms.FloatField(label='Amount')
#     description = forms.CharField(label='Description', max_length=100)
#     date = forms.DateField()
#     category = forms.ChoiceField(label='Category',widget=forms.Select(choices=CATEGORIES))


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)

