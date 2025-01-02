from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, HouseholdViewSet, ActivityviewSet
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'households', HouseholdViewSet)  # Register the HouseholdViewSet
router.register(r'activities', ActivityviewSet)  # Register the ActivityViewSet

urlpatterns = [
    path('', include(router.urls)),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
