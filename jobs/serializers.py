from rest_framework import serializers
from .models import Freelancer, Business

class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = ['id', 'name', 'tagline', 'bio', 'website', 'profile_pic']

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'name', 'bio', 'profile_pic']
