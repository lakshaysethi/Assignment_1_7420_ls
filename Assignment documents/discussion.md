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

28. Which type of object serialization notation is most commonly used on the web?
29. What is Postman and what is it used for?
30. What are websockets and what are they used for? Javascript: 
31. What is NodeJS and how is it different from in-browser Javascript?
32. What is npm and what is it used for?
33. What is ES6? List the names of 3 features that ES6 provides.
34. What is ReactJS and what is it used for?
35. List two popular alternative Javascript libraries to ReactJS. 
36. What is the DOM? What is a virtual DOM?
37. What is the difference between sessionStorage and localStorage? 
38. What is a library like Material-UI used for? Docker: 
39. Why do we run apt-get update && apt-get install -y in one command when using Docker? 
40. What are Docker containers and what are the pros and cons of using them?
41. What is the difference between ADD and COPY with Docker?
42. What is a .dockerignore file used for?
43. What is Kubernetes and why didn’t we use it? 
## Deployment: 
44. What is Amazon S3 used for? 
45. What is Amazon ECS? 
46. What is the difference between ECS Fargate and EC2? 
47. Name 3 other cloud providers. 
48. What is Sentry and what is it used for? 
49. What is Cloudflare and what is it used for? 
50. What is SendGrid and what is it used for? 
51. What is the difference between a DNS A record and a CNAME record?
## Meta: 
52. What are some of the mistakes or difficulties you encountered in developing these 2 assignments? 
53. What have you learned from this course that you think might be useful in your career?
