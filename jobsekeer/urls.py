
from django.urls import path,include
from jobsekeer import views as v
urlpatterns = [
    path('joblist/',v.ListAPI.as_view(),name='joblist'),
]
