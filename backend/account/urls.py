from django.urls import path
from .views import RegisterView,ActivateAccountView,LoginObtainPairView,StaffTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', LoginObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view()),
    path('activate/<uidb64>/<token>/',ActivateAccountView.as_view()),
    path('admin/login/',StaffTokenObtainPairView.as_view()),
]
