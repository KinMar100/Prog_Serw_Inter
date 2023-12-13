from django.urls import path, include
from rest_framework import routers
from . views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'add_post', PostViewSet)
router.register(r'add_comment', CommentViewSet)

app_name = 'posts'

urlpatterns = [
    path('api/', include(router.urls)),
]
