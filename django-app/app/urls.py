from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from api_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='app')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/sample/', views.SampleView.as_view(), name="Samples"),
    path('api/sample/search', views.SampleSearchView.as_view(), name="Samples"),
    path('api/sample/<int:id>', views.SampleGetView.as_view(), name="Samples"),
    path('api/sample/result/<int:id>', views.SampleResultView.as_view(), name="Samples"),
]

urlpatterns += router.urls
