from django.test import TestCase
from django.urls import reverse

from faker import Faker

from rest_framework.test import APITestCase, APIClient

class TestSetup(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()

        self.user_data = {
            'first_name': self.fake.name().split(' ')[0],
            'last_name': self.fake.name().split(' ')[1],
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown
