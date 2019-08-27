from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views.generic.edit import CreateView
from datetime import datetime
from django.db.models import Q, Count, Avg
from pytz import UTC
from .models import User, Blog, Topic
from .forms import FormCreateUser, FormCreateBlog, FormCreateTopic

#class CreateTopic(CreateView):
#    template_name =

def report(request):
    people = User.objects.all()
    topics = Topic.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'db_test/report.html', {
        'people': people,
        'blogs': blogs,
        'topics': topics,
    })

def create_user(request):
    p = User()
    p.first_name = request.POST.get('first_name')
    p.last_name = request.POST.get('last_name')
    p.save()
    return HttpResponseRedirect(reverse('db_test:report'))

def create_blog(request):
    try:
        title = request.POST.get('title')
        user = User.objects.get(first_name=request.POST.get('author'))
        Blog.objects.create(title = title, author = user)
        return HttpResponseRedirect(reverse('db_test:report'))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('db_test:report'))

def create_topic(request):
    try:
        title = request.POST.get('title')
        user = User.objects.get(first_name=request.POST.get('author'))
        blog = Blog.objects.get(author=user, title=request.POST.get('blog'))
        Topic.objects.create(title = title, author = user, blog = blog)
        return HttpResponseRedirect(reverse('db_test:report'))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('db_test:report'))

def create_topic2(request):
    topic_form = FormCreateTopic(request.POST)
    if topic_form.is_valid():
        topic_form.save()
        return HttpResponseRedirect(reverse('db_test:report'))
    else:
        return render(request, 'db_test/show.html')

def subscribe_user(request):
    subscribers = request.POST.get('subscribers')
    blog_id = request.POST.get('id')
    blog = Blog.objects.get(id=blog_id)
    for sub in subscribers.split(','):
        user = User.objects.get(first_name=sub)
        blog.subscribers.add(user)
    blog.save()
    return HttpResponseRedirect(reverse('db_test:report'))


def like(request):
    users = request.POST.get('likes')
    topic = Topic.objects.get(id=request.POST.get('id'))
    users_obj = []
    for u in users.split(','):
        users_obj.append(User.objects.get(first_name=u))
    topic.likes.add(*users_obj)
    topic.save()
    return HttpResponseRedirect(reverse('db_test:report'))


def delete_user(request, id):
    User.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('db_test:report'))

def delete_blog(request, id):
    Blog.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('db_test:report'))

def delete_topic(request, id):
    Topic.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('db_test:report'))


def edit_users(request):
    fn = request.POST.get('first_name')
    #ln = request.POST.get('last_name')
    if fn and '|' in fn:
        first_field = fn.split('|')
        edit_users_field(first_field)
    #if ln and '|' in ln:
    #    last_field = ln.split('|')
    #    edit_users_field(last_field)
    return HttpResponseRedirect(reverse('db_test:report'))

def edit_users_field(field):
    if field[0] == '*':
        users = User.objects.all()
        edit_users_sub(users, field[1])
    elif ',' in field[0]:
        users = User.objects.all().filter(first_name__in = field[0].split(','))
        edit_users_sub(users, field[1])
    else:
        users = [User.objects.filter(first_name=field[0]).first()]
        if users[0] is not None:
            edit_users_sub(users, field[1])

def edit_users_sub(users, replacement):
    for user in users:
        user.first_name = replacement
        user.save()

def unsubscribe_user(request):
    user = request.POST.get('first_name')
    blog = request.POST.get('title')
    if user and blog:
        target_blog = Blog.objects.filter(title = blog).first()
        target_user = User.objects.filter(first_name=user).first()
        target_blog.subscribers.remove(target_user)
    return HttpResponseRedirect(reverse('db_test:report'))

# Доделать
def calculations(request):
    title = request.POST.get('title')
    topics_per_blog = {}
    topic_to_blog = {}
    topic = Topic.objects.all()
    blogs = Blog.objects.all()
    users = User.objects.all()
    topic_end = topic.filter(title__endswith=title)
    topic_count = topic.count()
    for blog in blogs:
        topics_per_blog[blog] = Topic.objects.filter(blog_id=blog.id)
    return  HttpResponseRedirect(reverse('db_test:report'))

def show(request):
    users_last2 = User.objects.order_by('-id')[:2]
    topics_per_blog = Blog.objects.annotate(topic_count=Count('topic')).order_by('topic_count')
    context = {}
    return render(request, 'db_test/show.html', context)



def get_topic_title_ended():
    pass


def get_user_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
