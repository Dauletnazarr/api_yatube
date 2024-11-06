from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import path, include
from .views import PostViewSet, GroupViewSet, comments, comment_detail

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', comments, name='post-comments'),
    path('posts/<int:post_id>/comments/<int:comment_id>/',
         comment_detail, name='comment-detail'),
    path('api-token-auth/', views.obtain_auth_token),
]
