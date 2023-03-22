from django.urls import path
from _profiles.api import views

urlpatterns = [
    path('user-profiles/', views.ProfileList.as_view(), name='profiles'),
]
