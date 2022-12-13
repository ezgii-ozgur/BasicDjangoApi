from django.urls import re_path
from StudentApp import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^get_data/student$', csrf_exempt(views.StudentTransactionView.as_view())),
    re_path(r'^insert_data/student$', csrf_exempt(views.StudentTransactionView.as_view())),
    re_path(r'^update_data/student$', csrf_exempt(views.StudentTransactionView.as_view())),
    re_path(r'^delete_data/student/([0-9]+)$', csrf_exempt(views.StudentTransactionView.as_view())),
    re_path(r'^get_data/department$', csrf_exempt(views.DepartmentTransactionView.as_view())),
    re_path(r'^insert_data/department$', csrf_exempt(views.DepartmentTransactionView.as_view())),
    re_path(r'^update_data/department$', csrf_exempt(views.DepartmentTransactionView.as_view())),
    re_path(r'^delete_data/department/([0-9]+)$', csrf_exempt(views.DepartmentTransactionView.as_view())),
]
