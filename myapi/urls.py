from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapi.views import FlowerView, flowerPredict

router = routers.DefaultRouter()
router.register(r'myapi', FlowerView)

urlpatterns = [
    path('', include(router.urls)),
    path('status/', flowerPredict)
]