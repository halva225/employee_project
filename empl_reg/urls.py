from django.urls import path,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    #reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
    ##
    path('positions/', views.employee_pos, name = 'employee_pos'),
    path('admin/', admin.site.urls),

    path('', views.employee_form, name = 'employee_insert'),    #get and post request insert
    path('<int:id>/', views.employee_form, name = 'employee_update'),   #get and post request for update
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete'),
    path('list/', views.employee_list, name = 'employee_list')  #get request to retrieve and display all records
]


