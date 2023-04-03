from django.urls import path,include
from . import views
from django.contrib import admin



urlpatterns = [
    path('positions/', views.employee_pos, name = 'employee_pos'),
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', views.employee_form, name = 'employee_insert'),    #get and post request insert
    path('<int:id>/', views.employee_form, name = 'employee_update'),   #get and post request for update
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete'),
    path('list/', views.employee_list, name = 'employee_list')  #get request to retrieve and display all records
]





