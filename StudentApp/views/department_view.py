from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StudentApp.models.departments import Departments
from StudentApp.serializer.department_serializer import DepartmentSerializer


@csrf_exempt
def get_department_data(request):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)


@csrf_exempt
def insert_department_data(request):
    if request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully !!", safe=False)
        return JsonResponse("Failed to Add !!", safe=False)


@csrf_exempt
def update_departments_data(request):
    if request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(Department_id=department_data['Department_id'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully !!", safe=False)
        return JsonResponse("Failed to Update !!", safe=False)


@csrf_exempt
def delete_departments_data(request, id=0):
    if request.method == 'DELETE':
        department = Departments.objects.get(Department_id=id)
        department.delete()
        return JsonResponse("Deleted Successfully !!", safe=False)
