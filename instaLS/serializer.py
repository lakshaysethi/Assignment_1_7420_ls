from rest_framework import serializers
from instaLS.models import Like,Profile,Post


# class DataAnalyser:
#     topUser = calculateTopUser(self,1)   #the one with the most posts
#     maxPostsPerUser = calculateTopUser(self,1) #the one with the most likes/reactions
#     topPost = calculateTopUser(self,2)   
#     maxLikes = calculateTopPost(self,2)

#     def DataAnalyser(self):
#         pass


#     def calculateTopUser(self,num):
#         mostPostsPerProfile = 0
#         bestProfile = None
#         for profile in Profile.objects.all():
#             if (getNumberOfPosts(profile)>mostPostsPerProfile):
#                 mostPostsPerProfile = getNumberOfPosts(profile)
#                 bestProfile = profile
#         if(num == 2):
#             return mostPostsPerProfile
#         else:
#             return bestProfile


#     def calculateTopPost(self,num):
#             mostLikesPerPost = 0
#             bestPost = None
#             for Post in Post.objects.all():
#                 if (getNumberOfLikes(Post)>mostLikesPerPost):
#                     mostLikesPerPost = getNumberOfLikes(Post)
#                     bestPost = Post
#             if(num == 2):
#                 return mostLikesPerPost
#             else:
#                 return bestPost
    
#     def getNumberOfPosts(self,profile):
#         return profile.post_set().count
    
#     def getNumberOfLikes(self,Post):
#         return Post.like_set().count


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




