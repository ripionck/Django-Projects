from django import forms
import datetime
from django.core import validators


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


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")


class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(
        10, message='Enter a name with at least 10 characters')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[
                            validators.EmailValidator(message="Enter a valid Email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(
        34, message="age must be maximum 34"), validators.MinValueValidator(24, message="age must be at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(
        allowed_extensions=['pdf', 'png'], message='File Extension must be ended with .pdf')])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")
