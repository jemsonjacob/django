from django.urls import path
from jobseeker import views

urlpatterns = [
    path("", views.JobSeekerHome.as_view(), name="jhome"),
    path("profile/add", views.AddProfileView.as_view(), name="jprofileadd"),
    path("profile/list/{id}", views.JProfileListView.as_view(), name="jprofilelist"),
    path("profile/edit/<int:id>", views.JEditProfile.as_view(), name="jprofileedit"),
    path('jobs/find',views.JobSearchView.as_view(),name="findjob"),
    path('job/{id}',views.JobView.as_view(),name="jlist"),

    path('job/apply/<int:id>', views.JobApplyView.as_view(), name="japply"),


]
