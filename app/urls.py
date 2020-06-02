from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.CDListView.as_view(), name='cd_list'),
    path('create/', views.SearchWordCreateView.as_view(), name='create'),
    path('create_done/', views.create_done, name='create_done'),
    path('word_list/', views.WordListView.as_view(), name='word_list'),
    path('update/<int:pk>/', views.WordUpdateView.as_view(), name='update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.WordDeleteView.as_view(), name='delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
    path('jan_update/', views.update_jan_info, name='jan_update'),
    
]