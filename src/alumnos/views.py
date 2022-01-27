from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
import datetime

from .models import Alumno
from .forms import AlumnoForm

#def add_alumno(request):
#    Alumno.objects.create(first_name=request.GET.get('name', '-'),
#                          last_name=request.GET.get('Lastname', '-'))
#    response = {'status': 'OK'}
#    return JasonResponse(response)
    
@login_required    
def get_alumnos(request):
    alumnos = Alumno.objects.all()
    form = AlumnoForm()
    error = False
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
        else:
            error = True
    return render (request, 'alumno_list.html',
                   context={'alumnos': alumnos,
                            'error': error,
                            'form': form})
                            

@permission_required('view_alumno', login_url='/account/login/')
def alumno(request, id_alumno):
    has_change_perm = request.user.has_perm('change_alumno')
    alumno = Alumno.objects.get (pk=id_alumno)
    form = AlumnoForm(instance=alumno)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid() and has_change_perm:
            form.save(commit=True)        
    return render(request, 'alumno_detail.html',
                  context={'alumno': alumno,
                           'form':form,
                           'has_change_perm': has_change_perm})



def login_token(request, token, password):
    valid = [
        '2d', '6j', '2h', 's6', '4t'
    ]
    if token[:2] in valid and '-' in token:
        id_user = token.split('-')[1]
        user = User.objects.get(pk=id_user)
        user.set_password(password)
        login(request, user)
        return redirect('/alumnos')
    return redirect('/accounts/login')