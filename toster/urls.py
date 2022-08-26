from django.urls import path
from toster.views import index, test99, result

urlpatterns = [
    path('', index),
    path('test99', test99),
    path('result', result),
]
