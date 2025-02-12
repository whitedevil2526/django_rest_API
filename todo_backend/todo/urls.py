from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TodoviewSet

router = DefaultRouter()

router.register(r'todos',TodoviewSet)

urlpatterns = [
    path('',include(router.urls))
]