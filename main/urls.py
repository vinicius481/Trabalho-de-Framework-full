from django.urls import path
from .views.index import Index
from .views.login import Login
from .views.signup import Signup
from .views.update_user import UpdateUser
from .views.dashboard import Dashboard
from .views.logout import Logout


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
    path('dashboard/<str:username>/', Dashboard.as_view(), name='dashboard'),
    path('atualizar/cadastro/<int:pk>', UpdateUser.as_view(), name='updateuser'),
]
