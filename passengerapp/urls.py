from django.urls import path
from .views import passengerView, passengerDetail

urlpatterns = [
    path('passenger/', passengerView),
    path('passenger/<int:pk>', passengerDetail),
]
