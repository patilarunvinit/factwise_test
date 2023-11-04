from .models import TeamData
from rest_framework import serializers

from django.db.models import IntegerField
from django_mysql.models import ListTextField




class TeamDataS(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=128)
    admin = serializers.CharField(max_length=64)


    class Meta:
        model = TeamData
        fields = ("name","description","admin")

    def create(self, validated_data):
        return TeamData.objects.create(**validated_data)





class TeamlistS(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=128)
    creation_time = serializers.DateField()
    admin = serializers.CharField(max_length=64)

    class Meta:
        model = TeamData
        fields = ("name","description", "creation_time","admin")

    def create(self, validated_data):
        return TeamData.objects.create(**validated_data)





class TeamdescribeS(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=128)
    creation_time = serializers.DateField()
    admin = serializers.CharField(max_length=64)


    class Meta:
        model = TeamData
        fields = ("name","description", "creation_time","admin")

    def create(self, validated_data):
        return TeamData.objects.create(**validated_data)



class testS(serializers.Serializer):
    users = ListTextField(
        base_field=IntegerField(),
        size=50,
    )

    class Meta:
        model = TeamData
        fields = ("users")

    def create(self, validated_data):
        return TeamData.objects.create(**validated_data)




class ForUserFilterS(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=128)
    creation_time = serializers.DateField()


    class Meta:
        model = TeamData
        fields = ("name","description", "creation_time")

    def create(self, validated_data):
        return TeamData.objects.create(**validated_data)






