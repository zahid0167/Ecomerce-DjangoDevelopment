from django import forms
from App_payment.models import BillingAddress

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields =('addresh', 'zipcode', 'city', 'country',)