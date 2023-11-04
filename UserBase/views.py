from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import listS, testS, describeS
from .models import userData
from TeamBase.models import TeamData
from TeamBase.serializers import ForUserFilterS


# create a user

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data1 = JSONParser().parse(request)
        outdata = testS(data=data1)
        if outdata.is_valid():
            outdata.save()
            name=data1["name"]
            id = userData.objects.filter(name=name).values("id")
            return JsonResponse({'id': id[0]['id']}, safe=False)
        else:
            return JsonResponse(outdata.error, safe=False)





# list all users

@csrf_exempt
def list_users(request):
    if request.method == "GET":
        output = userData.objects.all()
        print(output)
        outdata = listS(output, many=True)
        return JsonResponse(outdata.data, safe=False)




# describe user

@csrf_exempt
def describe_user(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        output = userData.objects.all().filter(id=id)
        outdata = describeS(output, many=True)
        return JsonResponse(outdata.data, safe=False)






# update user

@csrf_exempt
def update_user(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        userdata=data1["user"]
        name=userdata['name']
        display_name=userdata['display_name']
        userData.objects.filter(id=id).update(name=name,display_name=display_name)
        return JsonResponse({"massage":"update successful"}, safe=False)





#get teams of user

@csrf_exempt
def get_user_teams(request):
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        id = data1["id"]
        teamIDs=TeamData.objects.all().values("id")
        for i in teamIDs:
            shortID=TeamData.objects.all().filter(id=i["id"]).values("users")
            for j in shortID[0]['users']:
                if id == j:
                    print(id)
                    output = TeamData.objects.all().filter(id=i['id'])
                    print(output)
                    outdata = ForUserFilterS(output, many=True)
                    return JsonResponse(outdata.data, safe=False)
                else:
                    pass


