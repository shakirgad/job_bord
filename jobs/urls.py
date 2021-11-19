from django.urls import path
from .import views
from .import api

app_name='jobs'

urlpatterns = [ 
    path('', views.job_list ,name='home'),
    path('addjob/',views.addjob,name='addjob'),
    path('<str:slug>',views.job_detail ,name='job_detail'),
    path('job/api',api.jobsapi ,name='jobsapi'),
    path('job/api/<int:id>',api.jobdetail ,name='jobdetail'),
    path('job/api/v2',api.Jobs_Class_Api.as_view() ,name='Jobs_Class_Api'),
    path('job/api/v2/<int:id>',api.Job_Detail_Api.as_view() ,name='Job_Detail_Api'),
    path('job/api/mixins',api.mixins_list.as_view() ,name='mixins_list'),
    path('job/api/mixinsupd/<int:pk>',api.mixins_up_des.as_view() ,name='mixins_up_des'),
    path('aplay_api/',api.aplay_api ,name='aplay_api'),
    
    
]