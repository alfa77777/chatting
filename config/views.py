from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

def custom_logout(request):
    auth_views.auth_logout(request)
    return redirect('schema-swagger-ui')
