from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from quickstart import views

schema_view = get_schema_view(
   openapi.Info(
      title="Conectar back con front",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dany.calamateo@gmail.com",),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('OmniClass23', views.OmniClass23ViewSet)
router.register('OMC23Nivel1', views.OMC23Nivel1ViewSet)
router.register('OMC23Nivel2', views.OMC23Nivel2ViewSet)
router.register('OMC23Nivel3', views.OMC23Nivel3ViewSet)
router.register('OMC23Nivel4', views.OMC23Nivel4ViewSet)
router.register('OMC23Nivel5', views.OMC23Nivel5ViewSet)
router.register('OMC23Nivel6', views.OMC23Nivel6ViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework'))
]
