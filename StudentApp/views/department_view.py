from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StudentApp.models.departments import Departments
from StudentApp.serializer.department_serializer import DepartmentSerializer
from django.views import View


class DepartmentTransactionView(View):
    def get(self, request):
        if request.method == 'GET':
            departments = Departments.objects.all()
            departments_serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(departments_serializer.data, safe=False)

    def post(self, request):
            department_data = JSONParser().parse(request)
            departments_serializer = DepartmentSerializer(data=department_data)
            if departments_serializer.is_valid():
                departments_serializer.save()
                return JsonResponse("Added Successfully !!", safe=False)
            return JsonResponse("Failed to Add !!", safe=False)

    def put(self, request):
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(Department_id=department_data['Department_id'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully !!", safe=False)
        return JsonResponse("Failed to Update !!", safe=False)

    def delete(self, request):
        department = Departments.objects.get(Department_id=id)
        department.delete()
        return JsonResponse("Deleted Successfully !!", safe=False)
