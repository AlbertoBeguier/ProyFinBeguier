from django.urls import path
from AppGeneral.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
     # no se pone nada entre las comillas así siempre lee el inicio
    path('', def_inicio, name="Inicio"), 
    #path('InformeFormulario/', def_InformeFormulario,name="InformeFormulario"),
    path('InformeCreate/', InformeCreate.as_view(),name="InformeCreate"),
    path('quienesSomos/', def_quienesSomos, name="quienesSomos"), 
    path('politicas/', def_politicas, name="politicas"), 
    path('CRUDInformes/', def_CRUDInformes, name="CRUDInformes"), 
    path('LECTInformes/', def_LECTInformes, name="LECTInformes"), 
    path('contactenos/', def_contactenos, name="contactenos"), 
    path('login/', def_loginView, name="login"), 
    path('registrarse/', def_registar_usuario, name="registrarse"), 
    path('planesYprecios/', def_planesYprecios, name="planesYprecios"), 
    path('bienvenida/', def_bienvenida, name="bienvenida"), 
    path('logout', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('InformeDetail/<pk>', InformeDetail.as_view(),name="InformeDetail"),
    path('InformeDelete/<pk>', InformeDelete.as_view(),name="InformeDelete"),
    path('InformeUpdate/<pk>', InformeUpdate.as_view(),name="InformeUpdate"),
    path('InformeList/', InformeList.as_view(),name="InformeList"),
    path('InformeList1/', InformeList1.as_view(),name="InformeList1"),
    path('InformeList2/', InformeList2.as_view(),name="InformeList2"),
    path('InformeList3/', InformeList3.as_view(),name="InformeList3"),
    path('contacto/', def_contacto,name="contacto"),
    
]

