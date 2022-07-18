#from socket import fromshare
from django import forms
from core.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs = {
                'placeholder': 'name'}
                ),
            'color': forms.TextInput(attrs = {
                'placeholder': 'color'}
                ),
            'price': forms.TextInput(attrs = {
                'placeholder': 'price'}
                ),
        }