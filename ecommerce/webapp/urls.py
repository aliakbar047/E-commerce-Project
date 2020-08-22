from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name = 'home'),
    path('details/<int:pk>', detailPage, name = 'company_page'),
]