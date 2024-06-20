from .models import MyUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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

class LoginObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 添加额外信息
        token['username'] = user.username
        return token

class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        if not user.is_staff:
            raise serializers.ValidationError('User is not staff')

        refresh = self.get_token(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)


        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 添加额外信息
        token['username'] = user.username
        return token
