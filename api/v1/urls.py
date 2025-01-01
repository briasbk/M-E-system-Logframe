from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, HouseholdViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'households', HouseholdViewSet)  # Register the HouseholdViewSet

urlpatterns = [
    path('', include(router.urls)),
]
