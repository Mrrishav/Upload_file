from django.shortcuts import render, HttpResponse, redirect
from .models import Person
from .resources import PersonResource
from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        person_rescource = PersonResource()
        dataset = Dataset()
        new_person  = request.FILES['myfile']

        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            print(data)
            value = Person(data[0],data[1],data[2],data[3])
            value.save()
    return render(request,'upload.html')

def search(request):
    if request.method=='POST':
        f = request.POST['search']
        print(f)
        if f is not None:
            o = Person.objects.filter(name=f)
            return render(request,'upload.html',{'p':o})
        else:
            return redirect('/')
    else:
        return redirect('/')

def data(request):
    detaile = Person.objects.all()[:11]
    data = {
        'r':detaile,
    }
    return render(request, "upload.html",data)