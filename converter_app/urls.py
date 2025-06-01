# Este arquivo define as URLs específicas para o aplicativo converter_app.

from django.urls import path
from . import views

app_name = 'converter_app'

urlpatterns = [
    path('', views.converter_view, name='converter_page'), # ESTA LINHA é importante
]