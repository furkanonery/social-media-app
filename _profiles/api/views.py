from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from _profiles.models import Profile, ProfileStatus 
from _profiles.api.serializers import ProfileSerializer, ProfilStatusSerializer, ProfilePhotoSerializer
from rest_framework import mixins
from _profiles.api.permissions import ownProfileOrReadOnly, ownProfileStatusOrReadOnly

# class ProfileList(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

class ProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin, silme işlemi istemiyoruz şu an için
    GenericViewSet
):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,ownProfileOrReadOnly]

class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfilStatusSerializer
    permission_classes = [IsAuthenticated,ownProfileStatusOrReadOnly]

    def perform_create(self, serializer):
        
        serializer.save(user_profile_id = self.request.user.id)

class ProfilePhotoUpdateView(generics.UpdateAPIView):
    
    serializer_class = ProfilePhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object