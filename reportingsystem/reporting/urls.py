from django.urls import path
from reporting import views

urlpatterns = [
    path("home",views.AdminHome.as_view(),name="adminhome"),
    path('accounts/login',views.SignInView.as_view(),name="signin"),
    path('accounts/logout', views.SignOut.as_view(), name="signout"),
    path("user/add",views.AddUser.as_view(),name="adduser"),
    path("users",views.Users.as_view(),name="users"),
    path("users/change/<int:id>", views.EditUser.as_view(), name="edituser"),

    path("course/add",views.CourseCreateView.as_view(),name="addcourse"),
    path("courses/change/<int:id>", views.EditCourse.as_view(), name="editcourse"),
    path("courses",views.Courses.as_view(),name="courses"),


    path("batch/add",views.BatchCreateView.as_view(),name="addbatch"),
    path("batches", views.Batches.as_view(), name="batches"),
    path("batches/change/<int:id>", views.EditBatch.as_view(), name="editbatch"),

    path("users/home",views.UserHome.as_view(),name="userhome"),
    path("users/timesheet/add",views.AddTimeSheetView.as_view(),name="addtimesheet"),
    path("users/timesheets", views.TimeSheetView.as_view(), name="listtimesheet"),
    path("users/timesheet/change/<int:id>",views.EditTimeSheetView.as_view(),name="edittimesheet"),
    path("users/timesheet/changestatus/<int:id>", views.Status.as_view(), name="changestatus"),
    path("users/timesheet/deletetimesheet/<int:id>", views.RemoveTimeSheet.as_view(), name="deletetimesheet"),

      ]



