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

    template = 'base.html'
    context = {'user_tasks':user_tasks, 'logged_in':logged_in, 'register':register}
    
    return render_to_response(template, context, context_instance=RequestContext(request))

def clear(request):
    """ Usuwa z bazy danych wykonane zadania. """

    for task in api.tasks.get()['results']:
        if task['status'] == True:
            # DELETE 127.0.0.1:8000/tasks/1/ -a user:user
            api.tasks(task['id']).delete()

    return redirect('/')


def check(request, task_id):
    """ Zaznacza zadanie. """

    # PATCH 127.WW0.0.1:8000/tasks/1/ status="true" -a user:user
    api.tasks(task_id).patch({"status": True})

    return redirect('/')


def uncheck(request, task_id):
    """ Odznacza zadanie. """

    # PATCH 127.0.0.1:8000/tasks/1/ status="false" -a user:user
    api.tasks(task_id).patch({"status": False})

    return redirect('/')


def add_task(request):
    """ Dodaje nowe zadanie. """

    name, priority = request.POST.get('name'), request.POST.get('priority')

    if priority == "Niski":
        priority = 1
    elif priority == "Sredni":
        priority = 2
    elif priority == "Wysoki":
        priority = 3

    #  POST 127.0.0.1:8000/tasks/ name="task" priority="1" -a user:user
    api.tasks.post({"name": name, "priority": priority})

    return redirect('/')


def login(request):
    """ Loguje uzytkownika. """

    global api

    user, password = request.POST.get('user'), request.POST.get('password')

    # GET 127.0.0.1:8000 -a user:password
    api = slumber.API("http://127.0.0.1:8000/", auth=(user, password))

    return redirect('/')


def logout(request):
    """ Wylogowuje uzytkownika. """

    global api

    api = {}

    return redirect('/')


def reg(request):
    """ Rejestruje uzytkownika. """

    global api

    user, password, email = request.POST.get('username'), request.POST.get('pass'), request.POST.get('email')

    # GET 127.0.0.1:8000 -a user:password
    api = slumber.API("http://127.0.0.1:8000/", auth=("admin", "admin"))

    try:
        # POST 127.0.0.1:8000/users/ username="user" password="password" email="email"
        api.users.post({"username":user, "password":password, "email":email})
        del api
        return redirect('/success/')
    except:
        del api
        return redirect('/error/')


def success(request):
    """ Simple registration success page. """

    template = 'registration/success.html'
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))


def error(request):
    """ Simple registration error page. """

    template = 'registration/error.html'
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))
