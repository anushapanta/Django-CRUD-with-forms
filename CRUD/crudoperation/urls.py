from . import views
from django.urls import path

urlpatterns = [
    path('', views.studentListDetails, name='student_list'),
    path('student_create', views.studentCreate, name='student_create'),
    path('student_update/<int:id>', views.studentUpdate, name='student_update'),
    path('student_delete/<int:id>', views.studentDelete, name='student_delete'),
]
