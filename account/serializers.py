from .models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)

    #user_type = serializers.SerializerMethodField('get_user_type_info')
    class Meta :
        model = User
        fields =('id','username','email','password','password2','isdriver','isdeliverycompany')
    def validate(self,data):
        email = data.get('email')
        qs = User.objects.filter(email=email)
        if qs :
            raise serializers.ValidationError('email already exist')
        pw1 = data.get('password')
        pw2 = data.pop('password2')
        # chech if the two password match
        if pw1 != pw2 :
            raise serializers.ValidationError('Passwords should match')
        return data
    def create(self,validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user_obj = User(username=username,email=email)
        user_obj.set_password(password) # to save the password in a hashed format
        user_obj.save()
        return user_obj
    # def get_user_type_info(self,user_obj):
    #     if user.isdeliverycompany :
    #         deliverycompany_obj = user.deliverycompany
    #         serializer = DeliveryCompanySerializer(deliverycompany,many=False)
    #         return serializer.data
    #     elif user.isdriver :
    #         driver_obj = user_obj.driver
    #         serializer = DriverSerializer(drier_obj,many=False)
    #         return serializer.data
        # other then that we add on the futur isecommerce condition



class SimpleUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    class Meta :
        model  = User
        fields = ('id','username')
