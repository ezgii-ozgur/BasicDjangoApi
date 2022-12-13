from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views import View

from StudentApp.models.students import Students
from StudentApp.serializer.student_serializer import StudentsSerializer


class StudentTransactionView(View):

    def get(self, request):
        if request.method == 'GET':
            students = Students.objects.all()
            students_serializer = StudentsSerializer(students, many=True)
            return JsonResponse(students_serializer.data, safe=False)

    def post(self, request):
        if request.method == 'POST':
            student_data = JSONParser().parse(request)
            students_serializer = StudentsSerializer(data=student_data)
            if students_serializer.is_valid():
                students_serializer.save()
                return JsonResponse("Added Successfully !!", safe=False)
            return JsonResponse("Failed to Add !!", safe=False)

    def put(self, request):
        if request.method == 'PUT':
            student_data = JSONParser().parse(request)
            student = Students.objects.get(StudentId=student_data['StudentId'])
            students_serializer = StudentsSerializer(student, data=student_data)
            if students_serializer.is_valid():
                students_serializer.save()
                return JsonResponse("Update Successfully !!", safe=False)
            return JsonResponse("Failed to Update !!", safe=False)

    def delete(self, request, id=0):
        if request.method == 'DELETE':
            student = Students.objects.get(StudentId=id)
            student.delete()
            return JsonResponse("Deleted Successfully !!", safe=False)
