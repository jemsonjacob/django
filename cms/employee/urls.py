from django.urls import path

from employee import views

#
urlpatterns = [
    path('employees/add', views.employee_create, name="addemployee"),
    path("employees/list", views.employee_list, name="listemployee"),
    path('employee/detail/<int:id>', views.employee_detail, name="employeedetail"),
    path('employee/change/<int:id>',views.employee_update,name="changeemployee"),
    path('employee/remove/<int:id>',views.employee_remove,name="removeemployee"),

]
