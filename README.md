
The app is hosted in heroku  here : http://instaclone.lakshaysethi.com/
and the app running from a docker image in google cloud  is hosted here: http://insta-docker.lakshaysethi.com/
and the app running from a docker image in AWS is hosted here: http://insta-docker-aws.lakshaysethi.com/

[discussion](https://github.com/lakshaysethi/Assignment_1_7420_ls/edit/Assignment-2/Assignment%20documents/discussion.md)


insta-docker-aws.lakshaysethi.com  has an A record for  
3.25.65.141

S3 bucket used  is:
react-s3-a2.lakshaysethi.com.s3-website-ap-southeast-2.amazonaws.com

# About InstaClone - Assignment-7420

this is the Lakshay's simple instagram web app 
Features implemented:
1. user login and registrations 
2. user being able to upload photos to this app
3. ability to like images 
4. using aws s3 for image storage or other image storage solution
5. email notifications 
6. search photos by title description

Features yet to be implemented 
- keeping a view count and a like count in database
- if users want to keep some photos private they can
- ads //model 1
- comments on posts // model 2
- chat/dms // model 3
- group chats // model 4
- filter posts based on your reaction to a post
- conversation to progressive web app
- improving css
- need to confirm email before login
- private photos and private accounts
- posts links and #tags
- following and followers lists (partially implemented)
- switch accounts quickly stay logged in to both
- upload multiple files(images) at once to a post 
- upload multiple images and make them become separate posts 
- videos streaming support
- search your comments 
- search posts with #tags and texts or usernames 
- search for users
- option to download images and videos 
- make it hard for users to download media if the media owner doesn't want other users to be able to download his content
- customized feed
- share post to other platforms
- service worker browser notifications 
- postgresSQL and redis
- comments


class Diagram will look somwhat like this:
#### 
![](https://i.imgur.com/HLYDzQZ.png)
