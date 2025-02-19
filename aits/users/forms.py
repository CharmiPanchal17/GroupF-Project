from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Student
        fields = ['username', 'fullname', 'student_number', 'registration_number', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        validate_password(password1)
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = make_password(self.cleaned_data["password1"])  # Hash the password
        if commit:
            student.save()
        return student
