from django.contrib import admin
from django.urls import path, include

from app1.views import (
    CategoryListCreateView, 
    CategoryDetailView, 
    MenuItemListCreateView, 
    MenuItemDetailView,
    RegisterView
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Mening API Loyiham",
      default_version='v1',
      description="Loyiha uchun API hujjatlari va CRUD",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app1.urls')),
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('api/menu-items/', MenuItemListCreateView.as_view(), name='menu-item-list'),
    path('api/menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]