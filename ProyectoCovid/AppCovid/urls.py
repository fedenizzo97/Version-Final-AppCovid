"""ProyectoCovid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AppCovid import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path("barbijos", views.barbijos, name= "Barbijos"),
    path("barbijosFormulario/", views.barbijosFormulario, name= "Formulario de Barbijos"),
    path("busquedaDeBarbijos", views.busquedaDeBarbijos, name=  "Busqueda de Barbijos"),
    path("buscar/", views.buscar),
    #path("guantesFormulario/", views.guantesFormulario, name= "Formulario de Guantes"),
    path("eliminarBarbijo/<marca_para_borrar>", views.eliminarBarbijo, name= "EliminarBarbijo"),
    path("editarBarbijo/<marca_para_editar>", views.editarBarbijo, name= "EditarBarbijo"),

    path("leerBarbijos",views.leerBarbijos, name= "LeerBarbijos"),
    path('barbijos/list', views.BarbijosList.as_view, name='List'),
    
    path(r'^(?P<pk>\d+)$', views.BarbijosDetalle.as_view(), name='Detail'),
    
    path('logout', LogoutView.as_view(template_name='AppCovid/logout.html'), name="Logout"),
    
    path(r'^nuevo$', views.BarbijosCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.BarbijosUpdate.as_view(), name='Edit'),
    #path(r'^borrar/(?P<pk>\d+)$', views.OximetrosDelete.as_view(), name='Delete'),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil"),
]
