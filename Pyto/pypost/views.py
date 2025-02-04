from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def index(request):
    return HttpResponse("Hello, world. You're at the pypost index.")

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializers(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_posts(request):
    serializer = PostSerializers (data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
