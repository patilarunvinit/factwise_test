from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ListBS
from .models import BoardData, TaskData
import datetime


# create a board

@csrf_exempt
def create_board(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['name']
        description = data['description']
        team_id = data['team_id']
        creation_time = data['creation_time']
        out = BoardData(name=name,description=description,team_id=team_id,creation_time=creation_time)
        out.save()
        id = BoardData.objects.filter(name=name).values("id")
        return JsonResponse({'id': id[0]['id']}, safe=False)





# close a board

@csrf_exempt
def close_board(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        id = data['id']
        status="CLOSE"
        current_time = datetime.datetime.now()
        end_time=current_time
        BoardData.objects.filter(id=id).update(status=status,end_time=end_time)
        return JsonResponse({"massage": "Board successful closed" }, safe=False)





# add task to board

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        title = data['title']
        description = data['description']
        user_id = data['user_id']
        creation_time = data['creation_time']
        openB=BoardData.objects.filter(status="OPEN").values("name")
        for i in openB:
            if i["name"]==title:
                out = TaskData(title=title, description=description, user_id=user_id, creation_time=creation_time)
                out.save()
                id = TaskData.objects.filter(title=title).values("id")
                return JsonResponse({'id': id[0]['id']}, safe=False)
                break
            else:
                pass

        return JsonResponse({"massage": "Sorry Board is closed"}, safe=False)






# update the status of a task

@csrf_exempt
def update_task_status(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        id = data['id']
        status = data['status']
        TaskData.objects.filter(id=id).update(status=status)
        return JsonResponse({"massage": "Taks Status Updated"}, safe=False)





# list all open boards for a team

@csrf_exempt
def list_boards(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        id = data['id']
        outQ = BoardData.objects.all().filter(team_id=id)
        outdata = ListBS(outQ, many=True)
        return JsonResponse(outdata.data, safe=False)





#Create a text.file of given Boards

@csrf_exempt
def export_board(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        id = data['id']
        BoutQ = BoardData.objects.filter(id=id).values("id","name","description","team_id","creation_time","status","end_time")
        name=BoutQ[0]['name']
        TASKoutQ = TaskData.objects.filter(title=name).values("id","title","description","user_id","creation_time","status")
        if TASKoutQ:
            filename = "presentable_board"
            with open(filename + ".txt", 'w') as f:
                f.write(f"**view of the Board**\n")
                f.write(f" \n")
                f.write(f"id = {BoutQ[0]['id']} \n")
                f.write(f"name = {BoutQ[0]['name']} \n")
                f.write(f"description = {BoutQ[0]['description']} \n")
                f.write(f"team_id = {BoutQ[0]['team_id']} \n")
                f.write(f"creation_time = {BoutQ[0]['creation_time']} \n")
                f.write(f"status = {BoutQ[0]['status']} \n")
                f.write(f"end_time = {BoutQ[0]['end_time']} \n")
                f.write(f" \n")
                f.write(f"------------------------------------ \n")
                f.write(f" \n")
                f.write(f"**tasks of Board**\n")
                f.write(f" \n")
                f.write(f"id = {TASKoutQ[0]['id']} \n")
                f.write(f"title = {TASKoutQ[0]['title']} \n")
                f.write(f"description = {TASKoutQ[0]['description']} \n")
                f.write(f"user_id = {TASKoutQ[0]['user_id']} \n")
                f.write(f"creation_time = {TASKoutQ[0]['creation_time']} \n")
                f.write(f"status = {TASKoutQ[0]['status']} \n")

            return JsonResponse({"out_file": filename}, safe=False)
        else:
            filename = "presentable_board"
            with open(filename + ".txt", 'w') as f:
                f.write(f"**view of the Board**\n")
                f.write(f" \n")
                f.write(f"id = {BoutQ[0]['id']} \n")
                f.write(f"name = {BoutQ[0]['name']} \n")
                f.write(f"description = {BoutQ[0]['description']} \n")
                f.write(f"team_id = {BoutQ[0]['team_id']} \n")
                f.write(f"creation_time = {BoutQ[0]['creation_time']} \n")
                f.write(f"status = {BoutQ[0]['status']} \n")
                f.write(f"end_time = {BoutQ[0]['end_time']} \n")
                f.write(f" \n")
                f.write(f"------------------------------------ \n")
                f.write(f" \n")
                f.write(f"**task of Board**\n")
                f.write(f" \n")
                f.write(f"There is no task with given Board \n")
            return JsonResponse({"out_file": filename}, safe=False)










