from django.urls import path
from . import views

# 访问类视图views.类名.as_view()
urlpatterns = [
    path('users/register', views.Register.as_view())
]
