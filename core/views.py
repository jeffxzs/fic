from django.shortcuts import render, redirect
from .models import Area, Publico, Curso
from .forms import AreaForm
from django.contrib.auth import login, authenticate

def autenticar(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')

def inicial(request):
    return render(request, 'index.html')

def areas(request):
    lista_areas = Area.objects.all()
    context = {
        'lista_areas': lista_areas
    }
    return render(request, 'areas.html', context)

def area_cadastro(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('areas')
    context = {
        'form':form
    }
    return render(request, 'area_cadastro.html', context)
    
def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('areas')
    context = {
        'form':form
    }
    return render(request, 'area_cadastro.html', context)

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')
