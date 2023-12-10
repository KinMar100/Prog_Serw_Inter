from django.urls import path, include
from rest_framework import routers
from . views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

app_name = 'posts'

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]