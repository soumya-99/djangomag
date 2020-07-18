from django import forms
from .models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = All_Fields
        # fields = '__all__' #all the fields will be shown in the employee_form.html
        fields = ('storyname', 'authorname', 'content', 'content_type', 'edition', 'year') #customized fields

        #CUSTOMIZED LABELS (CRISPY_FORMS)
        labels = {
            'storyname': 'গল্পের নাম',
            'authorname': 'লেখক',
            'content': 'লিখুন',
            'content_type': 'বিভাগ',
            'edition': 'প্রকাশ সংখ্যা',
            'year': 'প্রকাশ সাল',
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'