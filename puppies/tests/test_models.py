from django.test import TestCase
from ..models import puppy

# Create your tests here.
class puppytest(TestCase):
	def setUp(self):
		puppy.objects.create(name="Casper",age=3,breed="Bull Dog",color="Black")
		puppy.objects.create(name="Muffin",age=1,breed="Grandane",color="White")

	def test_puppy(self):
		puppy_casper=puppy.objects.get(name="Casper")
		puppy_muffin=puppy.objects.get(name="Muffin")
		
		self.assertEqual(puppy_casper.get_breed(),"Casper belongs to Bull Dog breed.")