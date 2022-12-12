from django.urls import re_path
from StudentApp import views


urlpatterns=[
    re_path(r'^get_data/department$',views.department_view.get_department_data),
    re_path(r'^insert_data/department$',views.department_view.insert_department_data),
    re_path(r'^update_data/department$',views.department_view.update_departments_data),
    re_path(r'^delete_data/department/([0-9]+)$',views.department_view.delete_departments_data),
]