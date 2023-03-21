from _profiles.models import Profile,ProfileStatus
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProfilePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['photo']

class ProfilStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfileStatus
        fields = '__all__'