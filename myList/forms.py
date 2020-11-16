from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter code e.g Grocery Shopping'}
    ))