from rest_framework import serializers
from students import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'firstName',
            'lastName',
            'cohort',
            'favoriteTopic',
            'favoriteTeacher',
            'capstone',
        )
        model = models.Student