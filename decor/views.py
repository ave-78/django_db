from django.shortcuts import render
from django.db.models import Count
from django.http import Http404
from .models import Topic, Category

def index(request):
    topics = Topic.objects.all().annotate(Count('categories'))
    cats = Category.objects.all()
    return render(request, 'decor/index.html', context = {'topics': topics, 'categories': cats})

def topic_details(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404
    return render(request, 'decor/topic_details.html', context={'topic': topic})