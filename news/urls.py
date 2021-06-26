from django.urls import path

from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('view_by_category/<int:category_id>/', views.view_by_category, name='view_by_category'),
    path('rate_news/<int:pk>', views.rate_news, name='rate_news'),
    path('add_news/', views.add_news, name='add_news'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('view_news/<int:news_id>/', views.view_news, name='view_news'),
    path('user/<int:pk>/', views.user, name='user'),
    path('', views.UserView.as_view(), name='index'),
    path('search/', views.search, name='search'),
]

