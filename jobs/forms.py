from django import forms
from .models import Aplay ,Jobs  


class APlayForm(forms.ModelForm):
    class Meta:
        model = Aplay
        fields = ['name','email','website','load_cv','note']
        
class AddJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        exclude=('addman','slug',)
    