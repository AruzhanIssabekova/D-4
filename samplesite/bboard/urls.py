from django.urls import path
from . import views
from bboard.views import index, by_rubric, BbCreateView

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name="by_rubric"),
    path('', index, name="index"),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
]



