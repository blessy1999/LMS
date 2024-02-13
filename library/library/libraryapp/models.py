from django.contrib.auth.models import User
from django.db import models
from datetime import datetime,timedelta


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='book_covers', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

def get_expiry():
    return datetime.today() + timedelta(days=15)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.user.first_name)

    def get_name(self):
        return self.user.first_name

class IssuedBook(models.Model):
     enrollment=models.CharField(max_length=30)
     isbn=models.CharField(max_length=30)
     issuedate=models.DateField(auto_now=True)
     expirydate=models.DateField(default=get_expiry)
     statuschoice= [
         ('Issued', 'Issued'),
         ('Returned', 'Returned'),
     ]
     status=models.CharField(max_length=20,choices=statuschoice,default="Issued")

     def __str__(self):
        return self.enrollment
