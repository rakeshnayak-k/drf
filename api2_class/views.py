from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Students
from rest_framework import status


# Create your views here.
class StudentsAPI(APIView):
    def get(self,request,format=None):
        try:
            in_id = request.data.get('id',None)
            if in_id is not None:
                stu = Students.objects.get(id=in_id)
                serializer = StudentSerializer(stu)
                return Response({'Students':serializer.data})
            stu = Students.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response({'Students':serializer.data})
        except Exception as e:
            return Response({'error msg':str(e)})
    
    def post(self, request, format=None):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Student Created'}, status=status.HTTP_201_CREATED)
            return Response({'error msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error msg':str(e)})
    
    def put(self, request, format=None):
        try:
            id = request.data.get('id',None)
            stu = Students.objects.get(pk=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Student Updated'},status=status.HTTP_201_CREATED)
            return Response({'error msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        try:
            id = request.data.get('id',None)
            stu = Students.objects.get(pk=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Student Updated'},status=status.HTTP_201_CREATED)
            return Response({'error msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, format=None):
        try:
            id = request.data.get('id',None)
            stu = Students.objects.get(pk=id)
            stu.delete()
            return Response({'msg':'Student deleted'})
        except Exception as e:
            return Response({'error msg':str(e)})