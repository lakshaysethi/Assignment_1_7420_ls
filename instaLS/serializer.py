from rest_framework import serializers
from instaLS.models import Like,Profile,Post

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
