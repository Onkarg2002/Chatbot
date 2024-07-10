from django.urls import path
from .views import index, send_query

urlpatterns = [
    path('', index, name='index'),
    path('send_query/', send_query, name='send_query'),
]
