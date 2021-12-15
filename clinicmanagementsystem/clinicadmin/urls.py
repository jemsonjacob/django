from django.urls import path

from clinicadmin import views

urlpatterns = [ path("doctor/add",views.doctor_create,name="doctoradd"),
                path("doctor/list", views.doctor_list, name="doctorlist"),
                path("doctor/change/<int:id>", views.doctor_update,name="changedoctor"),
                path("doctor/remove/<int:id>",views.doctor_remove,name="removedoctor"),
                path('doctor/detail/<int:id>', views.doctor_detail, name="doctordetail"),
                path("accounts/signup", views.sign_up, name="signup"),
                path("accounts/signin", views.sign_in, name="signin"),
              ]

