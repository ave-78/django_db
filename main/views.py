from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from .forms import Form1
from .models import Person

@require_http_methods(["POST", "GET"])
def index(request):
    people = Person.objects.all()
    if request.method == 'POST':
        gotten_form = Form1(request.POST)
        if gotten_form.is_valid():
            fields = gotten_form.cleaned_data
            return HttpResponse(f'<p> {fields} </p>')
        else:
            return HttpResponse('Invalid data')
    else:
        form = Form1(field_order = ['name', 'age'])
        return render(request, 'index.html', {'form': form, 'people': people})

@require_http_methods(["POST",])
def create(request):
    p = Person()
    p.name = request.POST.get('name', 'fail')
    p.age = request.POST.get('age', 'fail')
    p.save()
    return HttpResponseRedirect('/persons/')

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/persons/')
        else:
            return render(request, 'main/edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/persons/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

def person(request):
    people = Person.objects.all()
    return render(request, 'main/persons.html', {'people': people})


def main(request):
#    data = {'header': 'Wellcome body', 'message': 'Glad to see you' }
    header = "Personal Data"
    langs = ["English", "German", "Spanish"]
    user = {"name": "Tom", "age": 23}
    addr = ("Абрикосовая", 23, 45)
    data = {'header': header, 'langs': langs, 'addr': addr, 'user': user}
    return render(request, 'main/home.html', context=data)

def main1(request):
    return TemplateResponse(request, 'main/home1.html')

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, product_id = 1):
    category = request.GET.get('cat', 'no such category')
    result = f'<H2>Product № {product_id} Category: {category}</H2>'
    return HttpResponse(result)

def users(request, id = 1, name = 'Alex'):
    result = f'<H2>User:</H2><H3> {id} name: {name}</H3>'
    return HttpResponse(result)