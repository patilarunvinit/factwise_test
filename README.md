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

5.In second part of project we have to store list of user in one place for that i have used ListTextField() list function from django_mysql.models.


##API's to manage board and task

1.I executed a same plan as user for creating a board as well as task.

2.In 3rd part of project we have to use save() funtion to create board and task beacouse of we dont have status and end_time to store.

3.In add task 1st i have retrieved open board and then i added a task to open board.

4.In close task i have used current time function to get end time of project and store it database.

5.For update task and list board i have executed a same plan as i uased in 1st tow part of project.

6.In export_board i have to use 2 database to retrieve a need data for our API and convert that data into text file as per need.

