from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        # fields = '__all__' #all the fields will be shown in the employee_form.html
        fields = ('name', 'email') #customized fields

        #CUSTOMIZED LABELS (CRISPY_FORMS)
        labels = {
            'name': 'আপনার নাম (দয়া করে ইংরেজিতে লিখুন)',
            'email': 'আপনার ইমেইল',
        }