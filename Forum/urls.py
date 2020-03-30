from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('list/', PostListView.as_view(), name='list'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete')

]
