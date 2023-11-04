from .models import userData
from rest_framework import serializers




class testS(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    display_name = serializers.CharField(max_length=64)

    class Meta:
        model = userData
        fields = ("name","display_name")

    def create(self, validated_data):
        return userData.objects.create(**validated_data)




class listS(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    display_name = serializers.CharField(max_length=64)
    creation_time = serializers.DateField()

    class Meta:
        model = userData
        fields = ("name","display_name", "creation_time")

    def create(self, validated_data):
        return userData.objects.create(**validated_data)





class describeS(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=128)
    display_name = serializers.CharField(max_length=64)

    class Meta:
        model = userData
        fields = ("name","display_name")

    def create(self, validated_data):
        return userData.objects.create(**validated_data)




class ForTeamS(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=64)
    display_name = serializers.CharField(max_length=64)

    class Meta:
        model = userData
        fields = ("id","name","display_name")

    def create(self, validated_data):
        return userData.objects.create(**validated_data)


