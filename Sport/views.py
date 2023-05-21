from django.shortcuts import render, get_object_or_404, redirect
from Sport.models import Statistic
from Sport.forms import SportForm, CommentForm, UserRegisterForm
import requests

from django.contrib import messages


# Create your views here.


def info(request):
    information = Statistic.objects.all()
    context = {
        'inform': information
    }
    return render(request, 'html/info.html', context)


def detail(request, id):
    informat = get_object_or_404(Statistic, pk=id)
    comments = informat.comments.all()

    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = informat
            # instance.body = 'THIS IS THE COMMENT'
            instance.save()
            form = CommentForm()
            messages.success(request, 'succesfully')

    context = {
        'informa': informat,
        'form': form,
        'comments': comments

    }
    return render(request, 'html/detail.html', context)


def publish(request):
    form = SportForm()
    if request.method == 'POST':
        form = SportForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.posted = request.user
            form.save()
            messages.success(request, 'post done successfully')
            return redirect('info')
    context = {
        'form': form
    }

    return render(request, 'html/publish.html', context)


def podelete(request, id):
    post = get_object_or_404(Statistic, id=id)
    post.delete()
    return redirect('info')


def edit_post(request, id):
    single_post = get_object_or_404(Statistic, pk=id)
    form = SportForm(request.POST or None, instance=single_post)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('info')
    context = {
        'form': form
    }
    return render(request, 'html/edit.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi, {username}, your account was created succesfully')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'html/signup.html', context)


def display_api_data(request):
    # headers = {'Authorization': 'Token f4217790d0d0c8293460718f58092d68c934f2a2'}
    # r = request.get('http://127.0.0.1:8000/sport/newapi/view/5/', headers=headers)
    response = requests.get('http://127.0.0.1:8000/sport/newapi/view/5/')
    data = response.json()
    context = {
        'data': data
    }
    return render(request, 'html/api_display.html', context)
