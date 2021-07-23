from django.urls import path
from .views import my_profile_view, test_view

app_name = 'profiles'

urlpatterns = [
    path('', my_profile_view, name='my'),
    path('test/', test_view, name='test')
]
