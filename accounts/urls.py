from django.urls import path
from . import views as v

app_name = 'accounts'

urlpatterns = [
    path('signup/', v.user_reg_view, name='signup'),
    path('login/', v.user_login_view, name='login'),
]
