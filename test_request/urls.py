from django.urls import path
from test_request.views import TestRequest

urlpatterns = [
    path('TestRequest',TestRequest.as_view(),name='test_request_get'),
]