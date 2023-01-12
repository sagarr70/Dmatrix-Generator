from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('saveexcel',views.saveexcel,name='excel_file')
]

