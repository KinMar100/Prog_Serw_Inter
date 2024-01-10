from django.urls import path, include
from rest_framework import routers
from . views import QuestionViewSet, ChoiceViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
