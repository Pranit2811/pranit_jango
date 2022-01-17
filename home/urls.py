from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('form', views.form,name='form'),
    path('sign_in', views.sign_in,name='sign_in'),
    path('logoutuser', views.logoutuser,name='logoutuser'), 
    path('delete/<int:id>/', views.delete,name='delete'),
    path('update/<int:id>/', views.update,name='update'),
]