from django.urls import path,include
from .import views
app_name='contact'
urlpatterns = [
    path('contact_us',views.contact_us,name='contact'),
]
