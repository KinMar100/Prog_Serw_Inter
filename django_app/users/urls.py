from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUserListView.as_view(), name='create'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('rank/', views.RankListView.as_view(), name='rank'),
]
