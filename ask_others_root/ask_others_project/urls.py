from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ask_others_app.views import RegisterView, ProfileView


schema_view = get_schema_view(
    openapi.Info(
        title="Ask Others (Swagger UI)",
        default_version='1.0.0',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ask_others_app.urls')),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('api/auth/register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redocs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
