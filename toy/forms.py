from django import forms
from django.contrib.auth import get_user_model

from .models import Toy

User = get_user_model()

class ToyCreateForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ToyCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].required = False

    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"name", "placeholder":"Enter your toy name"}))
    rent_price=forms.CharField(widget=forms.NumberInput(attrs={ "class":"form-control","id":"rent","placeholder":"Enter rent price","name":"rentprice","min":"0.01", "step":"0.01"}))
    sale_price=forms.CharField(widget=forms.NumberInput(attrs={ "class":"form-control","id":"sale","placeholder":"Enter sale price","name":"saleprice","min":"0.01", "step":"0.01"}))
    image=forms.ImageField(widget=forms.FileInput(attrs={ "class":"form-control-file","id":"pic","name":"myImage"}))

    class Meta:
        model = Toy
        fields = ['name','rent_price','sale_price','image']

    # validate data input
    # def clean_content(self):
    #     name = self.cleaned_data.get("name")
    #     if len(name) > 100:
    #         raise forms.ValidationError("This name is too long")
    #     return name

