from django.urls import path
from register import views as v

urlpatterns = [
    path('register/',v.RegisterAPI.as_view(),name='register'),
    path('login/',v.LoginAPI.as_view(),name='login'),
]
