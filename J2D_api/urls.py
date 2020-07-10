from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from J2D_api import views
from rest_framework.authtoken import views as token_view

urlpatterns = [
    path('get_todos/', views.UserTodos.as_view()),
    path('add_todo/', views.AddTodo.as_view()),
    path('edit_todo/<int:pk>', views.EditTodo.as_view()),

    path('get_items/', views.UserItems.as_view()),
    path('add_item/', views.AddItem.as_view()),
    path('edit_item/<int:pk>', views.EditItem.as_view()),

    path('get_itemlists/', views.UserItemLists.as_view()),
    path('add_itemlist/', views.AddItemList.as_view()),
    path('edit_itemlist/<int:pk>', views.EditItemList.as_view()),
    
    path('api-token-auth/', token_view.obtain_auth_token)
    # path('auth/', views.Authenctication.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)