from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('signup/',views.sign_up)
]