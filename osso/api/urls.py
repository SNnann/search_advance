from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from api.views import LevelViewSet, DocumentViewSet
from api import views

from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'level', views.LevelViewSet)
routers.register(r'document', views.DocumentViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('search/<text>/', views.LevelSearch.as_view()),
    path('searchAdvance/', views.LevelSearchAdvance.as_view()),
    path('drill/<id>/', views.LevelDrill.as_view()),
]
