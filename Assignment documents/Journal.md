Lakshay's Dev Journal :



# 10 Apr 2020

Now: 3:00pm
have been working on android assignment for the last few hours 
 – Started @ 1:00PM on web Dev

- searched for examples and tutorials for web Dev ass1 - instagram clone with django
- was following tutorial at https://www.youtube.com/watch?v=6jR6c16_DOs&list=PLBOh8f9FoHHjtZJFAYKQRT_sRunC5M0tA&index=4
- it a bit old 
@ 2:40 - had meeting with Kris about progress and what to do going forward
- meeting notes:    
    -Need to make class diagramms for ass 1  and send to Kris asap
    -need to keep writing in this dev journal
    -Need to be serious about web dev assignment
    - need to talk to Kris more - live 
now Going to 
1. make Class Diagrams for simple Instagram and send it to Kris - by 3:45 DONE
2. work on Mobile dev assignemnt for 2 hrs- try to complete it asap to submit before tonight.
3. do django work - 5 hrs 
should be all done by 1-2 am

@3:54 class diagrams are done 70% completion by me - sent to @kris   

-feel sleepy - but will continue to work -- will take a nap till 4:30pm   
@5:10pm  
    - just woke up
    - got banana milk musli , put on Music - im fully awake now :)
    
4.need to also add the class diagram attributes to readme.md of this repo. (DONE@ 5:36)

continueing work sequence from line 14

@5:37
now working on task # 2
- working on  `getTimeslotBooking(String licenceNumber)`(20 marks) (DONE)function - I have already coded it using other fucntions so its simple to implement, however I need to use it somewhere as well so I did use it in the `— bookTimeslot(String licenceNumber, String day, int hour)` (20marks)(DONE) function and now just need to test if everything still works time.Now() = 5:56pm
    - yes everything still works    


@6:02pm
- Now working on "Get a list of summary data for timeslot bookings on a given day  `getSlots(String day) ` (20 marks)Return a sequence of hours, bookingCounts ordered by hour"
    - so this will be basically `ArrayList<Slot> daySlots getSlots(String day)` in my code - ok  
    - yeah that was easy - i had already implemented other methods that helped me  :)  `like slot.getDateString()` so this is also (DONE)     
    

Now   
@6:13pm   

-Need to make the Hotspots UI(10 marks) ok 

- need to learn about how to use TableLayout damn
- so this table layout is kinda you know uses a lot of hard coding - i want to be able to choose the number of rows and columns programatically and just go from there @ 6:34pm 
- I am stuck in research mode!-this might take some time which I dont want to waste
- according to this website I can Do it programatically -https://technotzz.wordpress.com/2011/11/04/android-dynamically-add-rows-to-table-layout/ time.now()= 6:46pm - TOOK 1/2 hr - this felt like just 2-3 minutes 
- yes I was able to expriment amd make `TableLayout` work  time.now()= 7:07pm
- progress is slow.  
@8:46   

- just now I commited the hotspot design 
![hotspot](https://i.imgur.com/iaZNRDsr.jpg)


@9:09pm    
still working on the Mobile assignment 
- i added super user abilities and forcing the right orientation till 9:15pm
- shared the code with friends to get feedback while also marking it by myself for last 45 mins - this is too much time for this task Time now is 10:05pm 
- need to write Unit tests for the android app- but I do not know anything about unit tests - i need to learn it.- I will do it later.
-also it would be good if I sent an email to Jong Casy telling him i am finished with the app :)
- this was a simple app but it took too much time for me to make it.
- I can make this app better and improve it.


- I want to make more android apps- I like the challenge and I like to learn and create but there has to be a challenge and it should be achieveable 
- this project put me in a flow state.

@10:10pm
- now its time for django I need to learn and make the Instagram Clone

-- I will take a Bio Break now will return at 10:30pm
    -I am back I thought i took a lot of time in the shower but wow it was only 15 mins cool

-- so I had planned to do django for 5 hrs today - time now is - 1030 + 5 = 3:30am cool so Ill do that 



#----Starting session django web Apps Assignment 1 ---10:30 to 03:30am <br>
todo 
Read the assignment for 5 mins before 10:45pm [] Failed - document not found 

# 11 Apr 2020 

