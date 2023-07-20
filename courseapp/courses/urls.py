from django.urls import path
from . import views
urlpatterns = [

   # path('slay/',views.GetInfo),
    path('',views.site),
    path('lprogramlama',views.site),
    path('<category>',views.getKnowledge),
]
