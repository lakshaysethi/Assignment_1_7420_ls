# Questions
1. When would you prefer to develop an Assignment 1.  style web aplication (Server-side rendering, serving HTML)?
- for simple apps which dont require **many** changes to the front end quickly
- also If I want to get something finished quickly I will not bother making a react front end for it just make the server side templates
2. When would you prefer an  one (REST API & Single Page Application)?
- rest api is good to have for any large scale application so that you can also allow other developers to create custom versions of the front end and serve users in a customized way.
- Also if I want to monetize the data sent from my backend to the anyone who wants to use my api's I will use REST API
- if I am building something like facebook or a really big app
- I'll use a Single page app that uses client side rendering of data to save the cost of running my servers.
## Version Control
3. What is git and what is it used for?
- Git  is a version control system for tracking changes in source code during software development. 
- It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.
- However it works best with programming files and not with other media and document types like mp4 or docx 
4. List 3 git commands you’ve learned in this course.
- git commit
- git diff
- git push
5. What is GitHub and what is it used for?
- github uses Git, a version control system for software development
- it is a Git repository hosting service, we can use it to collaborate on a big programming projects to merge the code of all the colaborators
- It can be used for managing issues from users and testers with a current version using the issues tab
- we  can upload our code to it and it keeps a good history of all the changes we made to the code wing commits. we can see the differences
6. What is Kanban and what is it used for? 
- kanban is used to devide work into small parts and then assign it between people working in software development or any other field as well- kanban is japanese for billboards. A common kanban style board includes 3 boards with titles as backlog or todo  then dong now and then done 
each Sprint can have its own kanban board.
7. What is Markdown and what is it used for?
- markdown is a lightweight markup language with plain-text-formatting syntax. we can use it to write documentation or any thing really - but its not a fire that will run the code - it can have code snippets but its usually not used as a file to be read by interpreters and execute code from. There are many markdown readers that read and display markdown and - just lik browsers read and display HTML code
## Platform vs Infrastructure: -
8. What are some of the pros and cons of using Platform-as-a-Service (PaaS) providers such as Heroku?
#### pros 
- quick to setup and host/deploy simple apps
- easy/ has lots of support from the service provider - and sometimes has large number of users so it can be easy to find answers to problems and to debug
#### cons
- does not support or have all the features that IaaS might offer (limited capability)
- expensive
9.  What are some of the pros and cons of using Infrastructure-as-a-Service providers such as Amazon?
#### pros 
- is cheaper than PaaS
- easier to scale
- many more services than PaaS are available at a good price
#### cons
- it can be complicated to set up for the general user.
- companies try to lock down a customer with their setup time investment and complex setup.
## Web Frameworks
10. What is Django?
- it is a python web framework- which can be used to build both an api just -backend and also a complete package (Front and back)
11. What are some of its useful features? 
- ORM
- Forms
- Templates and views
- admin backend 
12. What is a model?
- it is like a class - when we make a class diagram we can make all models exacly as the classes in the class diagram 
- we can make custom models for any kind of object we want in our app
- 
13. What is a view?
- these are functions that are run when a URL is used to send a request to the server. Eg when we make a post request to the server using the URL pattern like Mysite.com/make-post/ then the function attached to it (the view) will be run
14. Name two other popular non-Python web frameworks.
Laravel for php
Spring for Java
15. What is WSGI?
Web server gateway interface, it is a convention that needs to be used by web servers to forward requests to the python code that runs a web app.
16. What is ASGI?
This is a cooler version of WSGI it basically does the same thing but also supports asynchronous python 
17. What is celery and what are task queues used for?
Celery is a vegetable that all students need to eat to be able to get the vitamins needed to do programming.
Jk
Celery is a task queue
The way I understand it is that is like a list made by a waiter at a restaurant. The waiter takes orders from the customers as they come
This waiter is using digital list.
The kitchen staff is like a worker that makes the dishes one by one.
Celery is a list of tasks (but works as a queue data structure ) and workers keep checking the list for new tasks and do them.
Tasks can be like sending an email or more complex which take more than a few milliseconds
Like processing a video.
The main reason I use it is to make my websites perform better and for a better UX. As I don't want to keep the users waiting and have no feedback about what's going on when the tasks are taking long
## Databases
18. What is PostgreSQL?
Its an open source relational  database management system.
19. Using StackShare, list 3 well-known companies that use PostgreSQL. 
Uber
Netflix
Instagram
Stackshare
20. List two other well-known databases.
Firebase firestore
mysql
Sqlite
Mongodb
21. What are some of the pros and cons of using an Object Relational Mapper (ORM)?
Pros
Don't have to write the SQL queries for the relationship for the models or classes in our app.
Makes it easy to migrate data between different databases
Cons
Complex queries can lead to performance issues
22. What is the purpose of database migrations?
when we run the makemigrations in django command then new changes we made in our models/classes get reflected in the data base as new  tables and/or new fields(columns)
 if we are running this for the first time then in a new database all the tables will be setup for use by the backend
