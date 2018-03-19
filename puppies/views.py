from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import puppy
from .serializers import puppyserializer
# Create your views here.

@api_view(['GET','DELETE','PUT'])
def get_delete_update_puppy(request, pk):
	try:
		p= puppy.objects.get(pk= pk)
	except puppy.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method=='GET':
		puppies=puppy.objects.get(pk=pk)
		serializer=puppyserializer(puppies)
		return Response(serializer.data)
	elif request.method=='POST':
		return Response({})
	elif request.method=='PUT':
		serializer = puppyserializer(p, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	if request.method=='DELETE':
		p.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	
		
		
@api_view(['GET','POST'])
def get_post_puppy(request):
	
		
	if request.method=='GET':
		puppies=puppy.objects.all()
		serializer=puppyserializer(puppies,many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		data = {
			'name': request.data.get('name'),
			'age': int(request.data.get('age')),
			'breed': request.data.get('breed'),
			'color': request.data.get('color')
		}
		serializer = puppyserializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	