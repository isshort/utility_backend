from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from users import views as  user_view


app_name='users'
urlpatterns = [
 
    path('list/', user_view.UserListMainView.as_view({'get': 'list'})),
    path('detail/<int:pk>', user_view.UserListMainView.as_view({'get': 'retrieve'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
