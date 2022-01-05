from django.shortcuts import render
from django.http import HttpResponse

from AppCovid.models import Barbijos
from AppCovid.forms import BarbijosFormulario, UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request, "AppCovid/inicio.html")


def barbijos(request):
    
    return render(request, "AppCovid/barbijos.html")



def barbijosFormulario(request):
    if request.method == "POST":

        miFormulario = BarbijosFormulario(request.POST)
        
        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            barbijoInst= Barbijos(marca= informacion["marca"], tamanio= informacion["tamanio"], precio= request.POST ["precio"])

            barbijoInst.save()  

            return render(request,"AppCovid/inicio.html")

    else:

        miFormulario = BarbijosFormulario()

    return render(request, "AppCovid/barbijosFormulario.html", {"miFormulario": miFormulario})

def busquedaDeBarbijos(request):

    return render(request, "AppCovid/busquedaDeBarbijos.html")


def buscar(request):

    if request.GET["marca"]:
        
        marca= request.GET["marca"]

        barbijo= Barbijos.objects.filter(marca__icontains= marca)

    #respuesta= f"Estoy buscando a: {request.GET['marca']}"
        return render(request, "AppCovid/resultadoBusqueda.html", {"barbijo": barbijo, "marca":marca})
    else: 
        respuesta= "Por favor mandame mas informacion, sino no puedo ayudarte"
    return HttpResponse(respuesta)


@login_required
def leerBarbijos(request):

    barbijo= Barbijos.objects.all()

    diccionario1= {"barbijo": barbijo}
    
    return render(request, "AppCovid/leerBarbijos.html",diccionario1)




def eliminarBarbijo(request, marca_para_borrar ):

    barbijoQueQuieroBorrar = Barbijos.objects.get( marca= marca_para_borrar)

    barbijoQueQuieroBorrar.delete()

    barbijo =Barbijos.objects.all()

    return render(request, "AppCovid/leerbarbijos.html", {"barbijo": barbijo})

def editarBarbijo(request, marca_para_editar):

    barbijAEditar= Barbijos.objects.get(marca=marca_para_editar)

    if request.method == "POST":

            miFormulario = BarbijosFormulario(request.POST)
            
            if miFormulario.is_valid():

                informacion3= miFormulario.cleaned_data

            
                barbijAEditar.marca= informacion3["marca"]
                barbijAEditar.tamanio= informacion3["tamanio"]
                barbijAEditar.precio= informacion3["precio"]
                

                barbijAEditar.save()

                return render(request,"AppCovid/inicio.html")

    else:

        miFormulario = BarbijosFormulario(initial={"marca": barbijAEditar.marca, "tamanio": barbijAEditar.tamanio, "precio": barbijAEditar.precio})

    return render(request, "AppCovid/editarBarbijo.html", {"miFormulario": miFormulario, "barbijAEditar": barbijAEditar})


class BarbijosList(ListView):
    
    model = Barbijos
    template_name = "AppCovid/babrijos_list.html"
    
#Detalle - SUPER Leer - Buscar!!!!!
class BarbijosDetalle(DetailView):
    
    model = Barbijos
    template_name = "AppCovid/babrijos_detalle.html"
    
#Crear elementos
class BarbijosCreacion(CreateView):
    
    model = Barbijos
    success_url = "../babrijos/list"  #AppCovid/template/AppCoder/editar
    fields = ["marca", "origen", "precio"]
    
#modificar!!!!!!!!!!!  
class BarbijosUpdate(UpdateView):
    
    model = Barbijos
    success_url = "../babrijos/list"
    fields = ["marca", "origen", "precio"]
  
#Borrar   
class BarbijosDelete(DeleteView):
    
    model = Barbijos
    success_url = "../babrijos/list"

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppCovid/inicio.html", {"mensaje":f"BIENVENIDO AL PORTAL, {usuario}!!!!"})
                
            else:
                
                return render(request, "AppCovid/inicio.html", {"mensaje":f"DATOS INCORRECTOS"})
                
            
        else:
            
            return render(request, "AppCovid/inicio.html", {"mensaje":f"Formulario Erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCovid/login.html", {"form":form} )


def register(request):

    if request.method == "POST":
        #form= UserCreationForm(request.POST)
        form= UserRegisterForm(request.POST)

        if form.is_valid():

            username= form.cleaned_data["username"]

            form.save()

            return render(request, "AppCovid/inicio.html" ,{"mensaje": f"{username} Creado y Registrado"})

    else:
        form = UserRegisterForm()
        #form= UserCreationForm()
    return render(request, "AppCovid/register.html" , {"form": form})


@login_required
def editarPerfil(request):

    usuario= request.user

    if request.method == "POST":

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            usuario.email= informacion["email"]
            usuario.password1= informacion["password1"]
            usuario.password2= informacion["password2"]

            usuario.save()

            return render(request, "AppCovid/inicio.html")

    else:

        miFormulario= UserEditForm(initial=({"email": usuario.email}))

    return render(request, "AppCovid/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
