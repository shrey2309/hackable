from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

from .models import Todo_safe, Todo_unsafe, user
from .forms import Todosafeform, Todounsafeform, userform


def safe(request):
    todofrom = Todosafeform
    sendform = todofrom(request.POST)

    if request.method == 'POST':
        if sendform.is_valid():
            sendform.save()

    query = Todo_safe.objects.all()
    return render(request, 'safe.html', {'data':query, "form": sendform})

def unsafe(request):
    todofrom = Todounsafeform
    sendform = todofrom(request.POST)

    if request.method == 'POST':
        if sendform.is_valid():
            sendform.save()

    query = Todo_unsafe.objects.all()
    return render(request, 'unsafe.html', {'data':query, "form": sendform})

def sqlsafe(request):
    data = userform
    instance = data(request.POST)

    if request.method == 'POST':
        if instance.is_valid():
            username = instance.cleaned_data['username']
            password =instance.cleaned_data['password']

            if user.objects.filter(username =username, password = password):
                return HttpResponse('login')
    return render(request, 'sqlinjectiosafe.html', {'form':instance})

def sqlunsafe(request):
    data = userform
    instance = data(request.POST)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        sqlquery = "SELECT * FROM check_user WHERE  username='"+ username+ "' AND password='"+password +"' "
        cursor = connection.cursor()
        cursor.execute(sqlquery)

        res = cursor.fetchone()        
        if res is not None:
            return HttpResponse('login')

    return render(request, 'sqlinjection.html', {'form':instance})