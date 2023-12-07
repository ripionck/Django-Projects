from django import forms
from mysite.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Name',
            'email': 'Email',
            'roll': 'Roll',
            'department': 'Department'
        }
