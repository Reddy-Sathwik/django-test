# myapp/views.py

from django.shortcuts import render
from .models import Person
from datetime import datetime

def form_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST['age'])
        dob = datetime.strptime(request.POST['dob'], "%Y-%m-%d")
        
        person = Person(name=name, age=age, dob=dob)
        person.save()

        return render(request, 'myfirstapp/form.html', {'message': 'Data saved successfully!'})

    return render(request, 'myfirstapp/form.html')
