from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import TeamDataS, TeamlistS, TeamdescribeS
from .models import TeamData
from UserBase.models import userData
from UserBase.serializers import ForTeamS



# create a team

@csrf_exempt
def create_team(request):
    if request.method == 'POST':
        data1 = JSONParser().parse(request)
        outdata = TeamDataS(data=data1)
        if outdata.is_valid():
            outdata.save()
            name=data1["name"]
            id = TeamData.objects.filter(name=name).values("id")
            return JsonResponse({'id': id[0]['id']}, safe=False)
        else:
            return JsonResponse(outdata.error, safe=False)



# list all teams

@csrf_exempt
def list_teams(request):
    if request.method == "GET":
        output = TeamData.objects.all()
        outdata = TeamlistS(output, many=True)
        return JsonResponse(outdata.data, safe=False)





# describe team

@csrf_exempt
def describe_team(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        output = TeamData.objects.all().filter(id=id)
        outdata = TeamdescribeS(output, many=True)
        return JsonResponse(outdata.data, safe=False)





# update team

@csrf_exempt
def update_team(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        teamdata=data1["team"]
        name=teamdata['name']
        description=teamdata['description']
        admin=teamdata['admin']
        TeamData.objects.filter(id=id).update(name=name,description=description,admin=admin)
        return JsonResponse({"massage": "update successful"}, safe=False)





# add users to team

@csrf_exempt
def add_users_to_team(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        users=data1["users"]
        list1 = TeamData.objects.filter(id=id).values("users")
        DataBlist = list1[0]["users"]

        if len(DataBlist) <= 50:
            counter=len(DataBlist) + len(users)
            print(counter)
            if counter<=50:
                toAdd=DataBlist+users
                TeamData.objects.filter(id=id).update( users=toAdd)
                return JsonResponse({"massage": "users added successfully"}, safe=False)

            else:
                pass
        else:
            pass



# remove users to team

@csrf_exempt
def remove_users_from_team(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        users = data1["users"]
        list1 = TeamData.objects.filter(id=id).values("users")
        DataBlist = list1[0]["users"]
        for i in range(len(users)):
            DataBlist.remove(int(users[i]))

        TeamData.objects.filter(id=id).update(id=id, users=DataBlist)
        return JsonResponse({"massage": "users removed successfully"}, safe=False)



# list users of a team

@csrf_exempt
def list_team_users(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        list1 = TeamData.objects.filter(id=id).values("users")
        DataBlist = list1[0]["users"]
        print(DataBlist)
        outQ = userData.objects.all().filter(id__in=DataBlist)
        outdata = ForTeamS(outQ, many=True)
        return JsonResponse(outdata.data, safe=False)
