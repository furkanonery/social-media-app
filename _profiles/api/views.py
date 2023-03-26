# from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from _profiles.models import Profile
from _profiles.api.serializers import ProfileSerializer
from rest_framework import mixins
from _profiles.api.permissions import ownProfileOrReadOnly

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