from django.urls import path

from patient import views

urlpatterns=[
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/signin',views.signin,name='signin'),
    path('accounts/signout',views.signout,name='signout'),
    path("", views.user_home, name="user_home"),
    path('appointment/add/<int:a_id>',views.appointment_create,name="appointmentcreate"),



]