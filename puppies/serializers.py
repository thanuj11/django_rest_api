from rest_framework import serializers
from .models import puppy

class puppyserializer(serializers.ModelSerializer):
	class Meta:
		model=puppy
		fields=('name','age','breed','color','created_at','updated_at')