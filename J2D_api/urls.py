from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from J2D_api import views
from rest_framework.authtoken import views as token_view

urlpatterns = [
    path('get/', views.UserTodos.as_view()),
    path('add/', views.AddTodo.as_view()),
    path('edit/<int:pk>', views.EditTodo.as_view()),
    path('api-token-auth/', token_view.obtain_auth_token)
    # path('auth/', views.Authenctication.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)