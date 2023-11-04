from .models import BoardData
from rest_framework import serializers




class BoardDataS(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=128)
    team_id = serializers.IntegerField()
    creation_time = serializers.DateField()
    status = serializers.CharField(max_length=15)
    end_time = serializers.DateField( )

    class Meta:
        model = BoardData
        fields = ("id","name","description","team_id","creation_time","status","end_time")

    def create(self, validated_data):
        return BoardData.objects.create(**validated_data)




class ListBS(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=64)


    class Meta:
        model = BoardData
        fields = ("id","name")

    def create(self, validated_data):
        return BoardData.objects.create(**validated_data)

