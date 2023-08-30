from django.urls import path
from users import views as  user_view
app_name='users'
urlpatterns = [
 
    path('list/', user_view.UserListMainView.as_view({'get': 'list'})),
    path('detail/<int:pk>', user_view.UserListMainView.as_view({'get': 'retrieve'})),
]
