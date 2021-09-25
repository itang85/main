from django.urls import path, include
from app.common.views import *


app_name = 'app.common'

urlpatterns = [
    path('', TestView.as_view(), name='test'),
]
