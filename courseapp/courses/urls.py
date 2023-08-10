from django.urls import path 

from . import views
urlpatterns = [
     
     path('',views.index),
    path('index',views.index),
    path('<kurs_id>',views.details),
  
  
    path('kategori/<int:category_id>',views.getCoursesId),
    
    path('kurslar/<str:category_name>',views.getCourses, name='courses_by_category'),

   


 
 
    
    

]
