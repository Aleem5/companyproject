from django.urls import include, path
from rest_framework import routers
from department import views

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]