from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView, toggle_favorite
from . import views

urlpatterns =[
    path('', BookmarkListView.as_view(), name = 'list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    path('bookmark/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', BookmarkListView.as_view(), {'favorite': True}, name='favorite_list'),

]