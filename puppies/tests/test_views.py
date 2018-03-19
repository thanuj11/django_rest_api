import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import puppy
from ..serializers import puppyserializer
from ..views import get_post_puppy

# initialize the APIClient app
client = Client()

class GetAllpuppies(TestCase):
	def setUp(self):
		puppy.objects.create(name="Casper",age=3,breed="Bull Dog",color="Black")
		puppy.objects.create(name="Muffin",age=1,breed="Grandane",color="White")
	def test_all_puppies(self):
		response=client.get(reverse('post_puppy'))
		
		puppies=puppy.objects.all()
		
		serializer=puppyserializer(puppies,many=True)
		self.assertEqual(response.data,serializer.data)
		
#class GetSinglepuppies(TestCase):
#	def setUp(self):
#		puppy.objects.create(name="Casper",age=3,breed="Bull Dog",color="Black")
#		puppy.objects.create(name="Muffin",age=1,breed="Grandane",color="White")
#	def test_all_puppies(self):
#		response=client.get(reverse('get_delete', kwargs={'pk': 1}))
		
#		puppies=puppy.objects.get(name="Casper")
		
#		serializer=puppyserializer(puppies)
#		self.assertEqual(response.data,serializer.data)

class UpdateSinglePuppyTest(TestCase):
	def setUp(self):
		self.casper = puppy.objects.create(
			name='Casper', age=3, breed='Bull Dog', color='Black')
		self.muffin = puppy.objects.create(
			name='Muffy', age=1, breed='Gradane', color='Brown')
		self.valid_payload = {
			'name': 'Muffy',
			'age': 2,
			'breed': 'Labrador',
			'color': 'Black'
		}
		self.invalid_payload = {
			'name': '',
			'age': 4,
			'breed': 'Pamerion',
			'color': 'White'
		}

	def test_valid_update_puppy(self):
		response = client.put(
			reverse('get_delete', kwargs={'pk': self.muffin.pk}),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, 200)

	def test_invalid_update_puppy(self):
		response = client.put(
			reverse('get_delete', kwargs={'pk': self.muffin.pk}),
			data=json.dumps(self.invalid_payload),
			content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		
		
		
	def test_valid_delete_puppy(self):
		response = client.delete(
			reverse('get_delete', kwargs={'pk': self.muffin.pk}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_delete_puppy(self):
		response = client.delete(
			reverse('get_delete', kwargs={'pk': 30}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)