from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username','first_name', 'last_name', 'email'] 
        
class UserAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = models.UserAccount
        fields = ['user', 'image', 'mobile_no', 'account_type']
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    account_type = serializers.CharField(required = True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password', 'confirm_password','account_type']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        account_type = self.validated_data['account_type']
       
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        
        models.UserAccount.objects.create(
        user = account,
        account_type = account_type,
        )
        return account
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
