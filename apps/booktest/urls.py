from django.urls import path

from apps.booktest import views

urlpatterns = [
    path('booktest', views.BookView.as_view()),
]
