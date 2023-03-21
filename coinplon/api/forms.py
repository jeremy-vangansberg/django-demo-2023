from .models import ApiModel
from django import forms

class ApiForm(forms.ModelForm):
    class Meta :
        model = ApiModel
        fields = '__all__'
        labels = {
            'slug' : "Entrez votre crypto ici",
            'convert': "Entrez votre devise ici"
                  }