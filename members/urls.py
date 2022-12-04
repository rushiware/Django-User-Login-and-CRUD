from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfirst,name="myfirst"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('index/',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('index/add/',views.add,name="add"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    path('index/update/<int:id>',views.update,name="update"),
    path('index/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
