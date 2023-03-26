from django.urls import path, include
from _profiles.api import views
from rest_framework.routers import DefaultRouter

# profile_list = views.ProfileViewSet.as_view({'get':'list'})
# profile_detail = views.ProfileViewSet.as_view({'get':'retrieve'})

router = DefaultRouter()
router.register(r'profiles',views.ProfileViewSet)
router.register(r'status',views.ProfileStatusViewSet, basename='status')

urlpatterns = [
    # path('user-profiles/', views.ProfileList.as_view(), name='profiles'),

    # path('user-profiles/', profile_list, name='profiles'),
    # path('user-profiles/<int:pk>', profile_detail, name='profile-detail'),

    path('',include(router.urls)),
    path('profile_photo/',views.ProfilePhotoUpdateView.as_view(),name='profile-photo'),
]
