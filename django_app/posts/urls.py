from django.urls import path, include
from rest_framework import routers

from . views import PostViewSet, PostNewestViewSet, CommentViewSet, ReactionViewSet

router = routers.DefaultRouter()
router.register(r'add_post', PostViewSet)
router.register(r'add_comment', CommentViewSet)
router.register(r'add_reaction', ReactionViewSet)

app_name = 'posts'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('newest_posts/', PostNewestViewSet.as_view(), name='newest_posts')
]
