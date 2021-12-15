from django.urls import path
from employer import views

urlpatterns = [
    path("",views.AdminHome.as_view(),name="companyhome"),
    path('accounts/signup',views.AddUser.as_view()),
    path('accounts/login', views.SignInView.as_view(), name="login"),
    path('accounts/logout', views.SignOut.as_view(), name="logout"),

    path("cprofilehome", views.CProfileHome.as_view(), name="cprofilehome"),
    path("employer/profile/add",views.ComProfileCreateView.as_view(),name="addcomprofile"),
    path("employer/profile/{id}",views.ComProfileListView.as_view(),name="listcomprofile"),
    path("employer/profile/change/<int:id>", views.EditComProfile.as_view(), name="editcomprofile"),

    path("employer/profile/delete/<int:id>", views.DeleteCprofile.as_view(), name="deletecprofile"),

    path("jobhome", views.JobHome.as_view(), name="jobhome"),
    path("employer/job/add", views.AddJob.as_view(), name="addjob"),
    path("employer/job/{id}", views.JobListView.as_view(), name="listjob"),
    path("employer/job/edit/<int:id>", views.EditJobView.as_view(), name="editjob"),

    path("employer/applications{id}", views.ApplicationView.as_view(), name="application"),
]
