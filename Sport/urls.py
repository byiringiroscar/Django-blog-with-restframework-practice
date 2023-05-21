from django.urls import path, re_path
from .import views
from django.contrib.auth import views as auth_view
...
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

name = 'Sport'

urlpatterns = [
    # django documentation with swagger
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', views.info, name='info'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('publish', views.publish, name='publish'),
    path('delete/<int:id>/', views.podelete, name='podelete'),
    path('edit-post/<int:id>', views.edit_post, name='edit_post'),
    path('login/', auth_view.LoginView.as_view(template_name='html/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout', auth_view.LogoutView.as_view(), name='logout'),
    path('display_api', views.display_api_data, name='display_api_data'),
]