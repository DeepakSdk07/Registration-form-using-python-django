from django.contrib import admin
from django.urls import path
from my_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('addData/', views.addData, name="register"),
    path('updateData/<int:id>', views.updateData, name="updateData"),
    path('deleteData/<int:id>', views.deleteData, name="deleteData"),
]
