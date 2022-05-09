from django.shortcuts import render
from phonebook.models import Contact

# Create your views here.
from django.http import HttpResponse

def index(request):

    allContacts = Contact.objects.all()
    context = {'contacts': allContacts}

    return render(request,'index.html',context)

def addContact(request):
    print("inside add contact")
    if request.method == "POST":
        print("inside post req")
        name = request.POST['c_name']
        number = request.POST['c_no']
        print(name,number)
        ins = Contact(c_name = name, c_no= number)
        ins.save()

    return render(request,'addContact.html')