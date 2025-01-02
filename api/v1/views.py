from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer, HouseholdSerializer, ActivitySerializer
from projects.models import Project
from household.models import Household
from activity.models import Activity

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated] 

# Household ViewSet
class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        user = self.request.user
        if user.organization:
            return Household.objects.filter(organization=user.organization)
        return Household.objects.all()
    

class ActivityviewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated] 
