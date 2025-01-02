from rest_framework import serializers
from projects.models import Project
from household.models import Household, HouseholdMember
from activity.models import Activity

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class HouseholdMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdMember
        fields = '__all__'

class HouseholdSerializer(serializers.ModelSerializer):
    members = HouseholdMemberSerializer(many=True, read_only=True)  # Nested serializer for members

    class Meta:
        model = Household
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        fields= '__all__'