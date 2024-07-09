from django.contrib import admin
from django.urls import path
from tpPesquisaOperacionalApp.views import lista_abrigos, alocar_desabrigados


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_abrigos, name='lista_abrigos'),
    path('alocar/', alocar_desabrigados, name='alocar'),
]
