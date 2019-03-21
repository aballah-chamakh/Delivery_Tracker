from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status,generics
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #permissons_classes = (IsOwnerOrReadOnly,)
    @action(methods=['PUT'],detail=True)
    def set_password(self,request,pk):
        user_obj = self.get_object()
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if old_password and new_password :
            if user_obj.check_password(old_password):
                user_obj.set_password(new_password)
                user_obj.save()
                return Response({'response':'password updated'},status=status.HTTP_200_OK)
            else :
                return Response({'response':'invalid password'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'you miss a field'},status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['GET'],detail=False)
    def get_user_info(self,request):
        user_obj = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user_obj,many=False,context={'request':request})
        return Response({'user_info':serializer.data},status=status.HTTP_200_OK)
    @action(methods=['POST'],detail=False)
    def email_exist(self,request):
        email  = request.data.get('email')
        qs = User.objects.filter(email=email)
        if qs :
            return Response({'exist':True},status=status.HTTP_200_OK)
        else :
            return Response({'exist':False},status=status.HTTP_200_OK)
