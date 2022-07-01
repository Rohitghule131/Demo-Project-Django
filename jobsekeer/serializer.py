from pyexpat import model
from rest_framework import serializers
from jobposter.models import Job_Post


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Post
        fields = "__all__"
