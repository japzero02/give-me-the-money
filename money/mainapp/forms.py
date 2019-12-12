from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_id', 'first_name', 'last_name', 'january',
                  'february', 'march', 'april', 'may',
                  'june', 'july', 'august', 'september',
                  'october', 'november', 'december', 'issues')
        widgets = {
            'student_id': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'january': forms.Select(attrs={'class':'form-control'}),
            'february': forms.Select(attrs={'class':'form-control'}),
            'march': forms.Select(attrs={'class':'form-control'}),
            'april': forms.Select(attrs={'class':'form-control'}),
            'may': forms.Select(attrs={'class':'form-control'}),
            'june': forms.Select(attrs={'class':'form-control'}),
            'july': forms.Select(attrs={'class':'form-control'}),
            'august': forms.Select(attrs={'class':'form-control'}),
            'september': forms.Select(attrs={'class':'form-control'}),
            'october': forms.Select(attrs={'class':'form-control'}),
            'november': forms.Select(attrs={'class':'form-control'}),
            'december': forms.Select(attrs={'class':'form-control'}),
            'issues': forms.TextInput(attrs={'class':'form-control'}),
        }
        