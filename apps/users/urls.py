from django.urls import path
from . import views

# 访问类视图views.类名.as_view()
urlpatterns = [
    path('usernames/<username:username>/count/', views.RegisterName.as_view()),
    path('mobiles/<mobile:mobile>/count/', views.RegisterMobile.as_view()),
    path('register/', views.Register.as_view())
]
