from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Person
from django.http import JsonResponse
from django.core.serializers import serialize
# import json
import logging

logger = logging.getLogger(__name__)

def home(request):
    # approach one
    # persons = Person.objects.all()
    # persons_json = json.loads(serialize('json', persons))
    # return JsonResponse(persons_json, safe=False)
    #return render(request,'home/home.html',context={'infos':persons})
    
    # approach otwo
    # persons = Person.objects.values('id', 'name', 'email', 'age', 'address')
    # return JsonResponse(list(persons), safe=False)
    
    
    # approach three
    # fields = [field.name for field in Person._meta.fields]

    # persons = Person.objects.values(*fields)

    # return JsonResponse(list(persons), safe=False, status=200)
    
    persons = Person.objects.all()
    return render(request,'home/home.html',context={'infos':persons})


def add_person(request):
    return render(request,'home/add-person.html')




def add_new_person(request):
    logger.info(f"Request method: {request.method}")
    if request.method == 'POST':
        logger.info(f"POST data: {request.POST}")
        name = request.POST.get('name')
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']
        person = Person(name = name, email = email, age = age, address = address)
        person.save()
        return redirect('home')
        # return redirect('/')
        
        
def edit_person(request, id):
    person = get_object_or_404(Person, pk=id)
    
    # for showing  a single object as json format
    # fields = [field.name for field in Person._meta.fields]
    # person_data = {field: getattr(person, field) for field in fields}
    # return JsonResponse(person_data, safe=False, status=201)
    print(person)
    return render(request,'home/edit-person.html',{'person': person})

 
def update_person(request,id):
    logger.info(f"Request method: {request.method}")
    if request.method == 'PUT':
        logger.info(f"PUT data: {request.PUT}")
        name = request.PUT.get('name')
        email = request.POPUTST['email']
        age = request.PUT['age']
        address = request.PUT['address']
        person = Person(name = name, email = email, age = age, address = address)
        person.update()
        return redirect('home')
        # return redirect('/')

    
def delete_person(request,id):
    person = get_object_or_404(Person,pk=id)
    person.delete()
    # return HttpResponse(f'This is id parameter {person.name}')
    return redirect('home')

def about(request):
    return render(request,'about/about.html')


def contact(request):
   return render(request,'contact/contact.html')