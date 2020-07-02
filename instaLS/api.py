from instaLS.models import Post,Like,Profile
from rest_framework import viewsets, permissions
from . import serializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = serializer.PostSerializer





class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = serializer.LikeSerializer




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = serializer.ProfileSerializer



    