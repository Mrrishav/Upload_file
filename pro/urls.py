from django.urls import path
from . import views

urlpatterns = [
    path('',views.simple_upload,name="sample_upload"),
    path('data/', views.data, name='data'),
    path('detail/', views.search, name='search'),
]
