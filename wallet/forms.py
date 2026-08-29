from django import forms

class TopUpForm(forms.Form):

    amount = forms.DecimalField(max_digits=10,decimal_places=2,min_value=1.00,

    widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter amount (e.g. 50.00)', 'step': '0.01'})

    )


