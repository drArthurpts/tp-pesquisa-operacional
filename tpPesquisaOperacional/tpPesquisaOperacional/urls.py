from django.contrib import admin
from django.urls import path
from tpPesquisaOperacionalApp.views import lista_abrigos
<<<<<<< HEAD

=======
>>>>>>> e776a994954aff1467ddd7cd1c04b4f44973bffa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_abrigos),
]
