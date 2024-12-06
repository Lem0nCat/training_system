from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('', views.tests_list, name='tests_list'),
    path('<int:lecture_id>/', views.question_list, name='question_list'),
    path('<int:lecture_id>/<int:question_id>/', views.question_view, name='question_view'),
    path('<int:lecture_id>/create/<int:type>', views.question_create, name='question_create'),
    path('<int:lecture_id>/create/', views.test_create, name='test_create'),
]