ORM helps us because we can migrate to another database easily
23. What is redis and what are two things it can be used for?
redis is like a database but it only stores data temporarily 
24. Why do we use caches? HTTP & REST: 
25. Which four HTTP methods does REST use for performing CRUD operations?
GET
POST
DELETE
UPDATE
26. What is Django REST Framework used for?
the main purpose of DRF is to help make a REST  API for our django application server. 
DRF provides a way to serialize and deserialize models much like the django forms.- we need this inorder to send and recieve data to and from our API
DRF also provies a default router that  helps us make url patterns and we can specify permission levels for access to the api 
27. What is serialization and why do we use it?
we use serialization to convert objects into strings
this is done to convert complex data into a simpler string form so that it is easy to send this over the internet/network
28. Which type of object serialization notation is most commonly used on the web?
JSON
XML
29. What is Postman and what is it used for?
postman is software that makes it easy to make any kind of request to an API endpoint and  test the output from it
we can even put headers with our requests -
it provied a good GUI for all this and we can also store our  API links and queries in the software for testing at a later point 
30. What are websockets and what are they used for? Javascript: 
dont know
31. What is NodeJS and how is it different from in-browser Javascript?
NodeJS is something that allows us to run javascript outside the browser - in essence it makes the V8 JavaScript engine which is used in major browsers today available outside of the browser. And so now JS can be used as a backend language aswell instead of just being used in the frontend
now we can use it to write to files and databases and even sontrol the system it is running on.
the other differences are that the JS in use in NodeJS uses up to date ES6/ES7/ES8 where as  browsers still use old versions of JS so they cant read and run the code without dependencies.
32. What is npm and what is it used for?
npm is Node package manager
it is like pip 
it allows us to use packages/modules written by other developers
so that we dont have to recreate the wheels from scratch
we can do `npm init` and it makes a package.json file which has very useful info abou the dependencies of this node project we are working on 
npm packages like Express are really useful and we can do npm intall express and it creates a new entry in the dependiencies field in the package.json
this is really useful because it has become a standard any allows people to not have to upload/ share a copy of all dependencies of a project and make the new project light weight
npm also has scripts supports  the run command  like run build / start/ test 
33. What is ES6? List the names of 3 features that ES6 provides.
it is the 2016 version of JS caled ECMAScript 6
new syntax like
arrows `=>`  or `()=>{}`
template strings
modules- using `import`
promises
34. What is ReactJS and what is it used for?
ReactJS is a JS library
ReactJS is made by Facebook and they and now many companies use it to make their front end   - it is a virtual dom -
reactJS allows for an individual component to be updated instead of the whole html to be reloaded
react uses JSX which is like html but better as we can make our own custom components which have custom tags gor example `<MyCoolCustomComponentThatHasOtherComponentInIt />`
35. List two popular alternative Javascript libraries to ReactJS. 
VueJS
Angular
36. What is the DOM? What is a virtual DOM?
oh Dom, hes one of my old friends
DOM - its the document object model- its what is used by the browser to diaplay the various components like `<div>` or`<h1>` from the Html to the final renderd version
traditilly the JS frameworks updated the DOM too much and so it was slow.
so now we need a Virtual DOM that is a layer above the DOM in which only the component that needs to be updated will be updated and not the entire DOM
37. What is the difference between sessionStorage and localStorage? 
this is what i found from a youtube video by [Web Dev Simplified](https://www.youtube.com/watch?v=GihQAC1I39Q)
![sessionStorage vs localstorage](https://i.imgur.com/mZOJOAw.png)
so what I unserand is that this is a place to store user data in the browser.
it isent accessable across different browsers
session storage's scope is limited to the current tab in the browser and gets deleted when the tab is closed
localStorage can store more data like 10 mb than sessionStorage (5mb)and local storage persistes until the user manually deletes it
I think I used localStorages in some of my  apps at https://lakshaysethi.com
38. What is a library like Material-UI used for? 
Material UI has many premade ReactJS componets that we can use in our web apps 
on their website they say that thier goal is making React UIs development easier, better, and accessible to more people.
we can copy and past their code and modify it according to our requirements but they provide the building blocks for us to make the basic good looking components
#### Docker: 
39. Why do we run apt-get update && apt-get install -y in one command when using Docker? 

40. What are Docker containers and what are the pros and cons of using them?
    - Docker containers are are os free 
41. What is the difference between ADD and COPY with Docker?
42. What is a .dockerignore file used for?

43. What is Kubernetes and why didn’t we use it?
    - it is an open-source system for automating deployment, scaling, and management of containerized applications.
    - so what I unserstand is that it is a system that automatically checks the demands in usages and deploys more containers if needed to habndel the load  of an app/ API
    - According to Kris:
    > When there multiple containers or versions of our website running in the cloud, some backend and frontend container servers might have different versions at a given time.That's when we need to use a software for managing them, such as Kubernetes.However Kubernetes is  complex therefore its usually if we have 1000+ containers running.
## Deployment: 
44. What is Amazon S3 used for? 
    - S3 is a cloud storage offered by amazon - we can use it to host staric files to the public or
     to store important data or  files that need to backed up and needs to be super secure.
     it allows users to set different options on how secure they want their data to be.
45. What is Amazon ECS? 
    - Elastic Container service is amazon's service for helping people run and manage their containers in the same backed used by EC2
46. What is the difference between ECS Fargate and EC2? 
    - EC2  bascially is a Virtual machine offering by AWS. Users can make any kind of virtual machine and access it from anywhere in the world.
    it comes with all the good features of VMs like Snapshots etc.
    these can be configured to use any kind of hardware and run different software images.
    // dont know about Fargate 

47. Name 3 other cloud providers. 
    - Google Cloud platform
    -  Microsoft Azure
    - Alibaba Cloud
    - IBM Cloud

48. What is Sentry and what is it used for? 
    - Sentry is an Error Alerting system that Sends notifications to project/app owners/developers when something goes wrong in the system/ when some error occurs - this is really good during production as one needs to know if something is not right and when it happens
49. What is Cloudflare and what is it used for? 
    - Cloudflare is used to manage DNS and other important Domain related stuff like SSL and DNSSEC. 
    -  it offer's its own name servers for user's Domains
    - in my experience it is fast to add DNS records and these records get updated very quickly.- we can add Cname records and A records - and have our domain name added to our hosed app

50. What is SendGrid and what is it used for? 
    - Send grid is a company that offers digital marketing services to users like Email marketing and SMS marketing 
51. What is the difference between a DNS A record and a CNAME record?
    - I use A records for masking ip adresses and CNAME records for masking other domains like I used an A record to mask ip address of google Firebase and a CNAME record for amsking my AWS S3 publicaly hosted bucket 
## Meta: 
52. What are some of the mistakes or difficulties you encountered in developing these 2 assignments? 
#### difficulties
- difficulty focusing due to the my environment being very cold and especially my hands and feet get very cold in cold environments which can lead to other health problems like headaches
- food was another problem as I dont have the habit of cooking for myself and in the past when I have cooked I have ended up wasting the ingredients sometimes.The food that I ate caused heartburns (buring feelings in esophagus and stomach) many times.
- not sleeping before 1 am/ 12 am and staying up all night and then sleeping during the day
- feeling tired during the day immidiately when I start to work on my assignment.
#### Mistakes
- poor time management 
- lack of pre planning
- running around unconsciuosly and ignoring important stuff
- not taking out me time to think about these mistakes and how to remedy them 
- 
53. What have you learned from this course that you think might be useful in your career?
#### life skills and lessons
- Team working is great - there is something magical in working with people - it motivates you they can share their resources with you and you can work with them in harmonious way
- cultivating good realtionships is essential to be successful and happy in life 
- A good leader can change your life as he sets good standards and puts in good systems in place and helps you become a leader yourself (Kris did this for me) :) Thank You!! :)
- I need to take some time every week and do a meeting with myself talking about any problems I am facing or any mistakes im making repetedly and how I can best fix and solve them.
#### programming skills and lessons
- Django,python,etc skills - I really like this new tecnology 
- I like programming
- I got to play with and learn about JS, ReactJS, AWS, and many other technologies
- Github - issues and hwo to work in a team using github - i learnt that communication is really important - to understand your team and work smoothly.
#### due to the lockdown
- A Lockdown doesnt have to make us feel disconnected - we can still grow and communicate with our friends and work on our goals with other people online.
- However we need to be prepared and be a part of groups (before the lockdowns/other big change) that we are part of and a place to find new people that we can be sane with.
