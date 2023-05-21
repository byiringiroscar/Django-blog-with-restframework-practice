from django.urls import path
from Sport.new_api.views import registration_view_user, registration_view, api_detail_blog_view, api_detail_view, api_update_blog, api_delete_blog,api_create_blog, ApiStatListView, update_view, registration_view
from rest_framework.authtoken.views import obtain_auth_token

name = 'Sport'

urlpatterns = [
    path('register', registration_view_user, name="register_api"),
    path('login/', obtain_auth_token, name="login_api"),
    path('view/<int:pk>/', api_detail_blog_view, name='view'),
    path('detail/', api_detail_view, name='detail'),
    path('update_blog/<int:pk>/', api_update_blog, name='update_api'),
    path('delete/<int:pk>/',  api_delete_blog, name="delete_api"),
    path('create_api_blog/', api_create_blog, name="api_create"),
    path('list_api', ApiStatListView.as_view(), name="list"),
    path('register_view',  registration_view, name='register_view'),
    path('update_view', update_view, name='update_view'),




]