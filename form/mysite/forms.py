from django import forms
import datetime


class contactForm(forms.Form):
    name = forms.CharField(label='User Name', initial='Rahamat Ullah')
    email = forms.EmailField(
        label='User Email', required=False, initial='rahmat@gmail.com')
    age = forms.IntegerField()
    date = forms.DateField(initial=datetime.date.today)
    BIRTH_YEAR_CHOICE = ['1995', '1997', '2010', '2023']
    year = forms.IntegerField(widget=forms.SelectDateWidget(
        years=BIRTH_YEAR_CHOICE))
    balance = forms.DecimalField()
    check = forms.BooleanField(required=False)
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5}), max_length=200)
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favourite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    SIZE_CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=SIZE_CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    meal = forms.MultipleChoiceField(
        choices=MEAL, widget=forms.CheckboxSelectMultiple)
