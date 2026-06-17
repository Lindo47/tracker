from django.contrib import admin
from django.urls import path
from tracker import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.device_list, name='device_list'),
    
    path('delete/<int:device_id>/', views.delete_device, name='delete_device'),
]