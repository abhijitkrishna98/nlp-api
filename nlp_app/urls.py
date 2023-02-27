
from django.urls import path
from . import views
urlpatterns = [
    path('nlp_api', views.nlp_api),
]
