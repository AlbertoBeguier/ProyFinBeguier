from django.shortcuts import render,redirect
# importamos el modelo

from django.http import HttpResponse,HttpRequest
from .models import Avatar

#AVATARES 
def def_inicio(request):
    try:
        avatar=Avatar.objects.get(user=request.user.id)
        return render(request,  "Inicio.html",{"url_avatar": avatar.imagen.url} )
    except:
        return render(request, "Inicio.html")




#def def_inicio(request):
 #   return render (request, "Inicio.html")

def def_bienvenida(request):
    return render (request, "bienvenida.html")

def def_CRUDInformes(request):
    return render (request, "CRUDInformes.html")

def def_LECTInformes(request):
    return render (request, "LECTInformes.html")

# def def_login(request):
#    return render (request, "login.html")

def def_planesYprecios(request):
    return render (request, "planesYprecios.html")

def def_quienesSomos(request):
    return render (request, "quienesSomos.html")

def def_politicas(request):
    return render (request, "politicas.html")

def def_registrarse(request):
    return render (request, "registrarse.html")

from .forms import InformeFormulario

from .models import Informe, Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class InformeList(ListView):
    model=Informe
    template_name= "InformeList.html"
    context_object_name="id_informe"

class InformeList1(ListView):
    model=Informe
    template_name= "InformeList1.html"
    context_object_name="id_informe"

class InformeList2(ListView):
    model=Informe
    template_name= "InformeList2.html"
    context_object_name="id_informe"

class InformeList3(ListView):
    model=Informe
    template_name= "InformeList3.html"
    context_object_name="id_informe"


class InformeDetail(DetailView):
    model=Informe
    template_name= "InformeDetail.html"
    context_object_name="id_informe"
    


class InformeCreate (CreateView):
    # modelo vinculado 
    model = Informe
    # template donde se renderizará 
    template_name = "InformeCreate.html"
    # para que aparezcan todos los campos 
    fields = ("__all__")
    success_url = "/AppGeneral"
    
class InformeUpdate(UpdateView):
    model= Informe
    template_name = "InformeUpdate.html"
    fields=("__all__")
    success_url = "/AppGeneral/InformeList"
    context_object_name = "id_informe"

class InformeDelete (DeleteView):
    model = Informe
    template_name = "InformeDelete.html"
    context_object_name = "id_informe"
    success_url = "/AppGeneral/InformeList"
    



def def_InformeFormulario(request):
    
    if request.method == "POST":
        # proceso los datos del formulario
        miFormulario=InformeFormulario(request.POST)
        
        # si el formulario es válido
        if miFormulario.is_valid():
            # accedo a los datos ingresados en el formulario 
            # luego de que fueron validados y procesados 
            # y se los almacena en la variable data
            data=miFormulario.cleaned_data
            # instancio un objeto tipo informe 
            informe=Informe(tipo=data["tipo"],titulo=data["titulo"],
            subtitulo=data["subtitulo"], fecha=data["fecha"],contenido=data["contenido"])
            # grabo los datos del informe  
            informe.save()
        return render (request, "Inicio.html", {"mensaje": "El informe fué creado correctamente"})
    else:
        # si recibo un método get
        miFormulario = InformeFormulario()
        return render (request, "InformeFormulario.html", {"miFormulario":miFormulario})
    
    
 # USUARIOS   -----------  LOGIN
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def def_loginView(request):
    if request.method =='POST':
        miFormulario = AuthenticationForm(request, data=request.POST)
        
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            usuario= data["username"]
            psw=data["password"]
            user=authenticate(username=usuario, password=psw)
            if user:
                login(request,user)
                #return render(request, "Inicio.html")
                return redirect ("Inicio")
        return render (request, "Inicio.html",{"mensaje": f"Datos incorrectos !"})
    else:
        miFormulario = AuthenticationForm()
        return render (request, "login.html", {"miFormulario":miFormulario})
    
     
 # USUARIOS   -----------  REGISTRAR
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def def_registar_usuario(request):
    
    if request.method =='POST':
        
        miFormulario = UserCreationForm(request.POST)
        
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            usuario= data["username"]
            miFormulario.save()
            return render(request, "Inicio.html",{"mensaje": f"Bienvenido {usuario} !"})
        
        return render (request, "Inicio.html",{"mensaje": f"Formulario inválido !"})
    else:
        miFormulario = UserCreationForm()
        return render (request, "registrarse.html", {"miFormulario":miFormulario})


# ENVIAR email
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

def def_contactenos(request):
    return render (request, "contactenos.html")

def def_contacto(request):
      if request.method =='POST':
       name=request.POST["name"] 
       email=request.POST["email"] 
       subject=request.POST["subject"]
       message=request.POST["message"]
       
       template= render_to_string("email_template.html", {
           'name':name,
           'email':email,
           'message':message,
           
       })
       
       email = EmailMessage(
           subject,
           template,
           settings.EMAIL_HOST_USER,
           ["pythoncondjango@gmail.com"])
       
       email.fail_silently = False
       email.send()
       
       messages.success(request, 'Se ha enviado el mensaje con éxito')
       return redirect ('contactenos')
   
