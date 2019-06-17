from django.urls import path

from . import views
urlpatterns = [
    path('', views.step_tracker_main, name="step_tracker_main"),
]