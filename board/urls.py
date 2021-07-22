from django.urls import path
from .views import (
    board_view,
   
) 

app_name = 'board'

urlpatterns = [
    
    path('board/', board_view, name='board'),
   

]