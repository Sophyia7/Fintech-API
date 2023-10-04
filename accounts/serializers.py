# rest_framework imports 
from rest_framework import serializers

# App imports
from accounts.models import User



class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
        
# This is hash the User's password and not return the exact inputed password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
            
            
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["email", "password"]


class ResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["email"]

class ResetPasswordSeriliazer(serializers.Serializer):
    password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["password"]

class LogoutSeriliazer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["RefreshToken"]
