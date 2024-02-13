from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import forms,models
def home_view(request):
    return render(request,'index.html')

def is_admin(user):
    if user.is_superuser or user.is_staff:
        return True
    else:
        return False

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request, 'adminafterlogin.html')
    elif (is_student(request.user)):
        return render(request, 'studentafterlogin.html')

def studentsignup_view(request):
    form1 = forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    mydict = {'form1':form1,'form2':form2}
    if request.method == 'POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'studentsignup.html',context=mydict)


@login_required(login_url='adminlogin')
def addbook_view(request):
    form = forms.BookForm()
    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,'bookadded.html')
    return render(request,'addbook.html',{'form':form})

@login_required(login_url='adminlogin')
def viewbook_view(request):
    books = models.Book.objects.all()
    return render(request,'viewbook.html',{'books':books})

@login_required(login_url='adminlogin')
def issuebook_view(request):
    form=forms.IssuedBookForm()
    if request.method == 'POST':
        form=forms.IssuedBookForm(request.POST)
        if form.is_valid():
            obj = models.IssuedBook()
            obj.enrollment = request.POST.get('enrollment2')
            obj.isbn=request.POST.get('isbn2')
            obj.save()
            return render(request,'bookissued.html')
    return render(request,'issuebook.html',{'form':form})

@login_required(login_url='adminlogin')
def viewissuedbook_view(request):
    issuedbooks=models.IssuedBook.objects.all()
    li=[]
    for ib in issuedbooks:
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        books=list(models.Book.objects.filter(isbn=ib.isbn))
        students=list(models.Student.objects.filter(enrollment=ib.enrollment))
        i=0
        for l in books:
            t=(students[i].get_name,students[i].enrollment,books[i].title,books[i].author,issdate,expdate,fine,ib.status)
            i=i+1
            li.append(t)
    return render(request,'viewissuedbook.html',{'li':li})

@login_required(login_url='adminlogin')
def viewstudent_view(request):
    students = models.Student.objects.all()
    return render(request,'viewstudent.html',{'students':students})

@login_required(login_url='studentlogin')
def viewissuedbookbystudent(request):
    student=models.Student.objects.filter(user_id=request.user.id)
    issuedbook=models.IssuedBook.objects.filter(enrollment=student[0].enrollment)
    li1=[]
    li2=[]
    for ib in issuedbook:
        books=models.Book.objects.filter(isbn=ib.isbn)
        for book in books:
            t=(request.user,student[0].enrollment,student[0].branch,book.title,book.author)
            li1.append(t)
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        t=(issdate,expdate,fine,ib.status,ib.id)
        li2.append(t)
    return render(request,'viewissuedbookbystudent.html',{'li1':li1,'li2':li2})

def returnbook(request, id):
    issued_book = models.IssuedBook.objects.get(pk=id)
    issued_book.status = "Returned"
    issued_book.save()
    return redirect('viewissuedbookbystudent')

def aboutus_view(request):
    return render(request,'about.html')
