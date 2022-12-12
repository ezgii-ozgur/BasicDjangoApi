from rest_framework import serializers
from StudentApp.models.departments import Departments


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('Department_id', 'DepartmentName')
