from .models import MyUser
from rest_framework import serializers


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = MyUser
        fields = "__all__"
    
    def create(self,validated_data):
        user = MyUser.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password'],
            birthday = validated_data.get('birthday',None),
            sex = validated_data.get('sex',""),
        )

        return user

    def update(self,instance,validated_data):
        password = validated_data.pop('password',None)

        for attr , value in validated_data.items():
            setattr(instance,attr,value)
        
        if password :
            instance.set_password(password)
        instance.save()
        return instance