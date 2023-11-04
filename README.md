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


##API's to manage teams

1.For 1st three API's(create_team, update_team, list_all_teams) i have excuted a same plan as i used for 1st part of project. 

2.In adding users to team with 50 user limit i have used if else statment. in this process 1st i have to make sure to how many used already present in our database after that with help of if else statment and counter i have stored upto 50 users in teams.

3.For removing user from team 1st we have to get all user list of team and after i have used remove() function on that list and store that new list in database again.

4.For list team users i have used both apps models. 1st i have retrieved a user ids from team database and then retrieved user data for all ids.


