from django.urls import path

from apps.verification import views

urlpatterns = [
    path('image_codes/<uuid:uuid>/', views.ImageCodes.as_view()),
]
