from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from ask_others_app.views import RegisterView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ask_others_app.urls')),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('api/auth/register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
