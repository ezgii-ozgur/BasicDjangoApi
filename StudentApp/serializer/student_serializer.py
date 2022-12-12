from rest_framework import serializers
from StudentApp.models.students import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('StudentId', 'StudentName', 'Department', 'Date', 'PhotoFileName')
