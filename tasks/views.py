from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import slumber

def home(request, register=False):

    try:
        user_tasks = api.tasks.get()
        logged_in = True
    except:
        logged_in = False
        user_tasks = {}

    if request.POST.get('add'):
        add_task(request.POST.get('name'), request.POST.get('priority'))
        return redirect('/')

    elif request.POST.get('reg'):
        reg(request.POST.get('username'), request.POST.get('pass'), request.POST.get('email'))
        return redirect('/')

    elif request.POST.get('login'):
        login(request.POST.get('user'), request.POST.get('password'))
        return redirect('/')

    template = 'base.html'
    context = {'user_tasks':user_tasks, 'logged_in':logged_in, 'register':register}
    
    return render_to_response(template, context, context_instance=RequestContext(request))

def clear(request):
    """ Usuwa z bazy danych wykonane zadania. """

    for task in api.tasks.get()['results']:
        if task['status'] == True:
            api.tasks(task['id']).delete()

    return redirect('/')

def check(request, task_id):
    """ Zaznacza zadanie. """

    api.tasks(task_id).patch({"status": True})

    return redirect('/')

def uncheck(request, task_id):
    """ Odznacza zadanie. """

    api.tasks(task_id).patch({"status": False})

    return redirect('/')

def add_task(name, priority):
    """ Dodaje nowe zadanie. """

    if priority == "Niski":
        priority = 1
    elif priority == "Sredni":
        priority = 2
    elif priority == "Wysoki":
        priority = 3

    api.tasks.post({"name": name, "priority": priority})

def login(user, password):
    """ Loguje uzytkownika. """

    global api

    api = slumber.API("http://127.0.0.1:8000/", auth=(user, password))

def logout(request):
    """ Wylogowuje uzytkownika. """

    global api

    api = {}
    return redirect('/')

def reg(user, password, email):
    """ Rejestruje uzytkownika. """

    global api

    api = slumber.API("http://127.0.0.1:8000/", auth=("admin", "admin"))
    try:
        api.users.post({"username":user, "password":password, "email":email})
    except:
        pass
    del api
    return redirect('/')