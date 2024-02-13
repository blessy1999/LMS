from django import forms
from django.contrib.auth.models import User
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'isbn', 'genre', 'edition']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['enrollment','branch']

class IssuedBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Book",
                                   to_field_name="isbn", label='Book ')
    enrollment2 = forms.ModelChoiceField(queryset=models.Student.objects.all(), empty_label="Studnet",
                                         to_field_name='enrollment', label='Student')

