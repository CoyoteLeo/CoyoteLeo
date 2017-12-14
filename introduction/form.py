from django.forms import ModelForm
from django import forms
from .models import Contact

class ReplyForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message' ]
        widgets = {
            'name': forms.TextInput(
                attrs={"required":True,},
            ),
            'email':forms.EmailInput(
                attrs={"required":True}
            ),
            'message': forms.Textarea(
                attrs={"required":True,"rows":5}
            )
        }
