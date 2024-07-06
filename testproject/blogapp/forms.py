from django import forms
from .models import details
class blogsform(forms.ModelForm):
    class Meta:
        model=details
        fields=['name','age','department']

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'message']
