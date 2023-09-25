from django.contrib import admin

# Register your models here.
from .models import Informe, Avatar

admin.site.register(Informe)
admin.site.register(Avatar)

admin.site.site_header = "Panel de Administración CONSULTING S.A."

