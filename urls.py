
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='drivingtest_login'),
    path('test/',views.test,name='drivingtest_test'),
    path('questions/', views.ques,name='cityhead_question'),
    path('tutorial/', views.tutorial,name='drivingtest_tutorial'),
    
    #urls below are defined for mobile view purpose and refer to the links which are temporarly kept on home page. can be removed once those hyperlinks are removed from home page.
    path('instructions', views.instructions,name='instructions'),
    path('mobilequestions', views.mobilequestions,name='mobilequestions'),
    path('mobilequestionpanel', views.mobilequestionpanel,name='mobilequestionpanel'),
    path('mobilereviewpage', views.mobilereviewpage,name='mobilereviewpage'),

]
