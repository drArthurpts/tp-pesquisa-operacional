from django.contrib import admin
from django.urls import path
from tpPesquisaOperacionalApp.views import lista_abrigos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_abrigos),
]