DAY START @11:40AM

 the past 11-14 hours were a breeze 

 --I am making python app that  an automatically writes my journal for me  
 -- i am very distracted :( i am not focused 
 --its 12:15 pm now and I have not made any progress yet

 -- I want to  make a list of projects that i want to do and finish
#list of projects
1. youtube clone with alex
2. bootstrap course
3. driver licence app
4. Cloud computing app
5. web dev app - Instagram clone with django
6. 

starting to work on django web dev project 12:43pm 11 apr    
Estimate will work till - 7pm

```
== add friend/follower/following feature - 2:12 - 3:00pm 
   -add  friend/follower/following list field to user model
   -get current logged in user
   -get selected user/ selected friend/follower/following
   -in database add the selected friend/follower/following to current user's friend/follower/following list
|coud not find how to do it - taking beak now will be back and start again 
```
Unplanned break from 2:52pm to 4:00pm
```
#Plan after break 
== add friend/follower/following feature - 4:00pm - 5:00pm
==search post function should work 5:00 to 6:00 

==change/reset password 6:00 to 7:00

```
5pm- 6pm ok starting again
```
I deleted all the unnecessary files in my django project
learnt how to use .gitignore files and how to setup a pycharm project with .gitignore
```
@6pm- 7pm
```
finally got .gitignore to work using this 

git rm -r --cached .
git add .
git commit -m "fixed untracked files"

got this from stackoverflow 
still .vs code files were showing up so added to gitignore worked now

:(- stoped at 7PM and then took break and did break stuff 
```
@820 now
```
session is over- it was not productive 
not much progress made :(

```




# 12 April 2020

its 5:23 pm now

now I am working with django shell

```python

PS C:\Users\KL\Desktop\blogapp> python manage.py shell
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on 
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user1 = User.objects.first()
>>> posts = Post.objects.all()
>>> posts.filter(author = user1)           
<QuerySet [<Post: Blog 1 First Post Content!!>, <Post: Blog 2 Second Post Content!!>]>
>>> post4 = Post(title = 'blog4')               
>>> post4
<Post: blog4 >
>>> post4.save()
sqlite3.IntegrityError: NOT NULL constraint failed: blog_post.author_id
django.db.utils.IntegrityError: NOT NULL constraint failed: blog_post.author_id
>>> post4.author_id
>>> post4.author_id = 14
>>> post4.save()         
>>> post4.date_posted
datetime.datetime(2020, 4, 12, 4, 37, 20, 652798, tzinfo=<UTC>)
>>> post4.author 
<User: lakshay>
>>> post4.author.email
''
>>> post4.author.password
'pbkdf2_sha256$180000$tZ1ubThpNrof$eTJIKyVyBrNU0+S2M1BRhVPB16AC31KXn7vagm9VU9A='
>>> post4.author.post_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x00E972E0>
>>> post4.author.post_set() # XXXXXXXXXXXXXXXX wrong
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: __call__() missing 1 required keyword-only argument: 'manager'
>>> post4.author.post_set  
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x00E97250>
>>> post4.author.post_set.all() # right 
<QuerySet [<Post: blog4 >]>
>>> post4.author.post_set.first()
<Post: blog4 >
>>> for(user in User.objects.all()):
>>> for user in User.objects.all():
...     print(user)
... 
manas
lakshay
lakshay2
...
>>> for user in User.objects.all():
...     print(user.id) 
... 
1
14
15...
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> Post.objects.first().__str__()
'Blog 1 bymanas'
```

# 15 April 2020

last 2 days have been bad

now it is 4;27am

```


i am using a time tracker to track all my time but i think it is not a substitute for this


keeping a journal helps has a feature that is I record what I found that could be useful to me in the future

1.java code for Custom recycler Adapter from medium 
2. del and rd commands in cmd /s/q /f 
3. how to make a virtual environment for python
4. how to see the mac address of a router connected to my pc 
etc

I have been doing basics of django tutorials

for the last 4-5 hours I have been working on a personal Android  project - goals app

I also want to work on a journal writer 
I have made some progress on the goals app its  good :) 
I will sleep now

```

I slept at 6 am  and  I woke up just now -  5:15 pm==  sleep time --11hrs 15 mins bad ,np im rested well.

I will write more now

now it is 5:15pm:

```english
Strarting work on django Assignment for 7420

Tasks

1. setup
2. make/find good template for first page of instagram clone
3.
4.
5.
6.
```

```
Going to work on Task #1, 

Estimate: 15 minutes 5:40 to 5:55pm

1.1 so the problem was that I had not uploaded the venv files to the remote and I deleted the project files - when when I cloned the project again pycharms could not find an interpreter - i solved this problem by googling - i need to add an interperter using the bottom right  button "add interpreter" then I had to go to terminal and activate venv and then pip install django 

then I am getting tthis error

1.2 OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: '<frozen importlib._bootstrap>'
this was caused by crispy forms installed apps line in setting.py  - could not find this on the web but i rememberd encountering this problem before and  checked my setting.py again

1.3 now there are some more errors - will fix those 

now it is 5:55 so ill give it 5 mins more - its done at 5:57pm 
```

```
Going to work on Task #2
estimate - 30 mins - 6:00 to 6:30pm x
new estimate -> till 7pm 
new estimate-> till 7:30pm

2.1 look at instagrams first page
 they dont have a header - just a footer and a main in the first page page 
 
2.2 write the firstpage.html
I will be using bootstrap for this

2.3 test if the urls are rendering the templates or not 
	they are not !!
	I added the templates directory  in pycharms's settings - it worked but !! the rpoblem is that it didn't change any settings .py files when I did that - Ill get to this later - test is that does it work when there is no .pycache files 


2.4 make firstpage.html better x
	2.4.1 learn Bootstrap  x
		2.4.1.1 learn how to make container be in the center center center x
2.5 find a readymade template - X

```

@ 7:55 am 

learnt something new 
<div class="container">

```
<div class="row justify-content-center">

    <div class="col-6">
        <h1>wall</h1>
    </div>



</div>
```




```

user authentication
user profile with picture
static files for logo and css
 reset password by link on email
good enough css i guess - on all templates
adding a new post 
seeing list of all other users to add them as a friend /follow them 
search posts with text 

# I have to implement the following features :
improving css
email verification
using postgress 
deploying on heroku/hosting
using upload care for images problem with heroku
add/delete friend/ follower
chatting
notifications when someone you follow posts something etc
commenting 
liking and saving liked posts list
```

Now I am working on :
-chatting
-feed
-notifictons
-ads
-


need the following code for visual studio activate:
`Set-ExecutionPolicy RemoteSigned`
