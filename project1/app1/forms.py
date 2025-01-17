from django import forms
from .models import Student

gender_choices = [
    ('','Select Choices'),
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHER')
]
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'roll': 'Roll No',
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'marks': 'Marks',
            'city': 'City',
            'gender': 'Gender',
            'mail': 'E-Mail',
            'address': 'Address',
            'dob': 'Date_Of_Birth',
            'password': 'Password'
        }
        widgets = {
            'roll':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'E.g.,1',
            }),
            'f_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'E.g.,Joe'
            }),
            'l_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'E.g.,Biden',
            }),
            'marks':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'E.g.,90.34'
            }),
            'city':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'E.g.,Mumbai',
            }),
            'gender':forms.Select(choices=gender_choices,attrs={
                'class':'form-control'
            }),
            'mail':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'youremail@gmail.co.in'
            }),
            'address':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Maharashtra,Mumbai',
                'rows':'3'
            }),
            'dob':forms.DateInput(attrs={
                'class':'form-control',
                'type':'date'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control',
            })
        }