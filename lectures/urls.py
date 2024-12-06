from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lectures_home, name='lectures_home'),
    path('create/', views.create, name='add-lecture'),
    path('<int:pk>/', views.LecturesDetailView.as_view(), name='lectures-detail'),
    path('<int:pk>/update', views.LecturesUpdateView.as_view(), name='lectures-update'),
    path('<int:pk>/delete', views.LecturesDeleteView.as_view(), name='lectures-delete')
]
