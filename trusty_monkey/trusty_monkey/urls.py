from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django_registration.backends.one_step.views import RegistrationView
from core.views import IndexTemplateView, DummyView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegistrationView.as_view(
                                success_url='/'),
                                name='django_registration_register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('users.api.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('places.api.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    re_path(r"^(?!media).*$", IndexTemplateView.as_view(), name="entry-point")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
