from rest_framework import serializers

from students.models import student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('First_name', 'Last_name', 'Favorite_Topic', 'Capstone')