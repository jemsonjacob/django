from django.urls import path

from owner import views
#
urlpatterns=[


    path("", views.dashboard, name="dashboard"),
    path('mobiles/add', views.mobile_create, name="addmobile"),
    path('mobiles/detail/<int:id>', views.mobile_detail, name="mobiledetails"),
    path("accounts/signup", views.signupview, name="signup"),
    path("accounts/signin", views.signinview, name="signin"),
    path("mobiles/list", views.mobile_list, name="listmobile"),
    path('mobiles/change/<int:id>', views.mobile_update, name="changemobile"),
    path('mobiles/remove/<int:id>', views.mobile_remove, name="removemobile"),
    path('dashboard/edit/<int:id>', views.dashboard_edit, name="dashboardedit")

]
