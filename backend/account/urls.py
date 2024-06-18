from django.urls import path
from .views import RegisterView,ActivateAccountView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('activate/<uidb64>/<token>/',ActivateAccountView.as_view()),
]
