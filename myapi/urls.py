from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapi.views import FlowerView, flowerPredict, vitaminPredict, breastCancerPredict

router = routers.DefaultRouter()
router.register(r'myapi', FlowerView)

urlpatterns = [
    # path('', include(router.urls)),
    path('flower/', flowerPredict),
    path('vitamin/', vitaminPredict),
    path('breastCancer/', breastCancerPredict)
]