# factwise_test
##project planner tool

created REST-FULL API's for team project planner tool.

##API's to manage users

1.With the help of model and Serializer we have created a basic user for planner tool.

2.We have used json formate for both input as well as output also we have user JsonResponse to send output response as json formate.

3.For list all users we have use objects.all() function to retrieve all users data from database.

4.In user describe part we need only one user data for that we have used .filter() function.

5.For updating a user data we have used .update(values...) funtion.

6.To get team of a user 1st we have to find our user in team database with there id. For that i have find loop idea to get our user in team database and after that we have to get that id where our user id found. with the hepl of that team id we have displayed tram information of team. 

7.IN 1st part of project i have face problem in to find user in teams and i use loop to find user and get that team id.
