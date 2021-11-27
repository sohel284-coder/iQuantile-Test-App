from django.urls import path

from filemanagementapp.views import *


urlpatterns = [
    path('', file_management, name='file_management'),
    path('api/create-file', FileManagementListCreateAPIView.as_view(), ),
    path('api/files', FileListAPIView.as_view(), ),
    path('api/file/<int:id>', FileRetrieveUpdateDestroyAPIView.as_view(),),
    path('register', register_page, name="register_page"),
    path('login', login_page, name='login_page'),
    path('logout', logout_user, name='logout_user'),
    
]